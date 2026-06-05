import json
import os
from datetime import datetime

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
GALLERY_JSON_PATH = os.path.join(BASE_DIR, "gallery.json")

def parse_entry_date(item):
    d_str = item.get("date", "")
    if not d_str:
        return datetime.min
        
    # Standard format used in gallery: "May 17, 2016" or "May 17, 2016 12:00:00"
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            # Clean up potential leading/trailing spaces
            return datetime.strptime(d_str.strip(), fmt)
        except ValueError:
            continue
            
    # If date string contains month and year, try parsing it e.g. "May 2016"
    try:
        return datetime.strptime(d_str.strip(), "%b %Y")
    except ValueError:
        pass
        
    print(f"Warning: Could not parse date format for '{d_str}' in item '{item.get('title')}'")
    return datetime.min

def main():
    if not os.path.exists(GALLERY_JSON_PATH):
        print("gallery.json not found.")
        return
        
    with open(GALLERY_JSON_PATH, "r") as f:
        gallery = json.load(f)
        
    # Sort descending (newest first)
    gallery.sort(key=parse_entry_date, reverse=True)
    
    with open(GALLERY_JSON_PATH, "w") as f:
        json.dump(gallery, f, indent=2)
        
    print(f"Successfully sorted {len(gallery)} entries in gallery.json in descending order of date (newest first).")

if __name__ == "__main__":
    main()
