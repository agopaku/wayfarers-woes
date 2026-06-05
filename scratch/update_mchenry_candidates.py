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
    if cid == "CAND_106":
        cand["title"] = "Camping with the Jeep Cherokee"
        cand["location"] = "Chain O' Lakes State Park, McHenry County, Illinois, USA"
        cand["description"] = "Setting up camp next to my new Jeep Cherokee at Chain O' Lakes State Park, my first road and camping trip after purchasing the vehicle."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_106 details.")
    elif cid == "CAND_107":
        cand["title"] = "Kayaking on the Chain O' Lakes"
        cand["location"] = "Chain O' Lakes State Park, McHenry County, Illinois, USA"
        cand["description"] = "Kayaking along the shores of the Chain O' Lakes, enjoying a clear, sunny autumn afternoon on the water with residential cottages lining the shore."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_107 details.")
    elif cid == "CAND_349":
        cand["title"] = "Catching Football at Campground"
        cand["location"] = "Chain O' Lakes State Park, McHenry County, Illinois, USA"
        cand["description"] = "Playing catch with a football at our grassy campsite in Chain O' Lakes State Park during a weekend getaway."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_349 details.")

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
