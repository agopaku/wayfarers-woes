import os
import json
from PIL import Image

# Paths
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
INDEXed_JSON = os.path.join(BASE_DIR, "scratch/indexed_photos.json")
APP_DATA_DIR = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596"
PREVIEWS_DIR = os.path.join(APP_DATA_DIR, "previews")
REVIEW_MD_PATH = os.path.join(BASE_DIR, "candidate_gallery.md")

def get_focal_length_num(fl_str):
    if not fl_str:
        return None
    try:
        # e.g. "70.0 mm" -> 70.0
        parts = fl_str.replace("mm", "").strip().split()
        if parts:
            return float(parts[0])
    except:
        pass
    return None

def select_candidates_for_folder(photos):
    # If 1 or 2 photos, select all
    if len(photos) <= 2:
        return photos
        
    # Heuristic selection:
    # We want to find a wide-angle (landscape/nature) and a telephoto/shallow depth of field (portrait/details)
    wide_angle = None
    tele_or_portrait = None
    
    # Try to find a wide-angle shot (focal length <= 35mm)
    for p in photos:
        fl = get_focal_length_num(p["metadata"]["focal_length"])
        if fl is not None and fl <= 35.0:
            wide_angle = p
            break
            
    # Try to find a telephoto/portrait shot (focal length >= 50mm or aperture wide <= f/2.8)
    for p in photos:
        fl = get_focal_length_num(p["metadata"]["focal_length"])
        ap = p["metadata"]["aperture"]
        is_tele = fl is not None and fl >= 50.0
        is_wide_ap = False
        if ap and ap.startswith("f/"):
            try:
                f_val = float(ap.replace("f/", ""))
                if f_val <= 2.8:
                    is_wide_ap = True
            except:
                pass
        if is_tele or is_wide_ap:
            if p != wide_angle:
                tele_or_portrait = p
                break
                
    selected = []
    if wide_angle:
        selected.append(wide_angle)
    if tele_or_portrait:
        selected.append(tele_or_portrait)
        
    # If we couldn't find matches, or we only got 1, fill with evenly spaced chronologically
    if len(selected) == 0:
        # Pick first and middle
        idx1 = 0
        idx2 = len(photos) // 2
        selected.append(photos[idx1])
        if idx2 != idx1:
            selected.append(photos[idx2])
    elif len(selected) == 1:
        # Find one more that is different
        for p in photos:
            if p not in selected:
                selected.append(p)
                break
                
    # Sort selected by path or date
    return selected[:2]

def curate_and_generate_sheet():
    if not os.path.exists(INDEXed_JSON):
        print(f"Error: {INDEXed_JSON} does not exist. Run indexer first.")
        return
        
    with open(INDEXed_JSON, "r") as f:
        all_photos = json.load(f)
        
    print(f"Loaded {len(all_photos)} indexed photo records.")
    
    # Group by folder
    folders_dict = {}
    for p in all_photos:
        fld = p["folder"]
        if fld not in folders_dict:
            folders_dict[fld] = []
        folders_dict[fld].append(p)
        
    print(f"Found {len(folders_dict)} unique folders.")
    
    # Curate candidates
    shortlisted = []
    for fld, photos in folders_dict.items():
        candidates = select_candidates_for_folder(photos)
        shortlisted.extend(candidates)
        
    print(f"Shortlisted {len(shortlisted)} candidate photos from all folders.")
    
    # Create previews directory
    os.makedirs(PREVIEWS_DIR, exist_ok=True)
    
    # Generate previews and md entries
    markdown_lines = [
        "# Photo Curation & Review Sheet (10-Year DSLR Archive)",
        "",
        "We have scanned your `/Volumes/Pictures` drive and curated a first batch of **candidate photos** (1-2 per folder, focusing on landscapes, portraits, nature, and family moments).",
        "",
        "## How to approve images",
        "To approve and import these images, reply in the chat with their **ID** (e.g. `CAND_001`, `CAND_005`), and provide their custom titles/stories if you have any. For example:",
        "```",
        "CAND_001: Title - Evening at Yosemite Valley, Story - We watched the sun light up El Capitan just before dusk.",
        "CAND_005: Title - Baby Sia's First Steps",
        "```",
        "If you approve an image but don't specify a title/story, we will auto-generate descriptive titles based on their folder and date.",
        "",
        "---",
        ""
    ]
    
    processed_candidates = []
    
    for i, item in enumerate(shortlisted):
        cand_id = f"CAND_{i+1:03d}"
        src_path = item["file_path"]
        folder = item["folder"]
        filename = item["filename"]
        meta = item["metadata"]
        
        # Save a compressed temp preview
        preview_filename = f"{cand_id}_{filename}"
        preview_path = os.path.join(PREVIEWS_DIR, preview_filename)
        
        # Check if preview already exists to save time
        if not os.path.exists(preview_path):
            try:
                with Image.open(src_path) as img:
                    img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                    img.save(preview_path, "JPEG", quality=80)
            except Exception as e:
                print(f"Failed to generate preview for {src_path}: {e}")
                continue
                
        # Format EXIF string
        exif_parts = []
        if meta["camera"]: exif_parts.append(f"Camera: {meta['camera']}")
        if meta["lens"]: exif_parts.append(f"Lens: {meta['lens']}")
        if meta["aperture"]: exif_parts.append(f"Aperture: {meta['aperture']}")
        if meta["shutter_speed"]: exif_parts.append(f"Shutter: {meta['shutter_speed']}")
        if meta["iso"]: exif_parts.append(f"ISO: {meta['iso']}")
        if meta["focal_length"]: exif_parts.append(f"Focal: {meta['focal_length']}")
        exif_str = ", ".join(exif_parts) if exif_parts else "No EXIF details available"
        
        # Add to Markdown list
        markdown_lines.append(f"### ID: **{cand_id}**")
        markdown_lines.append(f"- **Original File**: `{filename}`")
        markdown_lines.append(f"- **Source Folder**: `{folder}`")
        markdown_lines.append(f"- **Date Taken**: `{meta['date_taken'] or 'Unknown'}`")
        markdown_lines.append(f"- **EXIF**: {exif_str}")
        markdown_lines.append(f"- **Full Path**: `{src_path}`")
        markdown_lines.append("")
        # Embed the image using file:// protocol so it renders in the chat UI
        markdown_lines.append(f"![{cand_id} Preview](file://{preview_path})")
        markdown_lines.append("")
        markdown_lines.append("---")
        markdown_lines.append("")
        
        processed_candidates.append({
            "cand_id": cand_id,
            "file_path": src_path,
            "filename": filename,
            "folder": folder,
            "date_taken": meta["date_taken"],
            "metadata": meta
        })
        
        if (i+1) % 50 == 0:
            print(f"Generated previews for {i+1} candidates...")
            
    # Write candidate metadata reference file
    reference_path = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
    with open(reference_path, "w") as f:
        json.dump(processed_candidates, f, indent=2)
        
    # Write Markdown Review Sheet
    with open(REVIEW_MD_PATH, "w") as f:
        f.write("\n".join(markdown_lines))
        
    print(f"\nCuration complete!")
    print(f"Generated {len(processed_candidates)} previews in {PREVIEWS_DIR}")
    print(f"Review sheet written to {REVIEW_MD_PATH}")
    print(f"Curated reference metadata saved to {reference_path}")

if __name__ == "__main__":
    curate_and_generate_sheet()
