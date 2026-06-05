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
    if cid == "CAND_208":
        cand["title"] = "Winter at Franconia Notch State Park"
        cand["location"] = "Franconia Notch State Park, New Hampshire, USA"
        cand["description"] = "A beautiful winter scene showing a snow-covered bridge surrounded by frosted trees in Franconia Notch State Park, New Hampshire."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_208 details.")
    elif cid == "CAND_209":
        cand["title"] = "Cannon Mountain Ski Slopes"
        cand["location"] = "Franconia Notch State Park, New Hampshire, USA"
        cand["description"] = "A view of the ski slopes and chairlifts on Cannon Mountain in Franconia Notch State Park on a clear, sunny winter day."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_209 details.")

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
    print(f"Error: Could not find CAND_208 or CAND_209. Updated count: {updated_count}")
