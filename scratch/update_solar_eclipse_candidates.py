import os
import json
import subprocess

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

if not os.path.exists(CURATED_JSON):
    print(f"ERROR: {CURATED_JSON} not found!")
    exit(1)

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

updates = {
    "CAND_167": {
        "title": "Total Solar Eclipse — First Contact",
        "description": (
            "The moon begins its journey across the sun — an early partial phase of the total solar eclipse on April 8, 2024, "
            "captured from Findlay, Ohio. Shot through a solar filter at 300mm, the sun's disk shows just a subtle lunar bite "
            "as totality was still over an hour away. Findlay was within the path of totality, experiencing 100% coverage."
        ),
        "location": "Findlay, Ohio, USA",
        "category": "landscape",
        "status": "approve",
    },
    "CAND_168": {
        "title": "Total Solar Eclipse — Deep Partial Phase",
        "description": (
            "The moon carves a deep crescent into the sun during the partial phase of the total solar eclipse on April 8, 2024, "
            "shot from Findlay, Ohio. At 300mm and f/32, the dramatic golden corona glows around the moon's silhouette as "
            "totality approaches. Findlay lay in the heart of the path of totality."
        ),
        "location": "Findlay, Ohio, USA",
        "category": "landscape",
        "status": "approve",
    },
}

updated_ids = []
for candidate in candidates:
    cand_id = candidate.get("cand_id")
    if cand_id in updates:
        for key, value in updates[cand_id].items():
            candidate[key] = value
        updated_ids.append(cand_id)
        print(f"Updated {cand_id}: {candidate['title']}")

if not updated_ids:
    print("No candidates were updated. Check candidate IDs.")
else:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"\nSaved updates for: {', '.join(updated_ids)}")

    # Regenerate the review sheet
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    if os.path.exists(regen_script):
        print("\nRegenerating review sheet...")
        result = subprocess.run(["python3", regen_script], capture_output=True, text=True, cwd=BASE_DIR)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    else:
        print(f"Regen script not found: {regen_script}")
