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
    if cid == "CAND_076":
        cand["title"] = "Hiking the East Bluff Trail"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Climbing the steep stone stairs of the iconic East Bluff Trail, surrounded by towering trees and massive quartzite cliffs at Devil's Lake."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_076 details.")
    elif cid == "CAND_077":
        cand["title"] = "Devil's Lake East Bluff Vistas"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Enjoying the spectacular panoramic vistas of the lake and surrounding woodlands from the top of the East Bluff."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_077 details.")
    elif cid == "CAND_232":
        cand["title"] = "Exploring the Balanced Rock Path"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Hiking past ancient rock formations on the East Bluff, with views of the famous Balanced Rock and Devil's Doorway."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_232 details.")
    elif cid == "CAND_233":
        cand["title"] = "Devil's Lake East Bluff Woods"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Walking along the quieter, forested sections of the East Bluff Woods trail, surrounded by tall spring foliage."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_233 details.")

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
