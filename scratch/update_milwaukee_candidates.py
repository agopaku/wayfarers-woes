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
    if cid == "CAND_064":
        cand["title"] = "Harley-Davidson Museum Visit"
        cand["location"] = "Harley-Davidson Museum, Milwaukee, Wisconsin, USA"
        cand["description"] = "Visiting the famous Harley-Davidson Museum in Milwaukee, exploring the history, engineering, and culture of these iconic American motorcycles."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_064 details.")
    elif cid == "CAND_065":
        cand["title"] = "Milwaukee & Motorcycle Heritage"
        cand["location"] = "Harley-Davidson Museum, Milwaukee, Wisconsin, USA"
        cand["description"] = "Admiring the classic designs, historic vintage bikes, and interactive exhibits at the Harley-Davidson Museum."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_065 details.")

if updated_count == 2:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print("Successfully wrote updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find both candidates. Updated count: {updated_count}")
