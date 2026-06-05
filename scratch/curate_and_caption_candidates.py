import os
import json
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")
FOUND_JSON = os.path.join(BASE_DIR, "scratch/found_scan_results.json")
APP_DATA_DIR = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596"
ORIGINAL_CACHE_DIR = os.path.join(APP_DATA_DIR, "original_cache")
PREVIEWS_DIR = os.path.join(APP_DATA_DIR, "previews")

os.makedirs(ORIGINAL_CACHE_DIR, exist_ok=True)
os.makedirs(PREVIEWS_DIR, exist_ok=True)

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
        print(f"Warning parsing EXIF: {e}")
    return meta

def get_location_and_story(filename, folder, date_str, meta):
    # Default fallback
    location = "Unknown Location"
    title = f"Photo {filename}"
    story = "A beautiful frame captured in our archives."
    category = "landscape"

    # Analyze metadata
    camera = meta.get("camera", "") or ""
    focal_length_str = meta.get("focal_length", "") or ""
    aperture_str = meta.get("aperture", "") or ""

    # Estimate category
    is_portrait = False
    try:
        if focal_length_str:
            fl_val = float(focal_length_str.replace("mm","").strip())
            if fl_val >= 50.0:
                is_portrait = True
        if aperture_str and aperture_str.startswith("f/"):
            ap_val = float(aperture_str.replace("f/","").strip())
            if ap_val <= 2.2:
                is_portrait = True
    except:
        pass

    if is_portrait:
        category = "portrait"

    # Helper date converter
    dt = None
    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except:
            try:
                dt = datetime.strptime(date_str.split()[0], "%Y-%m-%d")
            except:
                pass

    # Kinnaur / Spiti Valley Trip (May - June 2016)
    if "kinnaur" in folder.lower() or "spiti" in folder.lower() or (dt and dt.year == 2016 and dt.month == 5):
        location = "Kinnaur, Himachal Pradesh, India"
        category = "portrait" if is_portrait else "landscape"
        if "dsc_0006" in filename.lower():
            title = "Himalayan Stream near Charang"
            story = "A sparkling mountain stream flowing through the rocky valleys of Kinnaur, along the Kinner Kailash circuit."
        elif "dsc_0158" in filename.lower():
            title = "A Local Smile in Kinnaur"
            story = "A warm, friendly local resident greeting us during our road trip through the remote village of Charang."
            category = "portrait"
        elif "dsc_0185" in filename.lower():
            title = "Navigating the Cliffhanger Routes"
            story = "Our taxi navigating precariously along the edge of the deep gorge, showcasing the legendary, challenging roads of Kinnaur."
        elif "dsc_0219" in filename.lower():
            title = "Charang Village Farmlands"
            story = "Terraced green fields contrasting beautifully with the dry, towering mountains of the high-altitude Kinnaur valley."
        elif "dsc_0291" in filename.lower():
            title = "Ancient Rangrik Shungma Temple"
            story = "The rustic entrance of the centuries-old Buddhist temple in Charang village, radiating quiet spirituality."
        elif "dsc_0407" in filename.lower():
            title = "Prayer Flags Fluttering in the Wind"
            story = "Colorful Buddhist prayer flags stretching across the windswept mountain passes, sending prayers into the valley."
        else:
            title = "Kinnaur Mountain Expedition"
            story = "Traversing the rugged, majestic terrains of Kinnaur on our road expedition, surrounded by giant peaks."

    # Lake Superior / Duluth winter trip (Dec 2017 - Jan 2018)
    elif "2017-12-31" in folder or "2017-12-24" in folder or (dt and dt.year in (2017, 2018) and dt.month == 12) or (dt and dt.year == 2018 and dt.month == 1 and dt.day <= 15):
        location = "Duluth, Lake Superior, Minnesota, USA"
        category = "landscape"
        if "dsc_4294" in filename.lower():
            title = "Frozen Shoreline of Lake Superior"
            story = "Giant blocks of ice and snow covering the black volcanic rocks of the Duluth shoreline during a brutal winter freeze."
        elif "dsc_4258" in filename.lower():
            title = "Lake Superior Sea Smoke"
            story = "Beautiful sea smoke rising from the freezing waters of Lake Superior on a sub-zero winter morning."
        elif "dsc_4265" in filename.lower():
            title = "Canal Park Ice Formations"
            story = "Thick, glassy ice layers coating the lighthouse piers and rocks at Canal Park in Duluth."
        elif "dsc_4647" in filename.lower():
            title = "Minnesota's Frozen North Shore"
            story = "A serene, snow-draped view of the Lake Superior coast, showcasing the quiet power of winter."
        else:
            title = "Sub-Zero Duluth Exploration"
            story = "Exploring the freezing shores of Lake Superior in Duluth, where temperatures dropped below -40°F."

    # South Dakota / Badlands (Sep 2017)
    elif "2017-09-01" in folder or "2017-09-02" in folder or (dt and dt.year == 2017 and dt.month == 9 and dt.day <= 5):
        location = "Badlands National Park, South Dakota, USA"
        category = "landscape"
        title = "Glow over the Badlands Spire"
        story = "The dramatic, layered mudstone formations and steep ridges of the Badlands glowing in the warm gold of sunset."

    # Grand Teton / Yellowstone (Sep-Oct 2025)
    elif "2025-09" in folder or "2025-10" in folder or (dt and dt.year == 2025 and dt.month == 9 and dt.day >= 25) or (dt and dt.year == 2025 and dt.month == 10 and dt.day <= 3):
        location = "Grand Teton National Park, Wyoming, USA"
        category = "landscape"
        if "dsc09118" in filename.lower() or "dsc09128" in filename.lower():
            title = "Jenny Lake Morning Mist"
            story = "A quiet, misty morning at Jenny Lake, with the Grand Teton peaks emerging slowly behind the fog."
        elif "dsc09225" in filename.lower() or "dsc09237" in filename.lower():
            title = "Grand Teton Peaks in Autumn"
            story = "Golden aspens and yellow shrubs framing the sharp, snow-dusted granite peaks of the Teton Range."
        else:
            title = "Yellowstone Geothermal Valleys"
            story = "Steaming pools and thermal vents rising from the colorful caldera floor of Yellowstone under a clear sky."

    # Naperville Baby / Family Photoshoots
    elif "2020-01-10" in folder or "2020-12-20" in folder or "iphone" in folder.lower() or (dt and dt.year in (2020, 2021) and dt.month == 1 and dt.day == 10) or (dt and dt.year == 2020 and dt.month == 12 and dt.day == 20):
        location = "Naperville, Illinois, USA"
        category = "portrait"
        if "dsc02305" in filename.lower():
            title = "Evie's Sweet Toddler Smile"
            story = "A delightful, bright-eyed portrait of Evie playing indoors, filled with laughter and curiosity."
        elif "img_2149" in filename.lower() or "img_2148" in filename.lower() or "img_2155" in filename.lower():
            title = "Evie's First Cozy Christmas"
            story = "Warm, cozy holiday moments at home shortly after Evie was born, celebrating family and winter cheer."
        else:
            title = "Evie's Happy Milestones"
            story = "Cherishing sweet, candid childhood milestones and cozy home memories in Naperville."

    # Arizona Trip (April-May 2022)
    elif "arizona" in folder.lower() or (dt and dt.year == 2022 and dt.month == 4 and dt.day >= 28) or (dt and dt.year == 2022 and dt.month == 5 and dt.day <= 5):
        location = "Sedona, Arizona, USA"
        category = "landscape"
        title = "Red Rock Canyons of Arizona"
        story = "The spectacular red sandstone formations of Sedona rising against a vast, deep blue desert sky."

    # Oregon Coast / PCH Trip (Oct 2022)
    elif "2022-10" in folder or (dt and dt.year == 2022 and dt.month == 10):
        location = "Oregon Coast, USA"
        category = "landscape"
        title = "Sea Stacks in the Pacific Mist"
        story = "Towering sea stacks rising from the pounding ocean waves, shrouded in coastal mist and temperate forest outlines."

    # General / Other
    else:
        if dt:
            title = f"Travelogue Archive - {dt.strftime('%B %Y')}"
            story = f"A memorable frame captured during our travels in {dt.strftime('%B %Y')}."
        else:
            title = f"Curation Archive - {folder}"
            story = f"A curated photograph from the {folder} archive directory."

    return title, story, location, category

