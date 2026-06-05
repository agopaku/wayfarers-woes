import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

updated_count = 0
for cand in candidates:
    cid = cand["cand_id"]
    if cid == "CAND_092":
        cand["title"] = "Triumph Tiger in the Ozarks"
        cand["location"] = "Ozark National Forest, Arkansas, USA"
        cand["description"] = "Riding my Triumph Tiger motorcycle through the winding mountain roads of the Ozark National Forest on the way to White Rock Mountain."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_092 details.")
    elif cid == "CAND_093":
        cand["title"] = "Ozark Scenic Riding Trails"
        cand["location"] = "Ozark National Forest, Arkansas, USA"
        cand["description"] = "Navigating the gravel forest service roads and scenic overlooks of the Ozarks on the Triumph Tiger."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_093 details.")
    elif cid == "CAND_094":
        cand["title"] = "White Rock Mountain Summit"
        cand["location"] = "White Rock Mountain, Arkansas, USA"
        cand["description"] = "Reaching the spectacular, isolated summit of White Rock Mountain, enjoying panoramic views of the surrounding hills."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_094 details.")
    elif cid == "CAND_095":
        cand["title"] = "Sunset at White Rock Mountain"
        cand["location"] = "White Rock Mountain, Arkansas, USA"
        cand["description"] = "A quiet, peaceful sunset casting warm orange hues over the endless forest valleys of the Ozarks from White Rock Mountain."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_095 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
