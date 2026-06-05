import json
import os
import subprocess

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
EXCLUDED_JSON = os.path.join(BASE_DIR, "scratch/excluded_filenames.json")

def main():
    if not os.path.exists(CURATED_JSON) or not os.path.exists(EXCLUDED_JSON):
        print("Required files not found.")
        return
        
    with open(CURATED_JSON, "r") as f:
        candidates = json.load(f)
        
    with open(EXCLUDED_JSON, "r") as f:
        excluded = set(json.load(f))
        
    initial_count = len(excluded)
    
    # Add all rejected candidates to the persistent exclusion list
    for cand in candidates:
        if cand.get("status") == "reject":
            filename_l = cand["filename"].lower()
            excluded.add(filename_l)
            
    # Also, we can add a status field update if they are in excluded but not marked reject
    # but the primary goal is to hide them.
    
    new_count = len(excluded)
    if new_count > initial_count:
        with open(EXCLUDED_JSON, "w") as f:
            json.dump(list(sorted(excluded)), f, indent=2)
        print(f"Added {new_count - initial_count} rejected filenames to excluded_filenames.json. Total excluded: {new_count}")
        
        # Re-run sheet regeneration
        regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
        res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
        print("Regenerate Sheet stdout:", res.stdout)
    else:
        print("No new rejections to exclude.")

if __name__ == "__main__":
    main()
