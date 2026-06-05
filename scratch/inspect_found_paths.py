import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
FOUND_JSON = os.path.join(BASE_DIR, "scratch/found_scan_results.json")

if not os.path.exists(FOUND_JSON):
    print("found_scan_results.json not found")
    exit(1)

with open(FOUND_JSON, "r") as f:
    found = json.load(f)

print(f"Total found files: {len(found)}")
# Group by parent folder hierarchy
by_parent = {}
for name, path in found.items():
    parent = os.path.dirname(path)
    by_parent[parent] = by_parent.get(parent, 0) + 1

print("\n--- Files by Parent Directory ---")
for parent, count in sorted(by_parent.items(), key=lambda x: -x[1]):
    print(f"  {parent}: {count} files")

# Print first 20 files and their full path
print("\n--- Sample of 20 Mappings ---")
for idx, (name, path) in enumerate(list(found.items())[:20]):
    print(f"  {name} -> {path}")
