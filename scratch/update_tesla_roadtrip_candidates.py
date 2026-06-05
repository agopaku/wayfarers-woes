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
    
    # Oct 8, 2022: Badlands National Park
    if cid == "CAND_143":
        cand["title"] = "Sunset at Badlands"
        cand["location"] = "Badlands National Park, South Dakota, USA"
        cand["description"] = "The start of our epic Tesla road trip: looking out over the winding road and layered spires of Badlands National Park at dusk."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_144":
        cand["title"] = "Badlands Ridge Sunset"
        cand["location"] = "Badlands National Park, South Dakota, USA"
        cand["description"] = "The sun setting directly over the rugged, striated rock ridges of the Badlands, lighting up the sky in gold and orange."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        
    # Oct 9, 2022: Wyoming & Idaho
    elif cid == "CAND_145":
        cand["title"] = "Driving Towards the Rockies"
        cand["location"] = "Wyoming, USA"
        cand["description"] = "Driving our Tesla along the highway heading west towards the towering, snow-capped peaks of the Rocky Mountains in Wyoming."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_146":
        cand["title"] = "Welcome to Idaho"
        cand["location"] = "Idaho, USA"
        cand["description"] = "Passing the 'Welcome to Idaho' state line highway sign, surrounded by the steep, pine-covered slopes of the mountains."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        
    # Oct 10-11, 2022: Seattle / Olympic NP
    elif cid == "CAND_147":
        cand["title"] = "Hoh River Walk"
        cand["location"] = "Olympic National Park, Washington, USA"
        cand["description"] = "Walking along the rocky banks of the glacier-fed Hoh River, surrounded by the rainforest mountains of Olympic National Park."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_148":
        cand["title"] = "Remya at Chihuly Glass Garden"
        cand["location"] = "Chihuly Garden and Glass, Seattle, Washington, USA"
        cand["description"] = "Remya standing under the spectacular, yellow and orange hand-blown glass flower sculpture in the Seattle glass house."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_149":
        cand["title"] = "Space Needle in Glass"
        cand["location"] = "Chihuly Garden and Glass, Seattle, Washington, USA"
        cand["description"] = "A creative reflection of the Seattle Space Needle captured in a large, polished blue glass sphere in the Chihuly exhibition gardens."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        
    # Oct 12, 2022: Oregon Coast
    elif cid == "CAND_150":
        cand["title"] = "Cannon Beach Golden Sunset"
        cand["location"] = "Cannon Beach, Oregon Coast, Oregon, USA"
        cand["description"] = "A breathtaking golden hour view of the Oregon Coast at Cannon Beach, with the sun casting a warm glow over the wet sand and silhouettes."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_151":
        cand["title"] = "Sunset Stroll on the Coast"
        cand["location"] = "Cannon Beach, Oregon Coast, Oregon, USA"
        cand["description"] = "Walking along the shoreline of Cannon Beach as the sun sets directly over the Pacific Ocean, turning the sky a deep orange."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        
    # Oct 16-17, 2022: SF & Big Sur
    elif cid == "CAND_154":
        cand["title"] = "California Street Cable Car"
        cand["location"] = "San Francisco, California, USA"
        cand["description"] = "Looking down the steep hill of California Street in San Francisco, with a classic cable car climbing the tracks."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_155":
        cand["title"] = "Ocean Twilight Overlook"
        cand["location"] = "Highway 1, California, USA"
        cand["description"] = "Remya enjoying the peaceful ocean breeze from a clifftop bench during twilight, under a purple and pink sky."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_156":
        cand["title"] = "Tesla Model 3 in Big Sur"
        cand["location"] = "Big Sur, Highway 1, California, USA"
        cand["description"] = "Our red Tesla Model 3 parked on a scenic overlook along the winding coastal Highway 1 in Big Sur."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
    elif cid == "CAND_157":
        cand["title"] = "Looking Out Over Big Sur"
        cand["location"] = "Big Sur, Highway 1, California, USA"
        cand["description"] = "Standing on a high cliff overlooking the endless blue waters of the Pacific Ocean along the rugged coast of Big Sur."
        cand["category"] = "portrait"
        cand["status"] = "approve"
        updated_count += 1

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
