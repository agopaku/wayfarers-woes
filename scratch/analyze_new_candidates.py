import os
import json
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
FOUND_JSON = os.path.join(BASE_DIR, "scratch/found_scan_results.json")
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

# Load existing curated filenames to filter new ones
curated = []
if os.path.exists(CURATED_JSON):
    with open(CURATED_JSON, "r") as f:
        curated = json.load(f)
curated_filenames = {c["filename"].lower() for c in curated}

with open(FOUND_JSON, "r") as f:
    found = json.load(f)

new_files = []
for name, path in found.items():
    if name not in curated_filenames:
        new_files.append((name, path))

print(f"Total new files to analyze: {len(new_files)}")

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
                    elif decoded == "DateTimeOriginal":
                        try:
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
        pass
    return meta

# Group by parent folder and analyze a sample from each group
groups = {}
for name, path in new_files:
    parent = os.path.dirname(path)
    groups[parent] = groups.get(parent, []) + [(name, path)]

print("\n--- Folder Groups Summary ---")
for parent, files in sorted(groups.items(), key=lambda x: -len(x[1])):
    print(f"Parent: {parent} ({len(files)} files)")
    # Analyze first file as a representative
    sample_name, sample_path = files[0]
    meta = parse_exif(sample_path)
    print(f"  Sample: {sample_name} | Camera: {meta['camera']} | Date: {meta['date_taken']}")
