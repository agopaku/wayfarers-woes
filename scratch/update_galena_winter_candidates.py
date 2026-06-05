import os
import json
import subprocess

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
    if cid == "CAND_130":
        cand["title"] = "Winter Day in Galena"
        cand["location"] = "Galena, Illinois, USA"
        cand["description"] = "A snow-covered winter day in historic Galena, Illinois, enjoying the crisp air and quiet landscape."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_130 details.")
    elif cid == "CAND_131":
        cand["title"] = "Galena Snowy Getaway"
        cand["location"] = "Galena, Illinois, USA"
        cand["description"] = "Enjoying a peaceful winter weekend getaway in the snowy hills of Galena."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_131 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
