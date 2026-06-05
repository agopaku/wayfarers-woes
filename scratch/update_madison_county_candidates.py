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
    if cid == "CAND_134":
        cand["title"] = "Roseman Covered Bridge"
        cand["location"] = "Roseman Covered Bridge, Winterset, Iowa, USA"
        cand["description"] = "The historic Roseman Covered Bridge, built in 1883 and famous as a key location in the novel and movie 'The Bridges of Madison County'."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_134 details.")
    elif cid == "CAND_135":
        cand["title"] = "Pratheesh at Roseman Bridge"
        cand["location"] = "Roseman Covered Bridge, Winterset, Iowa, USA"
        cand["description"] = "A portrait of Pratheesh at the historic Roseman Covered Bridge during our road trip through Madison County."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_135 details.")
    elif cid == "CAND_136":
        cand["title"] = "High Trestle Trail Bridge"
        cand["location"] = "High Trestle Trail Bridge, Madrid, Iowa, USA"
        cand["description"] = "Standing on the iconic High Trestle Trail Bridge over the Des Moines River valley during our Iowa road trip."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_136 details.")

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
