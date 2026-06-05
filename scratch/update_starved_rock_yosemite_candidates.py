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
    if cid == "CAND_177":
        cand["title"] = "Hiking Starved Rock State Park"
        cand["location"] = "Starved Rock State Park, Oglesby, Illinois, USA"
        cand["description"] = "A scenic view captured along the trails of Starved Rock State Park during a spring hike, showcasing the park's unique sandstone canyons."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_177 details.")
    elif cid == "CAND_182":
        cand["title"] = "Yosemite National Park"
        cand["location"] = "Yosemite National Park, California, USA"
        cand["description"] = "A breathtaking landscape view showcasing the majestic granite cliffs and pristine wilderness of Yosemite National Park in California."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_182 details.")
    elif cid == "CAND_183":
        cand["title"] = "Exploring Yosemite Valley"
        cand["location"] = "Yosemite National Park, California, USA"
        cand["description"] = "A beautiful scenic view of Yosemite Valley, surrounded by towering trees and massive granite rock formations."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_183 details.")

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
    print(f"Error: Could not find any target candidates. Updated count: {updated_count}")
