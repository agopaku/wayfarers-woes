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
    if cid == "CAND_122":
        cand["title"] = "Golden Gate Bridge at Sunset"
        cand["location"] = "Golden Gate Bridge, San Francisco, California, USA"
        cand["description"] = "A breathtaking view of the Golden Gate Bridge at sunset, with a crescent moon appearing in the purple sky over the bay."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_122 details.")
    elif cid == "CAND_123":
        cand["title"] = "Sunset Over Golden Gate and Skyline"
        cand["location"] = "Golden Gate Bridge, San Francisco, California, USA"
        cand["description"] = "The sun setting behind the hills, casting a warm glow over the Golden Gate Bridge and the San Francisco skyline in the distance."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_123 details.")

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
