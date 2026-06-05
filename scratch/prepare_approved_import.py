import json
import os

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
APPROVED_IMPORT_JSON = os.path.join(BASE_DIR, "scratch/approved_import.json")

def main():
    with open(CURATED_JSON, "r") as f:
        candidates = json.load(f)
        
    approved_list = []
    for cand in candidates:
        if cand.get("status") == "approve":
            # Prefer 'story' for the description, fall back to 'description'
            desc = cand.get("story", "").strip() or cand.get("description", "").strip()
            
            approved_list.append({
                "cand_id": cand["cand_id"],
                "title": cand.get("title", ""),
                "description": desc,
                "location": cand.get("location", ""),
                "category": cand.get("category", "")
            })
            
    with open(APPROVED_IMPORT_JSON, "w") as f:
        json.dump(approved_list, f, indent=2)
        
    print(f"Wrote {len(approved_list)} entries to {APPROVED_IMPORT_JSON}")

if __name__ == "__main__":
    main()
