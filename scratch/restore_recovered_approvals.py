import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
RECOVERED_JSON = os.path.join(BASE_DIR, "scratch/recovered_all_approvals.json")

if not os.path.exists(RECOVERED_JSON):
    print("recovered_all_approvals.json not found")
    exit(1)

with open(RECOVERED_JSON, "r") as f:
    recovered = json.load(f)

recovered_dict = {x["cand_id"]: x for x in recovered}

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    curated = json.load(f)

restored_count = 0
for cand in curated:
    cid = cand["cand_id"]
    if cid in recovered_dict:
        rec = recovered_dict[cid]
        # Overlay fields
        cand["title"] = rec["title"]
        cand["description"] = rec["description"]
        cand["location"] = rec["location"]
        if "category" in rec:
            cand["category"] = rec["category"]
        cand["status"] = "approve"
        print(f"Restored custom details for {cid}: {cand['title']}")
        restored_count += 1

with open(CURATED_JSON, "w") as f:
    json.dump(curated, f, indent=2)

print(f"\nSuccessfully restored {restored_count} custom approvals to curated_candidates.json")

# Run sheet regeneration
import subprocess
regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
print("Regenerate Sheet stdout:", res.stdout)
