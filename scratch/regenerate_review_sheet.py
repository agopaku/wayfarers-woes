import os
import json
import re

# Paths
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
CURATED_JSON_PATH = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
EXCLUDED_JSON_PATH = os.path.join(BASE_DIR, "scratch/excluded_filenames.json")
APP_DATA_DIR = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596"
REVIEW_MD_PATH = os.path.join(BASE_DIR, "candidate_gallery.md")

def regenerate_sheet():
    # 1. Load imported filenames from gallery.json
    imported_basenames = set()
    if os.path.exists(GALLERY_JSON_PATH):
        with open(GALLERY_JSON_PATH, "r") as f:
            gallery = json.load(f)
        for item in gallery:
            base = os.path.basename(item.get("filename", "")).lower()
            if base:
                imported_basenames.add(base)
                
    # 2. Load persistent excluded filenames
    excluded_filenames = set()
    if os.path.exists(EXCLUDED_JSON_PATH):
        with open(EXCLUDED_JSON_PATH, "r") as f:
            excluded_filenames = set(json.load(f))
            
    # 3. Load curated candidates mapping to find candidate details
    if not os.path.exists(CURATED_JSON_PATH):
        print(f"Error: {CURATED_JSON_PATH} not found.")
        return
        
    with open(CURATED_JSON_PATH, "r") as f:
        candidates = json.load(f)
    candidates_by_id = {x["cand_id"]: x for x in candidates}
                
    # 4. Parse existing candidate_gallery.md for any new rejections/approvals
    newly_excluded_ids = set()
    newly_approved_ids = set()
    
    if os.path.exists(REVIEW_MD_PATH):
        with open(REVIEW_MD_PATH, "r") as f:
            content = f.read()
        blocks = content.split("---")
        for block in blocks:
            match_id = re.search(r"### ID: \*\*(CAND_\d+)\*\*", block)
            if match_id:
                cand_id = match_id.group(1)
                # Check if user marked Exclude check box
                if re.search(r"-\s*\[[xX]\]\s*.*?\*\*Exclude", block) or "🔴" in block or "Don't add" in block or "don't add" in block:
                    newly_excluded_ids.add(cand_id)
                # Check if user marked Approve check box
                elif re.search(r"-\s*\[[xX]\]\s*.*?\*\*Approve", block):
                    newly_approved_ids.add(cand_id)
                    
    # Save newly excluded candidates to our persistent list
    for cid in newly_excluded_ids:
        if cid in candidates_by_id:
            filename = candidates_by_id[cid]["filename"].lower()
            excluded_filenames.add(filename)
            print(f"Adding newly excluded file to persistent list: {filename}")
            
    # Update excluded filenames JSON
    with open(EXCLUDED_JSON_PATH, "w") as f:
        json.dump(list(sorted(excluded_filenames)), f, indent=2)
        
    # 5. Filter remaining active candidates (not imported, not excluded)
    active_candidates = []
    for c in candidates:
        base = c["filename"].lower()
        cand_id = c["cand_id"]
        if base in imported_basenames:
            continue
        if base in excluded_filenames:
            continue
        active_candidates.append(c)
        
    # 6. Generate markdown lines
    markdown_lines = [
        "# Active Photo Review Sheet (Remaining Candidates)",
        "",
        f"We have updated the review sheet. There are **{len(active_candidates)} active candidates** remaining (already reviewed images have been hidden).",
        "",
        "## How to approve or reject",
        "You can now directly use the checkboxes below in your editor to approve or reject each image:",
        "- Check the `[x] ✅ Approve & Import` box to import the photo.",
        "- Check the `[x] ❌ Exclude (Don't Add)` box to exclude the photo.",
        "",
        "If you approve an image, you can still reply in the chat with its ID and a custom title/story. Otherwise, we will auto-generate details based on their folder and date.",
        "",
        "---",
        ""
    ]
    
    previews_dir = os.path.join(APP_DATA_DIR, "previews")
    
    for item in active_candidates:
        cand_id = item["cand_id"]
        src_path = item.get("cached_path") or item["file_path"]
        folder = item["folder"]
        filename = item["filename"]
        meta = item["metadata"]
        
        # Sibling preview file path
        preview_filename = f"{cand_id}_{filename}"
        preview_path = os.path.join(previews_dir, preview_filename)
        
        exif_parts = []
        if meta.get("camera"): exif_parts.append(f"Camera: {meta['camera']}")
        if meta.get("lens"): exif_parts.append(f"Lens: {meta['lens']}")
        if meta.get("aperture"): exif_parts.append(f"Aperture: {meta['aperture']}")
        if meta.get("shutter_speed"): exif_parts.append(f"Shutter: {meta['shutter_speed']}")
        if meta.get("iso"): exif_parts.append(f"ISO: {meta['iso']}")
        if meta.get("focal_length"): exif_parts.append(f"Focal: {meta['focal_length']}")
        exif_str = ", ".join(exif_parts) if exif_parts else "No EXIF details available"
        
        markdown_lines.append(f"### ID: **{cand_id}**")
        markdown_lines.append(f"- [ ] ✅ **Approve & Import**")
        markdown_lines.append(f"- [ ] ❌ **Exclude (Don't Add)**")
        markdown_lines.append(f"- **Original File**: `{filename}`")
        markdown_lines.append(f"- **Source Folder**: `{folder}`")
        markdown_lines.append(f"- **Date Taken**: `{meta.get('date_taken') or 'Unknown'}`")
        markdown_lines.append(f"- **EXIF**: {exif_str}")
        markdown_lines.append(f"- **Generated Title**: *{item.get('title') or ''}*")
        markdown_lines.append(f"- **Generated Location**: *{item.get('location') or ''}*")
        markdown_lines.append(f"- **Generated Story/Caption**: {item.get('description') or ''}")
        markdown_lines.append(f"- **Category**: `{item.get('category') or 'landscape'}`")
        markdown_lines.append(f"- **Cached Path**: `{src_path}`")
        markdown_lines.append("")
        markdown_lines.append(f"![{cand_id} Preview](file://{preview_path})")
        markdown_lines.append("")
        markdown_lines.append("---")
        markdown_lines.append("")
        
    with open(REVIEW_MD_PATH, "w") as f:
        f.write("\n".join(markdown_lines))
        
    print(f"Successfully regenerated review sheet!")
    print(f"Total candidates: {len(candidates)}")
    print(f"Imported: {len(imported_basenames)}")
    print(f"Excluded: {len(excluded_filenames)}")
    print(f"Remaining active: {len(active_candidates)}")
    print(f"Updated review sheet written to {REVIEW_MD_PATH}")
    
    if newly_approved_ids:
         print(f"User approved the following IDs inside the document: {list(newly_approved_ids)}")

if __name__ == "__main__":
    regenerate_sheet()
