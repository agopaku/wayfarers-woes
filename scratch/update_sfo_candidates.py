import os
import json

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
    if cid == "CAND_086":
        cand["title"] = "San Francisco Skyline"
        cand["location"] = "San Francisco, California, USA"
        cand["description"] = "Capturing the iconic city layout and skyline of San Francisco during my mother's visit from India."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_086 details.")
    elif cid == "CAND_087":
        cand["title"] = "Mom's Visit to San Francisco"
        cand["location"] = "San Francisco, California, USA"
        cand["description"] = "A sweet portrait with my mother during her travel to San Francisco from India, exploring the city together."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_087 details.")
    elif cid == "CAND_088":
        cand["title"] = "Golden Gate Bridge Vista"
        cand["location"] = "Golden Gate Bridge, San Francisco, California, USA"
        cand["description"] = "A classic view of the Golden Gate Bridge stretching across the bay, showing it to my mother during her SFO trip."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_088 details.")
    elif cid == "CAND_089":
        cand["title"] = "Exploring the Bay Area"
        cand["location"] = "San Francisco, California, USA"
        cand["description"] = "Enjoying scenic views of the San Francisco Bay and coastal outlines on a beautiful summer day with my mother."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_089 details.")

if updated_count == 4:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print("Successfully wrote updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find all SFO candidates. Updated count: {updated_count}")