def main():
    # 1. Load existing candidates
    curated_candidates = []
    if os.path.exists(CURATED_JSON):
        with open(CURATED_JSON, "r") as f:
            curated_candidates = json.load(f)
            
    # Map filenames to candidates to find duplicates
    curated_filenames = {c["filename"].lower(): c for c in curated_candidates}
    
    # Max candidate ID index
    max_id_num = 0
    for c in curated_candidates:
        cid = c["cand_id"]
        try:
            num = int(cid.split("_")[1])
            if num > max_id_num:
                max_id_num = num
        except:
            pass
            
    print(f"Loaded {len(curated_candidates)} existing candidates. Max ID index: {max_id_num}")

    # 2. Load scan results
    if not os.path.exists(FOUND_JSON):
        print(f"Error: {FOUND_JSON} not found. Run scan_hd.py first.")
        return
        
    with open(FOUND_JSON, "r") as f:
        found_scan = json.load(f)

    # 3. Add new candidates from found scan results
    newly_added = 0
    skipped_count = 0
    
    for filename_l, full_path in found_scan.items():
        filename = os.path.basename(full_path)
        
        # Check if already a curated candidate
        if filename_l in curated_filenames:
            # We will just update its path if it shifted, but keep candidate details
            cand = curated_filenames[filename_l]
            cand["file_path"] = full_path
            continue
            
        # Parse EXIF metadata
        meta = parse_exif(full_path)
        
        # Inferred folder name from path
        parts = full_path.split("/")
        folder = parts[-3] if len(parts) >= 3 else "Unknown"
        
        # Determine candidate ID
        max_id_num += 1
        cand_id = f"CAND_{max_id_num:03d}"
        
        # Cache original copy
        cached_filename = f"{cand_id}_{filename}"
        cached_path = os.path.join(ORIGINAL_CACHE_DIR, cached_filename)
        
        print(f"Processing new candidate {cand_id}: {filename}")
        try:
            shutil.copy2(full_path, cached_path)
        except Exception as e:
            print(f"  Error copying file to original_cache: {e}")
            max_id_num -= 1 # Revert ID
            continue
            
        # Generate 800px preview
        preview_path = os.path.join(PREVIEWS_DIR, cached_filename)
        try:
            with Image.open(full_path) as img:
                img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                img.save(preview_path, "JPEG", quality=80)
        except Exception as e:
            print(f"  Error generating preview: {e}")
            if os.path.exists(cached_path):
                os.remove(cached_path)
            max_id_num -= 1
            continue

        # Get catchy title, story, location, category
        title, story, location, category = get_location_and_story(filename, folder, meta["date_taken"], meta)
        
        # Create candidate dictionary entry
        cand_entry = {
            "cand_id": cand_id,
            "file_path": full_path,
            "filename": filename,
            "folder": folder,
            "date_taken": meta["date_taken"] or f"{folder} 12:00:00",
            "metadata": meta,
            "cached_path": cached_path,
            "title": title,
            "description": story,
            "location": location,
            "category": category
        }
        
        curated_candidates.append(cand_entry)
        newly_added += 1

    print(f"\nAdded {newly_added} new candidates.")

    # 4. Write catchy captions for any candidate in curated_candidates.json that has empty or generic details
    updated_captions = 0
    for cand in curated_candidates:
        filename = cand["filename"]
        folder = cand["folder"]
        date_str = cand.get("date_taken") or cand["metadata"].get("date_taken")
        
        # Check if details are missing or generic
        has_generic_title = not cand.get("title") or "photo from" in cand.get("title").lower() or "photo dsc" in cand.get("title").lower() or cand.get("title") == f"Photo {filename}"
        has_generic_desc = not cand.get("description") or "captured on" in cand.get("description").lower() or cand.get("description") == "Photo from DSLR archive."
        
        if has_generic_title or has_generic_desc:
            title, story, location, category = get_location_and_story(filename, folder, date_str, cand["metadata"])
            # Update candidate details
            cand["title"] = title
            cand["description"] = story
            cand["location"] = location
            cand["category"] = category
            updated_captions += 1

    print(f"Updated/generated catchy captions and descriptions for {updated_captions} candidates.")

    # 5. Save back to curated_candidates.json
    with open(CURATED_JSON, "w") as f:
        json.dump(curated_candidates, f, indent=2)
    print(f"Saved {len(curated_candidates)} candidates to {CURATED_JSON}")

    # 6. Run sheet regeneration script
    print("Regenerating review sheet candidate_gallery.md...")
    import subprocess
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)

if __name__ == "__main__":
    main()
