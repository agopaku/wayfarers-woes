import json
import os

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

def main():
    with open(CURATED_JSON, "r") as f:
        candidates = json.load(f)
        
    updated = 0
    for cand in candidates:
        cid = cand["cand_id"]
        
        # Goa
        if cid == "CAND_253":
            cand["title"] = "Portrait of Shweta in Goa"
            updated += 1
        # Naperville Christmas
        elif cid == "CAND_257":
            cand["title"] = "Evie's Christmas Celebration"
            updated += 1
        # Willis Tower
        elif cid == "CAND_320":
            cand["title"] = "Chicago Sunset from Willis Tower"
            updated += 1
        # Navy Pier
        elif cid in ["CAND_321", "CAND_322", "CAND_341", "CAND_342", "CAND_343"]:
            if "Sub-Zero" in cand.get("title", ""):
                cand["title"] = "Navy Pier, Chicago"
                updated += 1
        # Mount Rushmore
        elif cid == "CAND_325":
            cand["title"] = "Mount Rushmore in the Mist"
            updated += 1
        # Naperville Winter Storm
        elif cid in ["CAND_345", "CAND_346"]:
            if "Sub-Zero" in cand.get("title", ""):
                cand["title"] = "Evie during Naperville Winter Storm"
                updated += 1
        # Baby photoshoots CAND_379 to CAND_393 (not Evie)
        elif 379 <= int(cid.split("_")[1]) <= 393:
            title = cand.get("title", "")
            if "Evie" in title:
                cand["title"] = title.replace("Evie's", "Baby").replace("Evie", "Baby")
                updated += 1
                
    if updated > 0:
        with open(CURATED_JSON, "w") as f:
            json.dump(candidates, f, indent=2)
        print(f"Successfully fixed titles for {updated} candidates in curated_candidates.json")
    else:
        print("No candidates needed title fixing.")

if __name__ == "__main__":
    main()
