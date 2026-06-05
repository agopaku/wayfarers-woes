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
    
    # 2018-01-14 Highway 1 Trip Candidates
    if cid == "CAND_124":
        cand["title"] = "Wild Mustard Fields on Highway 1"
        cand["location"] = "Highway 1, California, USA"
        cand["description"] = "A vibrant field of yellow wild mustard flowers blooming along the Pacific Coast Highway under a clear blue sky."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_124 details.")
    elif cid == "CAND_125":
        cand["title"] = "Presidio National Cemetery"
        cand["location"] = "San Francisco National Cemetery, San Francisco, California, USA"
        cand["description"] = "Standing before the rows of white headstones at the historic military cemetery in the Presidio before starting our road trip."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_125 details.")
    elif cid == "CAND_369":
        cand["title"] = "Panther Beach Sea Arch"
        cand["location"] = "Panther Beach, Santa Cruz, California, USA"
        cand["description"] = "Waves washing onto the sandy shore of Panther Beach, featuring the famous natural rock sea arch."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_369 details.")
    elif cid == "CAND_370":
        cand["title"] = "Davenport Rocky Shoreline"
        cand["location"] = "Davenport, California, USA"
        cand["description"] = "Ocean waves crashing over tide pools and rocky shelf along the rugged Central California coast."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_370 details.")
    elif cid == "CAND_371":
        cand["title"] = "Big Sur Rugged Coastline"
        cand["location"] = "Big Sur, California, USA"
        cand["description"] = "A sweeping panoramic view of the dramatic Big Sur cliffs, rocky coves, and cypress trees lining the Pacific coast."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_371 details.")
        
    # 2020-12-20 Naperville / Blackwell Forest Candidates
    elif cid == "CAND_126":
        cand["title"] = "Cozy Evening at Home"
        cand["location"] = "Naperville, Illinois, USA"
        cand["description"] = "A warm and quiet evening at home in Naperville, with Christmas lights hanging over the blinds and a movie on TV."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_126 details.")
    elif cid == "CAND_127":
        cand["title"] = "Winter Walk at Blackwell Forest"
        cand["location"] = "Blackwell Forest Preserve, Warrenville, Illinois, USA"
        cand["description"] = "A bright winter walk in the meadows of Blackwell Forest Preserve, enjoying the fresh air and golden hour light."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_127 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
