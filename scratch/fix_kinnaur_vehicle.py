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
    folder = cand.get("folder", "").lower()
    # Mapped to Kinnaur/Spiti Valley 2016 trip
    is_kinnaur_spiti = "kinnaur" in folder or "spiti" in folder or (cand.get("date_taken") and cand.get("date_taken").startswith("2016-05"))
    
    if is_kinnaur_spiti:
        desc = cand.get("description", "")
        title = cand.get("title", "")
        
        # Replace motorcycle/Royal Enfield terms
        new_desc = desc
        new_desc = new_desc.replace("Royal Enfield motorbikes", "road expedition")
        new_desc = new_desc.replace("Royal Enfield", "taxi")
        new_desc = new_desc.replace("motorcycle journey", "road trip")
        new_desc = new_desc.replace("motorcycles parked", "taxi parked")
        new_desc = new_desc.replace("motorbikes", "taxi")
        new_desc = new_desc.replace("motorcycle", "taxi")
        
        new_title = title
        new_title = new_title.replace("Riding the Cliffhanger Routes", "Navigating the Cliffhanger Routes")
        new_title = new_title.replace("Riding", "Navigating")
        new_title = new_title.replace("riding", "navigating")
        
        if new_desc != desc or new_title != title:
            cand["description"] = new_desc
            cand["title"] = new_title
            print(f"Updated {cand['cand_id']} ({cand['filename']}):")
            print(f"  Title: {title} -> {new_title}")
            print(f"  Desc:  {desc} -> {new_desc}")
            updated_count += 1

if updated_count > 0:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"\nSuccessfully updated {updated_count} Kinnaur/Spiti candidates to reflect taxi travel.")
    
    # Run sheet regeneration to update candidate_gallery.md
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
else:
    print("No Kinnaur/Spiti candidate details needed updates.")
