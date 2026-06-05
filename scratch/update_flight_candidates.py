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
    if cid == "CAND_059":
        cand["title"] = "Window Seat Views above the Clouds"
        cand["location"] = "In-flight, Chennai to Chicago"
        cand["description"] = "A dramatic aerial view of the cloud deck and skies, captured from the window seat of the aircraft somewhere on the long-haul flight from Chennai to Chicago."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_059 details.")

if updated_count == 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print("Successfully wrote updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find CAND_059. Updated count: {updated_count}")
