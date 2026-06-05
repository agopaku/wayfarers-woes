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
    if cid == "CAND_062":
        cand["title"] = "Strolling around Lake Geneva"
        cand["location"] = "Lake Geneva, Wisconsin, USA"
        cand["description"] = "Enjoying a tranquil late winter getaway to the beautiful shoreline of Lake Geneva, a historic resort town in Wisconsin."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_062 details.")
    elif cid == "CAND_063":
        cand["title"] = "Scenic Views of Lake Geneva"
        cand["location"] = "Lake Geneva, Wisconsin, USA"
        cand["description"] = "Capturing the peaceful and quiet landscapes of Lake Geneva during a crisp, scenic late winter stroll."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_063 details.")

if updated_count == 2:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print("Successfully wrote updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find both candidates. Updated count: {updated_count}")
