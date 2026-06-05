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
    if cid == "CAND_212":
        cand["title"] = "Bug Light Lighthouse"
        cand["location"] = "Bug Light, South Portland, Maine, USA"
        cand["description"] = "A close-up view of the historic Portland Breakwater Light (commonly known as Bug Light) decorated with a festive Christmas wreath in South Portland, Maine."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_212 details.")
    elif cid == "CAND_213":
        cand["title"] = "Portland Breakwater Light (Bug Light)"
        cand["location"] = "Bug Light, South Portland, Maine, USA"
        cand["description"] = "A wider scenic view of Bug Light standing at the end of the breakwater in South Portland, Maine, looking out towards the harbor."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_213 details.")

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
    print(f"Error: Could not find CAND_212 or CAND_213. Updated count: {updated_count}")
