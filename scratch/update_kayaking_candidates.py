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
    if cid == "CAND_081":
        cand["title"] = "Kayaking on Lake Superior"
        cand["location"] = "Lake Superior, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Launching our kayaks onto the crystal-clear, vast waters of Lake Superior at Pictured Rocks."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_081 details.")
    elif cid == "CAND_082":
        cand["title"] = "Pictured Rocks Kayak Expedition"
        cand["location"] = "Lake Superior, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Paddling along the base of the massive, colorful sandstone cliffs rising straight out of Lake Superior."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_082 details.")
    elif cid == "CAND_083":
        cand["title"] = "Navigating Sea Caves in Lake Superior"
        cand["location"] = "Lake Superior, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Steering our kayaks through the spectacular natural archways and sea caves carved into the Pictured Rocks cliffs."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_083 details.")
    elif cid == "CAND_286":
        cand["title"] = "Paddling under Sandstone Cliffs"
        cand["location"] = "Lake Superior, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Looking up at the towering, multi-colored mineral stains on the sandstone cliffs while kayaking on Lake Superior."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_286 details.")
    elif cid == "CAND_368":
        cand["title"] = "Resting in the Sea Caves"
        cand["location"] = "Lake Superior, Pictured Rocks National Lakeshore, Upper Peninsula, Michigan, USA"
        cand["description"] = "Taking a moment to marvel at the clear turquoise waters and carved rock ceilings of the sea caves."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_368 details.")

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
