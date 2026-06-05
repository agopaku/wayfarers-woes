import os
import json
import subprocess

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print("curated_candidates.json not found")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

updated_count = 0
for cand in candidates:
    cid = cand["cand_id"]
    if cid == "CAND_187":
        cand["title"] = "Yosemite Valley Landscape"
        cand["location"] = "Yosemite National Park, California, USA"
        cand["description"] = "A detailed telephoto shot showcasing the massive granite cliff faces and forest details in Yosemite National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_187 details.")
    elif cid == "CAND_188":
        cand["title"] = "Yosemite Starry Night"
        cand["location"] = "Yosemite National Park, California, USA"
        cand["description"] = "A spectacular 30-second long-exposure night landscape capturing the starry sky over Yosemite National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_188 details.")
    elif cid == "CAND_189":
        cand["title"] = "Lake Tahoe Scenic View"
        cand["location"] = "Lake Tahoe, California, USA"
        cand["description"] = "A breathtaking view of the crystal clear waters and surrounding mountain peaks of Lake Tahoe."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_189 details.")
    elif cid == "CAND_190":
        cand["title"] = "Sailing on Lake Tahoe"
        cand["location"] = "Lake Tahoe, California, USA"
        cand["description"] = "A scenic shot overlooking the pristine waters of Lake Tahoe under a bright blue sky."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_190 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
    if res.stderr:
        print("Regenerate Sheet stderr:", res.stderr)
else:
    print(f"Error: Could not find target candidates. Updated count: {updated_count}")
