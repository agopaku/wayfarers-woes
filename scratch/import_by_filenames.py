import os
import json
import fnmatch
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")
INDEXED_JSON_PATH = os.path.join(BASE_DIR, "scratch/indexed_photos.json")
HD_PICTURES_DIR = "/Volumes/Pictures/Pictures"
DEST_DIR = os.path.join(BASE_DIR, "images/ag-edits")
THUMB_DIR = os.path.join(BASE_DIR, "images/ag-edits-thumbnails")

target_names = [
    "DSC_0105 (2).jpg", "DSC_0673.jpg", "DSC_0200.jpg", "DSC_0920 copy.jpg", "DSC_0965.jpg",
    "DSC_0986.jpg", "DSC_1032.jpg", "DSC_1182.jpg", "DSC_1258.jpg", "DSC_2323.jpg",
    "DSC_4167.jpg", "DSC_4241.jpg", "DSC_0136-Edit-2.jpg", "DSC_0631-Edit.jpg",
    "DSC_0571-Edit.jpg", "DSC_0796-Edit.jpg", "DSC_0981-Edit.jpg", "IMG_0741-Edit.jpg",
    "DSC_1768-Edit.jpg", "DSC_3101-Edit.jpg", "DSC_3139-Edit.jpg", "DSC_3125-Edit.jpg",
    "DSC_3149-Edit.jpg", "DSC_3158-Edit.jpg", "DSC_3290-Edit.jpg", "DSC_5672-Edit.jpg",
    "DSC_5746-Edit.jpg", "DSC_5788-Edit.jpg", "IMG_2149.JPG", "IMG_2148.JPG",
    "IMG_2155.JPG", "DSC_8619.jpg", "DSC_8622.jpg", "DSC_8684.jpg", "DSC_8737.jpg",
    "DSC_8761.jpg", "IMG_9516.jpg", "DSC_9016.jpg", "IMG_2678.jpg", "IMG_2681.jpg",
    "DSC_9112.jpg", "IMG_2765.jpg", "DSC_9235.jpg", "DSC_9314.jpg", "IMG_2812.jpg",
    "DSC_9445.jpg", "DSC_9468.jpg", "DSC_9578.jpg", "DSC_9585.jpg", "DSC_9590.jpg",
    "DSC_9614.jpg", "DSC_9625.jpg", "DSC_9638.jpg", "DSC_9642.jpg", "IMG_2858.jpg",
    "DSC_9697.jpg", "DSC_9951.jpg", "DSC_0006.jpg", "DSC_0151.jpg", "DSC_0158.jpg",
    "DSC_0173.jpg", "DSC_0185.jpg", "DSC_0188.jpg", "DSC_0219.jpg", "DSC_0291.jpg",
    "DSC_0407.jpg", "DSC_0492.jpg", "DSC_0537.jpg", "DSC_2484.jpg", "DSC_2476.jpg",
    "DSC_2464.jpg", "DSC_2362.jpg", "IMG_3877.JPG", "DSC_3073.jpg", "DSC_3076.jpg",
    "DSC_3117.jpg", "DSC_3132.jpg", "DSC_3157.jpg", "DSC_3200.jpg", "DSC_3203.jpg",
    "DSC_3244.jpg", "DSC_3255.jpg", "DSC_3288.jpg", "DSC_3398.jpg", "DSC_3606.jpg",
    "DSC_3988.jpg", "DSC_4092.jpg", "DSC_4102.jpg", "DSC_4114.jpg", "DSC_4121.jpg",
    "DSC_4125.jpg", "DSC_4149.jpg", "DSC_4163.jpg", "DSC_4351-2.jpg", "DSC_4356.jpg",
    "DSC_4357.jpg", "DSC_4369.jpg", "DSC_4385.jpg", "DSC_4398.jpg", "DSC_4410.jpg",
    "DSC_4418.jpg", "DSC_4423.jpg", "IMG_4452.JPG", "DSC_4834.jpg", "DSC_0011.jpg",
    "DSC_0020.jpg", "DSC_0044.jpg", "DSC_0322.jpg", "DSC_0345.jpg", "DSC_0503.jpg",
    "DSC_0535.jpg", "DSC_0573.jpg", "DSC_0678.jpg", "DSC_0734.jpg", "DSC_0890.jpg",
    "DSC_0924.jpg", "DSC_0937.jpg", "DSC_0999.jpg", "DSC_1048.jpg", "DSC_1728.jpg",
    "DSC_1736.jpg", "DSC_1799.jpg", "DSC_1821.jpg", "DSC_1870.jpg", "DSC_2023.jpg",
    "DSC_2509.jpg", "DSC_2517.jpg", "DSC_2527-Pano.jpg", "DSC_2562.jpg", "DSC_2595.jpg",
    "DSC_2681.jpg", "DSC_2819.jpg", "DSC_2947.jpg", "DSC_3147.jpg", "DSC_3168.jpg",
    "DSC_3292.jpg", "DSC_3321.jpg", "DSC_3609.jpg", "DSC_3590.JPG", "DSC_3896.JPG",
    "DSC_4106.JPG", "DSC_4183.JPG", "DSC_4258.JPG", "DSC_4265.JPG", "DSC_4294.JPG",
    "DSC_4342.JPG", "DSC_4462.JPG", "DSC_4504.JPG", "DSC_4532.JPG", "DSC_4647.JPG",
    "DSC_4731.JPG", "DSC_4749.JPG", "DSC_4757.JPG", "_DSC4768.JPG", "_DSC5023.JPG",
    "_DSC5053.JPG", "_DSC5178-Pano.JPG", "DSC02912.jpg", "IMG_0163.jpg", "IMG_0162.jpg",
    "DSC_5775.jpg", "DSC_5787.jpg", "DSC_6163.jpg", "DSC_6179.jpg", "DSC_7040.jpg",
    "DSC_7036-Pano.jpg", "DSC_7039.jpg", "DSC_7153.jpg", "DSC_7301.jpg", "DSC_7345-Pano.jpg",
    "DSC_7385.jpg", "DSC_7437.jpg", "DSC_7447.jpg", "IMG_6074.JPG", "DSC_7871.jpg",
    "DSC_7999.jpg", "DSC_8477.jpg", "DSC_8420.jpg", "DSC_8432.jpg", "DSC_8446.jpg",
    "DSC_8456-2.jpg", "DSC_8460.jpg", "DSC_8464.jpg", "DSC_9209.jpg", "DSC_9464.jpg",
    "DSC_9469.jpg", "DSC_9526.jpg", "DSC_9717.jpg", "DSC_9776.jpg", "DSC02919.jpg",
    "DSC03310.jpg", "DSC03433.jpg", "DSC03591.jpg", "DSC03612.jpg", "DSC03815.jpg",
    "DSC01519.jpeg", "DSC01742.jpeg", "DSC01340.jpeg", "DSC02009.jpeg", "DSC02019.jpeg",
    "DSC02024.jpeg", "DSC02131.jpeg", "DSC02134.jpg", "DSC02190-2.jpg", "DSC02201.jpg",
    "DSC02216.jpg", "DSC02276-2.jpg", "DSC02305.jpg", "DSC02317.jpg", "DSC02349.jpg",
    "DSC02386-2.jpg", "DSC02388.jpg", "DSC02456-2.jpg"
]

