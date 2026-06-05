import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

for cand in candidates:
    if cand["folder"] == "2017-09-03":
        print(f"ID: {cand['cand_id']}, File: {cand['filename']}, Folder: {cand['folder']}, Title: {cand.get('title')}, Status: {cand.get('status')}")
