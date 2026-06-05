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
    if cid == "CAND_216":
        cand["title"] = "Descending the Stone Stairs at Bell Smith Springs"
        cand["location"] = "Bell Smith Springs Recreation Area, Shawnee National Forest, Illinois, USA"
        cand["description"] = "A view of the historic Civilian Conservation Corps stone staircase leading down into the canyon at Bell Smith Springs Recreation Area."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_216 details.")
    elif cid == "CAND_217":
        cand["title"] = "White Trail Signboard"
        cand["location"] = "Bell Smith Springs Recreation Area, Shawnee National Forest, Illinois, USA"
        cand["description"] = "A wooden trail sign on the White Trail pointing left towards Spring and right towards Devil's Backbone rock formation in Bell Smith Springs."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_217 details.")

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
    print(f"Error: Could not find CAND_216 or CAND_217. Updated count: {updated_count}")
