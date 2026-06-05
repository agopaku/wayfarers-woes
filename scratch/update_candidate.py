import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

updated = False
for cand in candidates:
    if cand["cand_id"] == "CAND_024":
        cand["title"] = "Breakfast with a View in Chitkul"
        cand["location"] = "Chitkul, Kinnaur, Himachal Pradesh, India"
        cand["description"] = "Having breakfast with a view from the terrace of one of the homestays in Chitkul, the last inhabited village near the Indo-Tibet border."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated = True
        print(f"Updated CAND_024: {cand['title']}")
        break

if updated:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print("CAND_024 not found in curated_candidates.json")
