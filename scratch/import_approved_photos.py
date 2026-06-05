import os
import json
from datetime import datetime
from PIL import Image

# Paths
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
CURATED_JSON_PATH = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
APPROVED_IMPORT_JSON = os.path.join(BASE_DIR, "scratch/approved_import.json")

DEST_DIR = os.path.join(BASE_DIR, "images/ag-edits")
THUMB_DIR = os.path.join(BASE_DIR, "images/ag-edits-thumbnails")

def format_date_display(dt_str):
    if not dt_str or dt_str.lower() == "unknown":
        return ""
    try:
        # Expected: YYYY-MM-DD HH:MM:SS or similar
        dt = datetime.strptime(dt_str.split()[0], "%Y-%m-%d")
        return dt.strftime("%b %d, %Y") # e.g. "May 17, 2016"
    except Exception:
        return dt_str

def import_approved():
    if not os.path.exists(APPROVED_IMPORT_JSON):
        print(f"Error: Approved import file {APPROVED_IMPORT_JSON} not found.")
        return
        
    if not os.path.exists(CURATED_JSON_PATH):
        print(f"Error: Curated candidates file {CURATED_JSON_PATH} not found.")
        return
        
    with open(APPROVED_IMPORT_JSON, "r") as f:
        approved_items = json.load(f) # List of dicts with keys: cand_id, title, description, location, category
        
    with open(CURATED_JSON_PATH, "r") as f:
        curated_items = {x["cand_id"]: x for x in json.load(f)}
        
    # Load current gallery
    current_gallery = []
    if os.path.exists(GALLERY_JSON_PATH):
        with open(GALLERY_JSON_PATH, "r") as f:
            current_gallery = json.load(f)
            
    # Track existing filenames to avoid duplicates
    existing_filenames = {os.path.basename(x.get("filename", "")).lower() for x in current_gallery}
    
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(THUMB_DIR, exist_ok=True)
    
    imported_count = 0
    
    for app in approved_items:
        cand_id = app["cand_id"]
        if cand_id not in curated_items:
            print(f"Warning: {cand_id} not found in curated candidates. Skipping.")
            continue
            
        cand = curated_items[cand_id]
        src_path = cand.get("cached_path") or cand["file_path"]
        filename = cand["filename"]
        
        # Check for duplicate in gallery
        if filename.lower() in existing_filenames:
            print(f"Image {filename} already exists in gallery.json. Skipping.")
            continue
            
        dest_path = os.path.join(DEST_DIR, filename)
        thumb_path = os.path.join(THUMB_DIR, filename)
        
        # 1. Optimize and resize original (2048px max dimension)
        try:
            print(f"Optimizing original: {filename}...")
            with Image.open(src_path) as img:
                exif_data = img.info.get('exif')
                img.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
                if exif_data:
                    img.save(dest_path, "JPEG", quality=85, optimize=True, exif=exif_data)
                else:
                    img.save(dest_path, "JPEG", quality=85, optimize=True)
        except Exception as e:
            print(f"Error processing original for {filename}: {e}")
            continue
            
        # 2. Generate thumbnail (800px max dimension)
        try:
            print(f"Generating thumbnail: {filename}...")
            with Image.open(src_path) as img:
                img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                img.save(thumb_path, "JPEG", quality=85, optimize=True)
        except Exception as e:
            print(f"Error generating thumbnail for {filename}: {e}")
            if os.path.exists(dest_path):
                os.remove(dest_path)
            continue
            
        # 3. Create entry
        meta = cand["metadata"]
        entry = {
            "filename": f"images/ag-edits/{filename}",
            "title": app.get("title") or f"{cand['folder']} - {filename}",
            "description": app.get("description") or f"Photo taken on {cand['date_taken']}.",
            "location": app.get("location") or "Unknown Location",
            "date": format_date_display(cand["date_taken"]),
            "camera": meta.get("camera") or "",
            "lens": meta.get("lens") or "",
            "aperture": meta.get("aperture") or "",
            "shutterSpeed": meta.get("shutter_speed") or "",
            "iso": meta.get("iso") or "",
            "focalLength": meta.get("focal_length") or "",
            "category": app.get("category") or "landscape"
        }
        
        current_gallery.append(entry)
        existing_filenames.add(filename.lower())
        imported_count += 1
        print(f"✓ Imported {filename} successfully!")
        
    if imported_count == 0:
        print("No new images imported.")
        return
        
    # Re-sort current_gallery chronologically
    def parse_entry_date(item):
        d_str = item.get("date", "")
        # Try custom formatted date e.g. "May 17, 2016"
        try:
            return datetime.strptime(d_str, "%b %d, %Y")
        except ValueError:
            pass
        # Fallback to current time if no date
        return datetime.max
        
    current_gallery.sort(key=parse_entry_date)
    
    # Save back to gallery.json
    with open(GALLERY_JSON_PATH, "w") as f:
        json.dump(current_gallery, f, indent=2)
        
    print(f"\nImport finished! Successfully imported {imported_count} images.")
    print(f"Updated {GALLERY_JSON_PATH} (total entries: {len(current_gallery)}).")

if __name__ == "__main__":
    import_approved()