def format_date_display(dt_str):
    if not dt_str or dt_str.lower() == "unknown":
        return ""
    try:
        dt = datetime.strptime(dt_str.split()[0], "%Y-%m-%d")
        return dt.strftime("%b %d, %Y")
    except Exception:
        return dt_str

def parse_exif(img_path):
    meta = {
        "camera": "", "lens": "", "aperture": "", "shutter_speed": "",
        "iso": "", "focal_length": "", "date_taken": ""
    }
    try:
        with Image.open(img_path) as img:
            exif = img._getexif()
            if exif:
                for tag, val in exif.items():
                    decoded = TAGS.get(tag, tag)
                    if decoded == "Model":
                        meta["camera"] = str(val).strip()
                    elif decoded == "DateTimeOriginal" or decoded == "DateTime":
                        try:
                            # Standard format: YYYY:MM:DD HH:MM:SS
                            dt = datetime.strptime(val[:19], "%Y:%m:%d %H:%M:%S")
                            meta["date_taken"] = dt.strftime("%Y-%m-%d %H:%M:%S")
                        except Exception:
                            meta["date_taken"] = str(val).strip()
                    elif decoded == "FocalLength":
                        try:
                            meta["focal_length"] = f"{float(val[0])/float(val[1])} mm"
                        except:
                            meta["focal_length"] = f"{val} mm"
                    elif decoded == "FNumber":
                        try:
                            meta["aperture"] = f"f/{float(val[0])/float(val[1])}"
                        except:
                            meta["aperture"] = f"f/{val}"
                    elif decoded == "ExposureTime":
                        try:
                            exposure = float(val[0])/float(val[1])
                            if exposure < 1.0:
                                meta["shutter_speed"] = f"1/{int(1.0/exposure)}s"
                            else:
                                meta["shutter_speed"] = f"{exposure}s"
                        except:
                            meta["shutter_speed"] = f"{val}s"
                    elif decoded == "ISOSpeedRatings":
                        meta["iso"] = str(val)
    except Exception as e:
        print(f"Warning parsing EXIF for {img_path}: {e}")
    return meta

