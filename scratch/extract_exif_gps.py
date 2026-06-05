import os
import json
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

target_ids = {"CAND_106", "CAND_107", "CAND_349"}

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    # Need to reopen because verify() closes the file or alters state
    image = Image.open(filename)
    info = image._getexif()
    if not info:
        return {}
    
    exif_data = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            gps_data = {}
            for gps_tag in value:
                sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                gps_data[sub_decoded] = value[gps_tag]
            exif_data[decoded] = gps_data
        else:
            exif_data[decoded] = value
    return exif_data

for cand in candidates:
    if cand["cand_id"] in target_ids:
        print(f"ID: {cand['cand_id']}")
        cached_path = cand.get("cached_path")
        if cached_path and os.path.exists(cached_path):
            try:
                exif = get_exif(cached_path)
                print(f"  Camera Model: {exif.get('Model')}")
                print(f"  DateTimeOriginal: {exif.get('DateTimeOriginal')}")
                print(f"  GPSInfo: {exif.get('GPSInfo')}")
            except Exception as e:
                print(f"  Error reading EXIF: {e}")
        else:
            print(f"  Cached path not found: {cached_path}")
        print("-" * 40)
