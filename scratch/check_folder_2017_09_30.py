import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

for cand in candidates:
    if cand["folder"] == "2017-09-30":
        print(f"ID: {cand['cand_id']}")
        print(f"  File: {cand['filename']}")
        print(f"  Title: {cand.get('title')}")
        print(f"  Location: {cand.get('location')}")
        print(f"  Description: {cand.get('description')}")
        print(f"  Status: {cand.get('status')}")
        print("-" * 40)
