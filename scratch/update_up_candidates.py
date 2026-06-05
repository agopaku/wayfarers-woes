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
    if cid == "CAND_080":
        cand["title"] = "Mosquito Falls Trail"
        cand["location"] = "Mosquito Falls, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Trekking the peaceful Mosquito Falls trail in the Upper Peninsula. Shortly after this photo was taken, we came face to face with a wild black bear!"
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_080 details.")
    elif cid == "CAND_081":
        cand["title"] = "Pictured Rocks Wilderness Hike"
        cand["location"] = "Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Hiking through the deep forest trails of Pictured Rocks National Lakeshore on our way to Mosquito Falls."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_081 details.")
    elif cid == "CAND_236":
        cand["title"] = "Mosquito River Crossings"
        cand["location"] = "Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Crossing the rustic wooden bridges over the rushing Mosquito River along the wilderness loop trail."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_236 details.")
    elif cid == "CAND_237":
        cand["title"] = "Wilds of the Upper Peninsula"
        cand["location"] = "Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Surrounded by dense forest canopy and pristine wilderness while hiking the Pictured Rocks trails."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_237 details.")

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
