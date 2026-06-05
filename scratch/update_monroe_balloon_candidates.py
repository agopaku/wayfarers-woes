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
    if cid == "CAND_084":
        cand["title"] = "Monroe Balloon Festival Launch"
        cand["location"] = "Monroe, Wisconsin, USA"
        cand["description"] = "Watching the colorful hot air balloons prepare for lift-off during our bike trip to the Monroe Balloon and Blues Festival near the Illinois-Wisconsin border."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_084 details.")
    elif cid == "CAND_085":
        cand["title"] = "Balloons over Monroe"
        cand["location"] = "Monroe, Wisconsin, USA"
        cand["description"] = "Capturing hot air balloons drifting gracefully over the green pastures and rolling hills of Monroe on our summer bike ride."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_085 details.")
    elif cid == "CAND_289":
        cand["title"] = "Midwest Hot Air Balloon Rally"
        cand["location"] = "Monroe, Wisconsin, USA"
        cand["description"] = "A spectacular array of vibrant hot air balloons inflating and taking flight into the clear morning skies over Monroe."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_289 details.")
    elif cid == "CAND_329":
        cand["title"] = "Monroe Balloon Festival"
        cand["location"] = "Monroe, Wisconsin, USA"
        cand["description"] = "Colorful hot air balloons filling the skies over the green countryside of Monroe near the Wisconsin-Illinois border."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_329 details.")
    elif cid == "CAND_330":
        cand["title"] = "Preparing for Lift-off in Monroe"
        cand["location"] = "Monroe, Wisconsin, USA"
        cand["description"] = "Admiring the giant balloons inflating with hot air, glowing under the summer sun before rising over the fairgrounds in Monroe."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_330 details.")

if updated_count >= 1:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Successfully wrote {updated_count} updates to curated_candidates.json.")
    
    # Run sheet regeneration
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print(f"Error: Could not find candidates. Updated count: {updated_count}")
