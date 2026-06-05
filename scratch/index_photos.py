import os
import json
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Paths
BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
PICTURES_DIR = "/Volumes/Pictures/Pictures"
INDEX_OUTPUT_PATH = os.path.join(BASE_DIR, "scratch/indexed_photos.json")

# Root-level directories to skip entirely
SKIP_ROOT_DIRS = {
    ".spotlight-v100",
    ".fseventsd",
    ".trashes",
    "lightroom library.lrlibrary",
    "lightroom",
    "videos",
    "drone videos",
    "seattle highwayone videos",
    "smokies video",
    "system volume information",
    "$recycle.bin",
    "music",
    "found.000",
    "ichat icons"
}

def get_exif_metadata(img_path):
    metadata = {
        "date_taken": None,
        "camera": None,
        "lens": None,
        "aperture": None,
        "shutter_speed": None,
        "iso": None,
        "focal_length": None
    }
    
    try:
        with Image.open(img_path) as img:
            exif = img._getexif()
            if not exif:
                return metadata
            
            exif_data = {}
            for tag, value in exif.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
            
            # Date Taken (36867 is DateTimeOriginal)
            dt_str = exif_data.get("DateTimeOriginal") or exif_data.get(36867)
            if dt_str:
                try:
                    dt = datetime.strptime(str(dt_str).strip(), "%Y:%m:%d %H:%M:%S")
                    metadata["date_taken"] = dt.strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    metadata["date_taken"] = str(dt_str)
            
            # Camera Make/Model
            make = exif_data.get("Make", "")
            model = exif_data.get("Model", "")
            if model:
                if make and make.lower() not in model.lower():
                    metadata["camera"] = f"{make} {model}".strip()
                else:
                    metadata["camera"] = model.strip()
            
            # Lens Model (Tag 0xa434 is LensModel)
            lens = exif_data.get("LensModel") or exif_data.get(0xa434)
            if lens:
                metadata["lens"] = str(lens).strip()
            
            # Aperture (FNumber)
            f_num = exif_data.get("FNumber")
            if f_num is not None:
                try:
                    metadata["aperture"] = f"f/{float(f_num):.1f}"
                except (ValueError, TypeError, ZeroDivisionError):
                    metadata["aperture"] = f"f/{f_num}"
            
            # Shutter Speed (ExposureTime)
            exp_time = exif_data.get("ExposureTime")
            if exp_time is not None:
                try:
                    val = float(exp_time)
                    if val > 0:
                        if val < 1.0:
                            denom = round(1.0 / val)
                            metadata["shutter_speed"] = f"1/{denom}s"
                        else:
                            metadata["shutter_speed"] = f"{val:.1f}s"
                except (ValueError, TypeError, ZeroDivisionError):
                    metadata["shutter_speed"] = f"{exp_time}s"
            
            # ISO (ISOSpeedRatings)
            iso = exif_data.get("ISOSpeedRatings")
            if iso is not None:
                metadata["iso"] = str(iso)
            
            # Focal Length
            foc_len = exif_data.get("FocalLength")
            if foc_len is not None:
                try:
                    metadata["focal_length"] = f"{float(foc_len):.1f} mm"
                except (ValueError, TypeError, ZeroDivisionError):
                    metadata["focal_length"] = f"{foc_len} mm"
                    
    except Exception as e:
        # Avoid printing error for every file if it's just missing EXIF
        pass
        
    return metadata

def load_existing_gallery_filenames():
    if not os.path.exists(GALLERY_JSON_PATH):
        return set()
    try:
        with open(GALLERY_JSON_PATH, "r") as f:
            data = json.load(f)
        existing = set()
        for item in data:
            filename = item.get("filename", "")
            base = os.path.basename(filename)
            if base:
                existing.add(base.lower())
        return existing
    except Exception as e:
        print(f"Error loading gallery.json: {e}")
        return set()

