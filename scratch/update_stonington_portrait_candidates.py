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
    if cid == "CAND_206":
        cand["title"] = "Anil at Stonington Point"
        cand["location"] = "Stonington Point, Stonington, Connecticut, USA"
        cand["description"] = "Anil standing along the scenic rocky coastline of Stonington Point, Connecticut, during our winter New England road trip."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_206 details.")
    elif cid == "CAND_207":
        cand["title"] = "Ankita at Stonington Point"
        cand["location"] = "Stonington Point, Stonington, Connecticut, USA"
        cand["description"] = "A lovely sunset portrait of Ankita smiling by the rocky shore of Stonington Point, Connecticut, during our winter road trip."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_207 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
    if res.stderr:
        print("Regenerate Sheet stderr:", res.stderr)
else:
    print(f"Error: Could not find CAND_206 or CAND_207. Updated count: {updated_count}")
