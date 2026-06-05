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
    if cid == "CAND_109":
        cand["title"] = "Autumn Colors on US-131"
        cand["location"] = "US-131, Michigan, USA"
        cand["description"] = "Driving through a corridor of vibrant fall colors along Highway US-131 during an autumn road trip in Michigan."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_109 details.")
    elif cid == "CAND_108":
        cand["title"] = "Scenic Winding Route"
        cand["location"] = "US-131, Michigan, USA"
        cand["description"] = "A scenic, winding stretch of US-131 lined with gold and green trees under an overcast sky."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_108 details.")
    elif cid == "CAND_367":
        cand["title"] = "Jeep on Pierce Stocking Scenic Drive"
        cand["location"] = "Sleeping Bear Dunes National Lakeshore, Michigan, USA"
        cand["description"] = "Cruising the winding forest road of Pierce Stocking Scenic Drive in the Jeep Cherokee, surrounded by late-autumn foliage."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_367 details.")
    elif cid == "CAND_364":
        cand["title"] = "Lake Michigan Dune Overlook"
        cand["location"] = "Sleeping Bear Dunes National Lakeshore, Michigan, USA"
        cand["description"] = "Looking down the massive sand dune slope of the Lake Michigan Overlook on Pierce Stocking Scenic Drive, watching waves lap the beach below."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_364 details.")

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