def resolve_missing_metadata(file_path, filename, folder, meta):
    # 1. Parse folder name to get a fallback date
    fallback_date = None
    try:
        dt_folder = datetime.strptime(folder.strip(), "%Y-%m-%d")
        fallback_date = dt_folder.strftime("%Y-%m-%d 12:00:00")
    except ValueError:
        try:
            parts = folder.strip().split("-")
            if len(parts) >= 3 and len(parts[0]) == 4:
                dt_folder = datetime.strptime("-".join(parts[:3]), "%Y-%m-%d")
                fallback_date = dt_folder.strftime("%Y-%m-%d 12:00:00")
        except ValueError:
            pass
            
    # 2. Check parent folder for original file EXIF if camera info is missing
    parent_dir = os.path.dirname(os.path.dirname(file_path))
    stem, _ = os.path.splitext(filename)
    parent_file = None
    if os.path.exists(parent_dir):
        for f in os.listdir(parent_dir):
            f_stem, f_ext = os.path.splitext(f)
            if f_stem.lower() == stem.lower() and f.lower() not in ['.ds_store', 'thumbs.db']:
                parent_file = os.path.join(parent_dir, f)
                break
                
    if parent_file:
        parent_meta = get_exif_metadata(parent_file)
        for k in ["camera", "lens", "aperture", "shutter_speed", "iso", "focal_length", "date_taken"]:
            if not meta[k] and parent_meta[k]:
                meta[k] = parent_meta[k]
                
    # 3. Use fallback date if date_taken is still missing or "Unknown"
    if not meta["date_taken"] or str(meta["date_taken"]).lower() == "unknown":
        if fallback_date:
            meta["date_taken"] = fallback_date
            
    return meta

def index_photos():
    print(f"Scanning target folders under {PICTURES_DIR}...")
    existing_filenames = load_existing_gallery_filenames()
    print(f"Loaded {len(existing_filenames)} filenames already in the gallery.")
    
    indexed_images = []
    duplicate_count = 0
    total_found = 0
    
    # Get top-level directories to crawl
    try:
        top_level_items = os.listdir(PICTURES_DIR)
    except Exception as e:
        print(f"Failed to list {PICTURES_DIR}: {e}")
        return

    target_dirs = []
    for item in top_level_items:
        item_path = os.path.join(PICTURES_DIR, item)
        if os.path.isdir(item_path) and item.lower() not in SKIP_ROOT_DIRS:
            target_dirs.append(item_path)
            
    print(f"Identified {len(target_dirs)} top-level directories to scan.")
    
    for target_dir in target_dirs:
        print(f"Scanning: {target_dir}...")
        for root, dirs, files in os.walk(target_dir):
            basename = os.path.basename(root)
            if basename.lower() == "ag-edits":
                for file in files:
                    if file.startswith('.'):
                        continue
                    if file.lower().endswith(('.jpg', '.jpeg')):
                        total_found += 1
                        file_path = os.path.join(root, file)
                        
                        # Deduplicate by filename
                        if file.lower() in existing_filenames:
                            duplicate_count += 1
                            continue
                            
                        meta = get_exif_metadata(file_path)
                        meta = resolve_missing_metadata(file_path, file, os.path.basename(os.path.dirname(root)), meta)
                        
                        indexed_images.append({
                            "file_path": file_path,
                            "filename": file,
                            "folder": os.path.basename(os.path.dirname(root)),
                            "size_bytes": os.path.getsize(file_path),
                            "mtime": os.path.getmtime(file_path),
                            "metadata": meta
                        })
                        
                        if len(indexed_images) % 100 == 0:
                            print(f"Indexed {len(indexed_images)} new images...")
                            
    # Sort indexed images chronologically
    def sort_key(item):
        dt = item["metadata"]["date_taken"]
        if dt:
            return dt
        return item["file_path"]
        
    indexed_images.sort(key=sort_key)
    
    # Save indexed results
    os.makedirs(os.path.dirname(INDEX_OUTPUT_PATH), exist_ok=True)
    with open(INDEX_OUTPUT_PATH, "w") as f:
        json.dump(indexed_images, f, indent=2)
        
    print(f"\nTargeted indexing finished!")
    print(f"Total JPEG images found in targeted ag-edits: {total_found}")
    print(f"Filtered out duplicates already in gallery: {duplicate_count}")
    print(f"Successfully indexed new candidate images: {len(indexed_images)}")
    print(f"Index written to {INDEX_OUTPUT_PATH}")

if __name__ == "__main__":
    index_photos()
