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
    if cid == "CAND_218":
        cand["title"] = "Grand Canyon Sunrise"
        cand["location"] = "Mather Point, Grand Canyon National Park, Arizona, USA"
        cand["description"] = "A stunning view of the sunrise lighting up the Grand Canyon, captured from Mather Point."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_218 details.")
    elif cid == "CAND_219":
        cand["title"] = "Anil Watching the Grand Canyon Sunrise"
        cand["location"] = "Mather Point, Grand Canyon National Park, Arizona, USA"
        cand["description"] = "Anil standing on a rock ledge, watching the spectacular golden sunrise over the Grand Canyon alongside fellow travelers at Mather Point."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_219 details.")
    elif cid == "CAND_220":
        cand["title"] = "Colorado River in the Grand Canyon"
        cand["location"] = "Grand Canyon National Park, Arizona, USA"
        cand["description"] = "A breathtaking wide-angle daylight landscape showing the Colorado River winding through the deep gorges of the Grand Canyon."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_220 details.")
    elif cid == "CAND_221":
        cand["title"] = "Mandalay Bay at Night"
        cand["location"] = "Las Vegas Strip, Nevada, USA"
        cand["description"] = "The iconic gold-tinted facade of the Mandalay Bay hotel and casino on the Las Vegas Strip, with its powerful sky beam lit up at night."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_221 details.")
    elif cid == "CAND_222":
        cand["title"] = "Planet Hollywood and Paris Las Vegas"
        cand["location"] = "Las Vegas Strip, Nevada, USA"
        cand["description"] = "A vibrant night shot on the Las Vegas Strip featuring the Planet Hollywood sign and the illuminated replica of the Eiffel Tower in the background."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_222 details.")
    elif cid == "CAND_223":
        cand["title"] = "Bellagio Fountains at Night"
        cand["location"] = "Las Vegas Strip, Nevada, USA"
        cand["description"] = "A spectacular capture of the Bellagio Fountains water show in full action against the backdrop of the illuminated Bellagio Hotel at night."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_223 details.")

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
