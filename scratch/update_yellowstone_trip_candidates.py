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
    if cid == "CAND_195":
        cand["title"] = "Prairie Dog at Roadside Stop"
        cand["location"] = "Cactus Flat, South Dakota, USA"
        cand["description"] = "A detailed close-up shot of a black-tailed prairie dog standing alert in the grass near a highway gas stop on the way to Yellowstone."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_195 details.")
    elif cid == "CAND_196":
        cand["title"] = "Curious Prairie Dog"
        cand["location"] = "Cactus Flat, South Dakota, USA"
        cand["description"] = "Another close-up of a curious prairie dog holding a piece of grass, photographed at a roadside stop on the way to Yellowstone."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_196 details.")
    elif cid == "CAND_197":
        cand["title"] = "Bull Elk at Mammoth Hot Springs"
        cand["location"] = "Mammoth Hot Springs, Yellowstone National Park, Wyoming, USA"
        cand["description"] = "A majestic bull elk with large antlers resting on the mineral-rich geothermal ground near Mammoth Hot Springs in Yellowstone."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_197 details.")
    elif cid == "CAND_198":
        cand["title"] = "Coyote in the Valley"
        cand["location"] = "Yellowstone National Park, Wyoming, USA"
        cand["description"] = "A wild coyote standing alert amidst the dry autumn grasses of a valley in Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_198 details.")
    elif cid == "CAND_199":
        cand["title"] = "Steaming Geothermal Pool"
        cand["location"] = "Yellowstone National Park, Wyoming, USA"
        cand["description"] = "A beautiful long-exposure capture of a steaming geothermal spring with vibrant mineral colors in Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_199 details.")
    elif cid == "CAND_200":
        cand["title"] = "Yellowstone Geothermal Features"
        cand["location"] = "Yellowstone National Park, Wyoming, USA"
        cand["description"] = "Steaming pools and thermal vents rising from the colorful caldera landscape of Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_200 details.")
    elif cid == "CAND_201":
        cand["title"] = "Mammoth Hot Springs Terraces"
        cand["location"] = "Mammoth Hot Springs, Yellowstone National Park, Wyoming, USA"
        cand["description"] = "Steaming terraces formed by geothermal activity at Mammoth Hot Springs in Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_201 details.")
    elif cid == "CAND_202":
        cand["title"] = "Yellowstone Thermal Springs"
        cand["location"] = "Yellowstone National Park, Wyoming, USA"
        cand["description"] = "Another scenic capture of steam rising from the geothermal features of Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_202 details.")
    elif cid == "CAND_203":
        cand["title"] = "Vibrant Hot Spring"
        cand["location"] = "Yellowstone National Park, Wyoming, USA"
        cand["description"] = "A long-exposure view of steam rising off a colorful hot spring, illustrating the volcanic activity under Yellowstone National Park."
        cand["category"] = "landscape"
        cand["status"] = "approve"
        updated_count += 1
        print("Updated CAND_203 details.")

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
    print(f"Error: Could not find any target candidates. Updated count: {updated_count}")
