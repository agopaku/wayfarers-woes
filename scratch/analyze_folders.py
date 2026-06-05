import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
APPROVED_JSON = os.path.join(BASE_DIR, "scratch/approved_import.json")
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
FOUND_JSON = os.path.join(BASE_DIR, "scratch/found_scan_results.json")

# Load approved IDs
approved_ids = []
if os.path.exists(APPROVED_JSON):
    with open(APPROVED_JSON, "r") as f:
        approved_ids = [x["cand_id"] for x in json.load(f)]

# Load curated candidates
curated = []
if os.path.exists(CURATED_JSON):
    with open(CURATED_JSON, "r") as f:
        curated = json.load(f)
curated_dict = {x["cand_id"]: x for x in curated}

# Load found scan results
found = {}
if os.path.exists(FOUND_JSON):
    with open(FOUND_JSON, "r") as f:
        found = json.load(f)

print("--- APPROVED FILES FOLDERS ---")
approved_folders = {}
for cid in approved_ids:
    if cid in curated_dict:
        c = curated_dict[cid]
        folder = c["folder"]
        approved_folders[folder] = approved_folders.get(folder, 0) + 1

for folder, count in sorted(approved_folders.items()):
    print(f"  {folder}: {count} files")

print("\n--- FOUND FILES ON HD ---")
found_folders = {}
for name, path in found.items():
    # Extract folder from path (e.g. /Volumes/Pictures/Pictures/2025/2025-05-29/ag-edits/file.jpg)
    parts = path.split("/")
    if len(parts) >= 3:
        folder = parts[-3]  # The folder name (e.g. 2025-05-29 or 2016-08-21 etc.)
        found_folders[folder] = found_folders.get(folder, 0) + 1

for folder, count in sorted(found_folders.items()):
    print(f"  {folder}: {count} files")
