import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

target_ids = {f"CAND_{i:03d}" for i in range(125, 136)}

for cand in candidates:
    if cand["cand_id"] in target_ids:
        print(f"ID: {cand['cand_id']}")
        print(f"  File: {cand['filename']}")
        print(f"  Folder: {cand['folder']}")
        print(f"  Title: {cand.get('title')}")
        print(f"  Location: {cand.get('location')}")
        print(f"  Description: {cand.get('description')}")
        print(f"  Status: {cand.get('status')}")
        print("-" * 40)
