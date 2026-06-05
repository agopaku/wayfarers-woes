import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

# Group by category / folder cluster to show a variety
groups = {}
for c in candidates:
    loc = c.get("location", "Unknown Location")
    cat = c.get("category", "landscape")
    folder = c.get("folder", "")
    
    # Simple cluster key
    if "Kinnaur" in loc or "Spiti" in loc:
        key = "Himalayan Expedition (Kinnaur / Spiti Valley)"
    elif "Duluth" in loc or "Superior" in loc:
        key = "Lake Superior / Duluth Winter Freeze"
    elif "Naperville" in loc:
        key = "Naperville Baby & Family Photoshoots"
    elif "Badlands" in loc:
        key = "South Dakota / Badlands"
    elif "Grand Teton" in loc:
        key = "Grand Teton & Yellowstone (Wyoming)"
    elif "Sedona" in loc or "Arizona" in loc:
        key = "Arizona Red Rocks"
    elif "Oregon" in loc:
        key = "Oregon Coastline"
    else:
        key = f"Other Trips ({loc})"
        
    if key not in groups:
        groups[key] = []
    groups[key].append(c)

for name, items in sorted(groups.items()):
    print(f"\n=========================================")
    print(f"🎬 {name} (Sample of {min(3, len(items))} from {len(items)} items)")
    print(f"=========================================")
    for item in items[:3]:
        print(f"ID: {item['cand_id']} | File: {item['filename']}")
        print(f"  Title      : {item.get('title')}")
        print(f"  Location   : {item.get('location')}")
        print(f"  Story      : {item.get('description')}")
        print(f"  Category   : {item.get('category')}")
        print()
