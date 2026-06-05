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
    if cid == "CAND_148":
        cand["location"] = "Chihuly Garden and Glass, Seattle, Washington, USA"
        cand["title"] = "Glasshouse at Chihuly Garden"
        cand["description"] = "Remya standing beneath the vibrant, 100-foot-long glass flower sculpture suspended inside the Glasshouse at Chihuly Garden and Glass in Seattle."
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_148 details.")
    elif cid == "CAND_149":
        cand["location"] = "Chihuly Garden and Glass, Seattle, Washington, USA"
        cand["title"] = "Space Needle Reflection in Glass Float"
        cand["description"] = "A stunning reflection of the adjacent Seattle Space Needle captured in a large, blue glass sphere in the exhibition gardens at Chihuly Garden and Glass."
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_149 details.")

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
