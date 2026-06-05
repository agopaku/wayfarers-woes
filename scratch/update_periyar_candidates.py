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
    if cid == "CAND_055":
        cand["title"] = "Trekking in Periyar National Park"
        cand["location"] = "Periyar National Park, Thekkady, Kumily, Kerala, India"
        cand["description"] = "Trekking through the lush, dense evergreen forests and moist deciduous woodlands of the Periyar Tiger Reserve."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print(f"Updated CAND_055 details.")
    elif cid == "CAND_056":
        cand["title"] = "Periyar Wilderness Exploration"
        cand["location"] = "Periyar National Park, Thekkady, Kumily, Kerala, India"
        cand["description"] = "Exploring the rich biodiversity and rugged forest trails of the Western Ghats during our wilderness trek in Thekkady."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print(f"Updated CAND_056 details.")

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
