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
    if cid == "CAND_074":
        cand["title"] = "Devil's Lake State Park Hike"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Trekking along the scenic clifftop trails at Devil's Lake State Park in Wisconsin."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_074 details.")
    elif cid == "CAND_075":
        cand["title"] = "Devil's Lake Scenic Overlook"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Enjoying the breathtaking views of Devil's Lake from the towering quartzite cliffs."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_075 details.")
    elif cid == "CAND_225":
        cand["title"] = "Devil's Lake Quartzite Formations"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Standing atop the ancient, rugged quartzite rock formations that frame Devil's Lake."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_225 details.")
    elif cid == "CAND_228":
        cand["title"] = "Hiking the Talus Slopes"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "Navigating the challenging talus slopes and rocky pathways overlooking Devil's Lake."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_228 details.")
    elif cid == "CAND_240":
        cand["title"] = "Sunset over Devil's Lake"
        cand["location"] = "Devil's Lake State Park, Baraboo, Wisconsin, USA"
        cand["description"] = "The warm, golden light of sunset reflecting over the peaceful waters of Devil's Lake."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_240 details.")

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
