import os
import json

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
INDEXED_JSON = os.path.join(BASE_DIR, "scratch/indexed_photos.json")

with open(INDEXED_JSON, "r") as f:
    photos = json.load(f)

for photo in photos:
    if photo.get("folder") == "2017-10-28":
        print(f"File: {photo['filename']}")
        print(f"  Path: {photo['file_path']}")
        print(f"  EXIF: {photo.get('metadata')}")
        print("-" * 40)
