import json
import os

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
CURATED_JSON_PATH = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

def main():
    if not os.path.exists(GALLERY_JSON_PATH) or not os.path.exists(CURATED_JSON_PATH):
        print("Required files not found.")
        return
        
    with open(GALLERY_JSON_PATH, "r") as f:
        gallery = json.load(f)
        
    with open(CURATED_JSON_PATH, "r") as f:
        candidates = json.load(f)
        
    # Map from lowercase filename to candidate
    candidates_by_filename = {c["filename"].lower(): c for c in candidates}
    
    updated_count = 0
    for entry in gallery:
        filename = os.path.basename(entry["filename"]).lower()
        if filename in candidates_by_filename:
            cand = candidates_by_filename[filename]
            
            # Prefer story, fallback to description
            story = cand.get("story", "").strip() or cand.get("description", "").strip()
            
            # Check if any field differs
            changed = False
            if entry.get("title") != cand.get("title"):
                entry["title"] = cand.get("title")
                changed = True
            if entry.get("description") != story:
                entry["description"] = story
                changed = True
            if entry.get("location") != cand.get("location"):
                entry["location"] = cand.get("location")
                changed = True
            if entry.get("category") != cand.get("category"):
                entry["category"] = cand.get("category")
                changed = True
                
            if changed:
                updated_count += 1
                
    if updated_count > 0:
        with open(GALLERY_JSON_PATH, "w") as f:
            json.dump(gallery, f, indent=2)
        print(f"Successfully synced metadata for {updated_count} gallery entries with curated candidates.")
    else:
        print("Gallery metadata is already in sync.")

if __name__ == "__main__":
    main()
