import http.server
import socketserver
import json
import os
import sys
import subprocess
import urllib.parse

PORT = 8080
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
APP_DATA_DIR = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596"
PREVIEWS_DIR = os.path.join(APP_DATA_DIR, "previews")
CURATED_JSON_PATH = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
EXCLUDED_JSON_PATH = os.path.join(BASE_DIR, "scratch/excluded_filenames.json")
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
APPROVED_IMPORT_JSON = os.path.join(BASE_DIR, "scratch/approved_import.json")

class ReviewHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html_path = os.path.join(BASE_DIR, "scratch/review.html")
            with open(html_path, "rb") as f:
                self.wfile.write(f.read())
            return

        elif path == "/api/candidates":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            # Load candidates
            candidates = []
            if os.path.exists(CURATED_JSON_PATH):
                with open(CURATED_JSON_PATH, "r") as f:
                    candidates = json.load(f)

            # Load excluded
            excluded = set()
            if os.path.exists(EXCLUDED_JSON_PATH):
                with open(EXCLUDED_JSON_PATH, "r") as f:
                    excluded = set(json.load(f))

            # Load gallery
            imported = set()
            if os.path.exists(GALLERY_JSON_PATH):
                with open(GALLERY_JSON_PATH, "r") as f:
                    gallery = json.load(f)
                for item in gallery:
                    base = os.path.basename(item.get("filename", "")).lower()
                    if base:
                        imported.add(base)

            # Filter remaining
            active = []
            for c in candidates:
                base = c["filename"].lower()
                if base not in excluded and base not in imported:
                    # Inject preview path relative to web server
                    c["preview_url"] = f"/previews/{c['cand_id']}_{c['filename']}"
                    active.append(c)

            self.wfile.write(json.dumps(active).encode('utf-8'))
            return

        elif path.startswith("/previews/"):
            filename = urllib.parse.unquote(path.replace("/previews/", ""))
            file_path = os.path.join(PREVIEWS_DIR, filename)
            if os.path.exists(file_path):
                self.send_response(200)
                if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                    self.send_header("Content-Type", "image/jpeg")
                elif filename.lower().endswith(".png"):
                    self.send_header("Content-Type", "image/png")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found")
            return

        else:
            # Fallback
            super().do_GET()

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if path == "/api/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            approvals = data.get("approvals", []) # list of dicts
            rejections = data.get("rejections", []) # list of cand_ids

            print(f"Received submit API request. Approvals: {len(approvals)}, Rejections: {len(rejections)}")

            # 1. Process rejections: add to excluded_filenames.json
            if rejections:
                candidates_by_id = {}
                if os.path.exists(CURATED_JSON_PATH):
                    with open(CURATED_JSON_PATH, "r") as f:
                        for c in json.load(f):
                            candidates_by_id[c["cand_id"]] = c

                excluded = set()
                if os.path.exists(EXCLUDED_JSON_PATH):
                    with open(EXCLUDED_JSON_PATH, "r") as f:
                        excluded = set(json.load(f))

                for cid in rejections:
                    if cid in candidates_by_id:
                        excluded.add(candidates_by_id[cid]["filename"].lower())

                with open(EXCLUDED_JSON_PATH, "w") as f:
                    json.dump(list(sorted(excluded)), f, indent=2)

            # 2. Process approvals: write to approved_import.json
            if approvals:
                # Load current approved_import or create fresh
                current_approved = []
                # Overwrite/save the currently approved list for this batch
                with open(APPROVED_IMPORT_JSON, "w") as f:
                    json.dump(approvals, f, indent=2)

                # Run import script
                import_script = os.path.join(BASE_DIR, "scratch/import_approved_photos.py")
                print(f"Running import script: {import_script}")
                res = subprocess.run(["python3", import_script], capture_output=True, text=True)
                print("Import stdout:", res.stdout)
                print("Import stderr:", res.stderr)

            # 3. Regenerate review sheet (cleans up candidate_gallery.md)
            regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
            print(f"Running sheet regeneration: {regen_script}")
            res_regen = subprocess.run(["python3", regen_script], capture_output=True, text=True)
            print("Regen stdout:", res_regen.stdout)

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"success": True, "message": f"Processed {len(approvals)} approvals and {len(rejections)} rejections."}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        elif path == "/api/review/update":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            cand_id = data.get("cand_id")
            status = data.get("status", "none")
            title = data.get("title", "")
            description = data.get("description", "")
            location = data.get("location", "")
            category = data.get("category", "landscape")

            print(f"Updating candidate {cand_id}: status={status}, title={title}")

            # Load candidates
            if os.path.exists(CURATED_JSON_PATH):
                with open(CURATED_JSON_PATH, "r") as f:
                    candidates = json.load(f)
                
                updated = False
                for c in candidates:
                    if c["cand_id"] == cand_id:
                        c["status"] = status
                        c["title"] = title
                        c["description"] = description
                        c["location"] = location
                        c["category"] = category
                        updated = True
                        break
                
                if updated:
                    with open(CURATED_JSON_PATH, "w") as f:
                        json.dump(candidates, f, indent=2)
                    
                    # Regenerate review sheet in background to match candidate_gallery.md
                    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
                    subprocess.run(["python3", regen_script], capture_output=True, text=True)

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"success": True, "message": f"Updated candidate {cand_id}."}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        else:
            self.send_error(404, "Endpoint not found")

class ThreadingHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    # Ensure port is not blocked, retry if needed
    server_address = ("", PORT)
    print(f"Starting photo review server at http://localhost:{PORT}")
    try:
        with ThreadingHTTPServer(server_address, ReviewHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)
