import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
APPROVED_JSON = os.path.join(BASE_DIR, "scratch/approved_import.json")
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(APPROVED_JSON):
    print("approved_import.json not found")
    exit(1)

with open(APPROVED_JSON, "r") as f:
    approved = json.load(f)

approved_ids = {item["cand_id"] for item in approved}
print(f"Total approved IDs in approved_import.json: {len(approved_ids)}")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

candidates_dict = {item["cand_id"]: item for item in candidates}

count = 0
for cid in sorted(approved_ids):
    if cid in candidates_dict:
        c = candidates_dict[cid]
        print(f"\nID: {cid}")
        print(f"  Filename: {c.get('filename')}")
        print(f"  Folder: {c.get('folder')}")
        print(f"  Date Taken: {c.get('date_taken')}")
        print(f"  File Path: {c.get('file_path')}")
        print(f"  EXIF: {c.get('metadata')}")
        count += 1
    else:
        print(f"\nID: {cid} (NOT FOUND IN curated_candidates.json)")

print(f"\nMatched {count} of {len(approved_ids)} approved candidates.")
