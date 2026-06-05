import os
import json
import shutil

# Paths
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON_PATH = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
APP_DATA_DIR = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596"
CACHE_DIR = os.path.join(APP_DATA_DIR, "original_cache")

def cache_originals():
    if not os.path.exists(CURATED_JSON_PATH):
        print(f"Error: Curated candidates file {CURATED_JSON_PATH} not found.")
        return
        
    with open(CURATED_JSON_PATH, "r") as f:
        candidates = json.load(f)
        
    print(f"Caching original files for {len(candidates)} candidates...")
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    copied_count = 0
    skipped_count = 0
    
    for item in candidates:
        src_path = item["file_path"]
        cand_id = item["cand_id"]
        filename = item["filename"]
        
        # Suffix with cand_id to avoid name collisions if different folders have same file name
        cache_filename = f"{cand_id}_{filename}"
        dest_path = os.path.join(CACHE_DIR, cache_filename)
        
        # Check if already cached
        if os.path.exists(dest_path) and os.path.getsize(dest_path) == os.path.getsize(src_path):
            skipped_count += 1
            # Update path in candidates json to point to local cache
            item["cached_path"] = dest_path
            continue
            
        if os.path.exists(src_path):
            try:
                shutil.copy2(src_path, dest_path)
                item["cached_path"] = dest_path
                copied_count += 1
            except Exception as e:
                print(f"Error copying {src_path} to cache: {e}")
        else:
            print(f"Source file not found: {src_path}")
            
    # Update curated candidates JSON with the local cache path reference
    with open(CURATED_JSON_PATH, "w") as f:
        json.dump(candidates, f, indent=2)
        
    print(f"\nCaching complete!")
    print(f"Copied to local cache: {copied_count} files.")
    print(f"Already cached: {skipped_count} files.")
    print(f"Local cache directory: {CACHE_DIR}")

if __name__ == "__main__":
    cache_originals()
