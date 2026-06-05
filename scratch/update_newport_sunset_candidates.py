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
    if cid == "CAND_204":
        cand["title"] = "Sunset at Brenton Point"
        cand["location"] = "Brenton Point State Park, Newport, Rhode Island, USA"
        cand["description"] = "A beautiful sunset view looking out over the ocean with our Tesla parked at Brenton Point State Park along Ocean Drive in Newport, Rhode Island."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_204 details.")
    elif cid == "CAND_205":
        cand["title"] = "Tesla Sunset at Brenton Point"
        cand["location"] = "Brenton Point State Park, Newport, Rhode Island, USA"
        cand["description"] = "A straight-on view of our Tesla parked against a vibrant orange winter sunset at Brenton Point State Park in Newport, Rhode Island."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_205 details.")

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
    print(f"Error: Could not find CAND_204 or CAND_205. Updated count: {updated_count}")
