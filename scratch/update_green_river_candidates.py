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
    if cid == "CAND_162":
        cand["title"] = "Perseids Meteor Shower at Green River"
        cand["location"] = "Green River State Wildlife Management Area, Harmon, Illinois, USA"
        cand["description"] = "A stunning long-exposure night sky photograph capturing stars during the peak of the Perseids meteor shower at Green River State Wildlife Management Area, a premier dark sky viewing site near Aurora, Illinois."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_162 details.")
    elif cid == "CAND_163":
        cand["title"] = "Stargazing and Chasing Meteors"
        cand["location"] = "Green River State Wildlife Management Area, Harmon, Illinois, USA"
        cand["description"] = "Another long-exposure capture of the starry night sky during the Perseids meteor shower, taken at Green River State Wildlife Management Area."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_163 details.")

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
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
