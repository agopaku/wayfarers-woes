import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
FOUND_JSON = os.path.join(BASE_DIR, "scratch/found_scan_results.json")

# Load existing candidates
curated = []
if os.path.exists(CURATED_JSON):
    with open(CURATED_JSON, "r") as f:
        curated = json.load(f)

curated_filenames = {c["filename"].lower() for c in curated}

# Load found scan results
found = {}
if os.path.exists(FOUND_JSON):
    with open(FOUND_JSON, "r") as f:
        found = json.load(f)

overlap = []
new_files = []

for name, path in found.items():
    if name in curated_filenames:
        overlap.append((name, path))
    else:
        new_files.append((name, path))

print(f"Total found files on HD: {len(found)}")
print(f"Overlap with existing candidates in curated_candidates.json: {len(overlap)}")
print(f"New files to add as candidates: {len(new_files)}")

# Print some of the new files
print("\n--- Sample of 10 New Files ---")
for name, path in new_files[:10]:
    print(f"  {name} -> {path}")

# Print some of the overlap files
print("\n--- Sample of 10 Overlap Files ---")
for name, path in overlap[:10]:
    print(f"  {name} -> {path}")