def main():
    if not os.path.exists(HD_PICTURES_DIR):
        print(f"Error: Hard drive pictures folder {HD_PICTURES_DIR} is not mounted.")
        print("Please connect the hard drive and try again.")
        return

    # 1. Load gallery to prevent duplicate imports
    gallery = []
    if os.path.exists(GALLERY_JSON_PATH):
        with open(GALLERY_JSON_PATH, "r") as f:
            gallery = json.load(f)
    gallery_filenames = {os.path.basename(x.get("filename", "")).lower() for x in gallery}

    # Helper mapping of date -> location to auto-infer locations
    date_locations = {}
    for item in gallery:
        dt = item.get("date")
        loc = item.get("location")
        if dt and loc and loc != "Unknown Location":
            date_locations[dt] = loc

    # 2. Load indexed photos mapping
    indexed_dict = {}
    if os.path.exists(INDEXED_JSON_PATH):
        with open(INDEXED_JSON_PATH, "r") as f:
            for item in json.load(f):
                indexed_dict[item["filename"].lower()] = item

    # 3. Find files on the connected hard drive
    found_files = {} # lower_filename -> full_path
    
    # Check ones we already have paths for in index
    to_find_names = []
    for name in target_names:
        name_l = name.lower()
        if name_l in gallery_filenames:
            print(f"File {name} already exists in the gallery database. Skipping.")
            continue
            
        if name_l in indexed_dict:
            # Check if index path exists
            index_path = indexed_dict[name_l]["file_path"]
            if os.path.exists(index_path):
                found_files[name_l] = index_path
            else:
                # If path doesn't exist (e.g. mount points shifted), we search for it
                to_find_names.append(name)
        else:
            to_find_names.append(name)

    # 4. Search HD recursively for missing filenames
    if to_find_names:
        print(f"Scanning HD for {len(to_find_names)} files not in index or with missing paths...")
        to_find_lower = {x.lower() for x in to_find_names}
        
        for root, dirs, files in os.walk(HD_PICTURES_DIR):
            # Exclude raw directories or ag-edits-thumbnails to be faster
            if "ag-edits-thumbnails" in root or "previews" in root:
                continue
            for file in files:
                file_l = file.lower()
                if file_l in to_find_lower and file_l not in found_files:
                    found_files[file_l] = os.path.join(root, file)
                    print(f"  Found: {file} at {found_files[file_l]}")
                    if len(found_files) == len(target_names) - len(gallery_filenames):
                        break

    print(f"\nScan complete. Total files to import: {len(found_files)}")

    # 5. Optimize, copy and insert to gallery
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(THUMB_DIR, exist_ok=True)
    
    imported_count = 0
    for name in target_names:
        name_l = name.lower()
        if name_l not in found_files:
            if name_l not in gallery_filenames:
                print(f"✗ Could not find file {name} on the connected hard drive.")
            continue
            
        src_path = found_files[name_l]
        filename = os.path.basename(src_path)
        dest_path = os.path.join(DEST_DIR, filename)
        thumb_path = os.path.join(THUMB_DIR, filename)
        
        # Skip if duplicate
        if filename.lower() in gallery_filenames:
            continue
            
        # Parse EXIF metadata
        meta = parse_exif(src_path)
        
        # If date taken is missing, try to infer from folder path
        if not meta["date_taken"]:
            # Check if parent folder matches a date format like YYYY-MM-DD
            parent_folder = os.path.basename(os.path.dirname(os.path.dirname(src_path)))
            try:
                dt = datetime.strptime(parent_folder, "%Y-%m-%d")
                meta["date_taken"] = dt.strftime("%Y-%m-%d 12:00:00")
            except:
                pass
                
        # 1. Resize & Optimize original (2048px max dimension)
        try:
            print(f"Optimizing: {filename}...")
            with Image.open(src_path) as img:
                exif_data = img.info.get('exif')
                img.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
                if exif_data:
                    img.save(dest_path, "JPEG", quality=85, optimize=True, exif=exif_data)
                else:
                    img.save(dest_path, "JPEG", quality=85, optimize=True)
        except Exception as e:
            print(f"Error optimizing {filename}: {e}")
            continue

        # 2. Generate thumbnail (800px max dimension)
        try:
            print(f"Generating thumbnail for: {filename}...")
            with Image.open(src_path) as img:
                img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                img.save(thumb_path, "JPEG", quality=85, optimize=True)
        except Exception as e:
            print(f"Error generating thumbnail for {filename}: {e}")
            if os.path.exists(dest_path):
                os.remove(dest_path)
            continue
            
        # 3. Infer Location and details
        display_date = format_date_display(meta["date_taken"])
        location = "Unknown Location"
        if display_date in date_locations:
            location = date_locations[display_date]
            print(f"  Inferred Location: {location} (based on date {display_date})")
            
        # Auto-infer title and description
        parent_dir = os.path.basename(os.path.dirname(os.path.dirname(src_path)))
        title = f"Photo from {parent_dir}" if "-" in parent_dir else f"Photo {filename}"
        description = f"Photo captured on {display_date}." if display_date else "Photo from DSLR archive."
        
        # Category heuristic (default to landscape)
        category = "landscape"
        fl_val = meta.get("focal_length", "")
        if fl_val:
            try:
                fl = float(fl_val.replace("mm","").strip())
                if fl >= 50.0:
                    category = "portrait"
            except:
                pass
                
        # Insert entry
        entry = {
            "filename": f"images/ag-edits/{filename}",
            "title": title,
            "description": description,
            "location": location,
            "date": display_date,
            "camera": meta.get("camera") or "",
            "lens": meta.get("lens") or "",
            "aperture": meta.get("aperture") or "",
            "shutterSpeed": meta.get("shutter_speed") or "",
            "iso": meta.get("iso") or "",
            "focalLength": meta.get("focal_length") or "",
            "category": category
        }
        
        gallery.append(entry)
        gallery_filenames.add(filename.lower())
        imported_count += 1
        print(f"✓ Successfully imported {filename}!")
        
    if imported_count == 0:
        print("\nNo new photos were imported.")
        return

    # 4. Sort chronologically
    def parse_entry_date(item):
        d_str = item.get("date", "")
        try:
            return datetime.strptime(d_str, "%b %d, %Y")
        except ValueError:
            pass
        return datetime.max
        
    gallery.sort(key=parse_entry_date)
    
    with open(GALLERY_JSON_PATH, "w") as f:
        json.dump(gallery, f, indent=2)
        
    print(f"\nImport finished! Successfully imported {imported_count} new images.")
    print(f"Total gallery size: {len(gallery)} items.")

if __name__ == "__main__":
    main()
