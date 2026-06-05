import json
import os
import subprocess

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
EXCLUDED_JSON = os.path.join(BASE_DIR, "scratch/excluded_filenames.json")
GALLERY_JSON = os.path.join(BASE_DIR, "gallery.json")

UNAPPROVED = [
    'DSC_8316.jpg', 'DSC_8303.jpg', 'DSC_8983.jpg', 'DSC_8977.jpg', 'DSC_9305.jpg',
    'DSC_0679.jpg', 'DSC_0700.jpg', 'DSC_0695.jpg', 'DSC_2142.jpg', 'DSC_2947.JPG',
    'DSC_2948.jpg', 'DSC_5885.jpg', 'DSC_1890.jpg', 'DSC_3561.jpg', 'DSC_3661.jpg',
    'DSC_4685.jpg', 'DSC_4671.jpg', 'DSC_8766.jpg', 'DSC01928.jpeg', 'DSC02896.jpeg',
    'DSC01045-Enhanced-NR.jpg', 'DSC01032-Enhanced-NR-2.jpg', 'DSC08855.jpg'
]

def main():
    unapproved_lower = {x.lower() for x in UNAPPROVED}
    
    # 1. Update curated_candidates.json
    if os.path.exists(CURATED_JSON):
        with open(CURATED_JSON, "r") as f:
            candidates = json.load(f)
        for cand in candidates:
            if cand["filename"].lower() in unapproved_lower:
                cand["status"] = "reject"
                print(f"Rejected candidate {cand['cand_id']} ({cand['filename']})")
        with open(CURATED_JSON, "w") as f:
            json.dump(candidates, f, indent=2)

    # 2. Update excluded_filenames.json
    if os.path.exists(EXCLUDED_JSON):
        with open(EXCLUDED_JSON, "r") as f:
            excluded = set(json.load(f))
        for item in UNAPPROVED:
            excluded.add(item.lower())
        with open(EXCLUDED_JSON, "w") as f:
            json.dump(list(sorted(excluded)), f, indent=2)
        print(f"Added {len(UNAPPROVED)} files to excluded_filenames.json")

    # 3. Update gallery.json
    if os.path.exists(GALLERY_JSON):
        with open(GALLERY_JSON, "r") as f:
            gallery = json.load(f)
        initial_len = len(gallery)
        gallery = [entry for entry in gallery if os.path.basename(entry["filename"]).lower() not in unapproved_lower]
        with open(GALLERY_JSON, "w") as f:
            json.dump(gallery, f, indent=2)
        print(f"Removed {initial_len - len(gallery)} entries from gallery.json. New size: {len(gallery)}")

    # 4. Delete physical files from images/ag-edits and images/ag-edits-thumbnails
    deleted_originals = 0
    deleted_thumbs = 0
    for filename in UNAPPROVED:
        orig_path = os.path.join(BASE_DIR, "images/ag-edits", filename)
        # Handle case variations on case-insensitive filesystem if needed, but direct match first
        if os.path.exists(orig_path):
            os.remove(orig_path)
            deleted_originals += 1
            
        thumb_path = os.path.join(BASE_DIR, "images/ag-edits-thumbnails", filename)
        if os.path.exists(thumb_path):
            os.remove(thumb_path)
            deleted_thumbs += 1
            
    print(f"Deleted {deleted_originals} original images and {deleted_thumbs} thumbnails physically.")

    # 5. Regenerate review sheet
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)

if __name__ == "__main__":
    main()
