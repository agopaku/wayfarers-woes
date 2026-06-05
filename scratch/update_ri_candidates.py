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
    if cid == "CAND_072":
        cand["title"] = "Rhode Island Coastal Views"
        cand["location"] = "Rhode Island, USA"
        cand["description"] = "Capturing the scenic beauty and quiet charm of the Rhode Island coastline on a spring afternoon."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_072 details.")
    elif cid == "CAND_073":
        cand["title"] = "Newport Coastline Walk"
        cand["location"] = "Newport, Rhode Island, USA"
        cand["description"] = "Walking along the cliffside paths and ocean views in Newport, enjoying the crisp ocean breeze of Rhode Island."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_073 details.")
    elif cid == "CAND_323":
        cand["title"] = "Rhode Island Ocean Horizons"
        cand["location"] = "Rhode Island, USA"
        cand["description"] = "A peaceful perspective of the vast Atlantic Ocean stretching out from the rocky shores of Rhode Island."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_323 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
