import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

missing_cache = []
for c in candidates:
    cached_path = c.get("cached_path")
    if not cached_path:
        missing_cache.append((c["cand_id"], c["filename"], "No cached_path key"))
    elif not os.path.exists(cached_path):
        missing_cache.append((c["cand_id"], c["filename"], f"File not found at {cached_path}"))

print(f"Total candidates checked: {len(candidates)}")
print(f"Candidates missing local cache: {len(missing_cache)}")

if missing_cache:
    print("\n--- Missing Cache list ---")
    for cid, name, reason in missing_cache[:20]:
        print(f"  {cid} ({name}): {reason}")
else:
    print("\n✓ All candidate original files are fully cached locally!")
