import os
import json
import subprocess

BASE_DIR = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
CURATED_JSON = os.path.join(BASE_DIR, "scratch/curated_candidates.json")

def generate_story(cand):
    title = cand.get("title", "").strip()
    desc = cand.get("description", "").strip()
    loc = cand.get("location", "").strip()
    folder = cand.get("folder", "").strip()
    filename = cand.get("filename", "").strip()
    cat = cand.get("category", "").strip()
    
    # Clean up title/desc if they match default placeholders
    if desc == "A beautiful frame captured in our archives.":
        desc = ""
    
    # 1. Custom overrides for specific candidates to make them feel highly authentic
    if "CAND_002" in cand["cand_id"]:
        return "Gearing up for Day 1 of the epic motorcycle ride from Trivandrum all the way to Agumbe. The Royal Enfield Desert Storm felt ready for the miles ahead."
    
    # Kinnaur/Spiti specific stories
    if "Kinnaur" in loc or "Spiti" in loc:
        if "Chitkul" in loc:
            return "Waking up to this breathtaking view in Chitkul, the last inhabited village near the border. Hot chai and snow-capped peaks made for the perfect morning."
        if "Charang" in loc:
            if "Monastery" in title or "Temple" in title:
                return "The quiet serenity of the ancient Rangrik Shungma temple in Charang. There is a deep, timeless spiritual energy that fills this high-altitude valley."
            return "Walking through the narrow paths of Charang village, surrounded by high-altitude farmlands and towering dry peaks."
        if "Dhankar" in loc:
            return "The challenging hike up to Dhankar Lake was grueling at high altitude, but standing by the calm waters surrounded by barren peaks made every step worth it."
        if "Chandratal" in loc:
            return "Reaching the mystical Chandratal Lake (the Lake of the Moon) after trekking through Spiti's rugged terrain. The water's deep blue hue was mesmerising."
        if "Kunzum" in loc:
            return "Crossing the mighty Kunzum Pass at 15,000 feet, where colorful prayer flags flutter wildly against the backdrop of massive glaciers."
        if "Stream" in title or "water" in desc.lower():
            return "Listening to the rush of a glacier-fed stream cutting through the rocky valley of Kinnaur under the warm sun."
        if "portrait" in cat:
            return "Meeting the incredibly warm and resilient locals of the high Himalayas, whose smiles are as unforgettable as the mountain landscapes."
        
        # Default Kinnaur/Spiti story
        return f"Navigating the legendary cliffhanger roads and deep gorges of {loc.split(',')[0]} during our high-altitude Himalayan expedition."

    # Badlands / South Dakota
    if "Badlands" in loc:
        return "Watching the sun go down over the rugged, layered ridges of the Badlands. The soft evening light brought out the vibrant colors of the ancient rock formations."
    
    # Lake Superior / Duluth winter trip
    if "Duluth" in loc or "Lake Superior" in loc:
        if "Sea Smoke" in title or "smoke" in desc.lower():
            return "Stepping out onto the shore to witness sea smoke rising from the freezing waters of Lake Superior—a magical sight on a morning that dipped below -30°F."
        if "pier" in desc.lower() or "lighthouse" in desc.lower() or "Canal Park" in loc:
            return "The pier at Canal Park was completely encased in thick, glassy sheets of ice, sculpted by the freezing lake spray and relentless winds."
        return "Exploring the freezing shores of Lake Superior in winter. The cold was biting and intense, but the serene ice formations were absolutely beautiful."

    # Devil's Lake
    if "Devil's Lake" in loc:
        return "Hiking the rocky bluffs of Devil's Lake State Park. Climbing up the ancient quartzite boulders rewarded us with a panoramic view of the lake nestled below."

    # Monroe / Balloon
    if "Monroe" in loc:
        if "balloon" in desc.lower() or "Balloon" in title:
            return "Watching colorful hot air balloons inflate and drift gracefully over the green hills of Monroe during the summer festival."
        return "A beautiful summer day exploring the scenic, rolling landscapes of green Monroe County."

    # Upper Peninsula Michigan / Pictured Rocks
    if "Pictured Rocks" in loc or "Upper Peninsula" in loc:
        if "falls" in desc.lower() or "Falls" in title:
            return "Hiking through the dense forest of the Upper Peninsula to find the peaceful, hidden cascade of Mosquito Falls."
        return "Standing on the rugged sandstone cliffs of Pictured Rocks, looking out over the vast, ocean-like waters of Lake Superior."

    # Great Smoky Mountains
    if "Smoky Mountains" in loc or "Smokies" in loc or "Charlies Bunion" in loc or "Gatlinburg" in loc:
        if "Charlies Bunion" in loc or "Bunion" in title:
            return "Standing on the exposed rock face of Charlies Bunion along the Appalachian Trail, surrounded by the signature blue mist of the Smokies."
        return "Driving through the winding roads of the Great Smoky Mountains, watching the morning fog cling to the dense autumn valleys."

    # Rhode Island / Newport
    if "Rhode Island" in loc or "Newport" in loc:
        return "Enjoying a quiet walk along the scenic Newport coastline, feeling the refreshing breeze off the Atlantic Ocean as the sun dipped low."

    # California / San Francisco / Yosemite / Highway 1
    if "San Francisco" in loc or "Golden Gate" in loc or "SFO" in loc:
        if "Golden Gate" in loc or "Bridge" in title:
            return "Catching the golden hour light hitting the iconic spans of the Golden Gate Bridge, with a blanket of fog rolling in from the bay."
        if "Cemetery" in loc:
            return "A solemn, quiet moment walking through the historic San Francisco National Cemetery overlooking the bay."
        return "Exploring the vibrant streets and hills of San Francisco, capturing the unique architecture and dynamic energy of the city."

    if "Highway 1" in loc or "Big Sur" in loc:
        return "Cruising along the cliffside curves of Highway 1, looking down at the wild Pacific waves crashing against the rocky shores of Big Sur."

    if "Lake Tahoe" in loc:
        return "Taking in the incredible clarity of Lake Tahoe, surrounded by towering pine trees and snow-capped Sierra Nevada peaks."

    if "Yosemite" in loc:
        return "Standing in awe of Yosemite's massive granite walls and cascading waterfalls, feeling small in one of nature's greatest cathedrals."

    # Yellowstone / Grand Teton
    if "Yellowstone" in loc or "Mammoth Hot Springs" in loc or "Teton" in loc:
        if "Jenny Lake" in loc or "Jenny" in title:
            return "Watching the early morning mist rise off Jenny Lake, with the jagged peaks of the Grand Tetons reflecting in the calm water."
        if "Mammoth Hot Springs" in loc:
            return "Walking along the wooden boardwalks of Mammoth Hot Springs, marveling at the colorful geothermal terraces sculpted by active springs."
        return "Exploring the surreal geothermal landscapes of Yellowstone, where steam rises from deep vents and colorful pools dot the caldera floor."

    # Maine / New England
    if "Ogunquit" in loc or "Lobster Point" in loc or "Maine" in loc or "Bug Light" in loc:
        return f"A serene winter coastal walk by {loc.split(',')[0]}, watching the cold waves lap against the rocky New England shoreline."

    # Fall colors Michigan
    if "Michigan" in loc and "fall" in folder:
        return "Taking a scenic autumn drive through northern Michigan, mesmerised by the brilliant reds, oranges, and yellows canopying the roadway."

    # If we have a decent description, we can rephrase it slightly to sound like a story
    if desc:
        # Rephrase / format desc as story
        story = desc
        if not story.endswith("."):
            story += "."
        return story

    # General fallback based on title/category
    if "portrait" in cat:
        return f"A candid portrait captured during our travels in {loc or 'the archives'}, preserving a fleeting moment and connection."
    return f"A beautiful perspective captured during our travels to {loc or 'various destinations'}, documenting the spirit of exploration."

with open(CURATED_JSON, "r") as f:
    candidates = json.load(f)

updated_count = 0
for cand in candidates:
    if cand.get("status") == "approve" and not cand.get("story", "").strip():
        story = generate_story(cand)
        cand["story"] = story
        updated_count += 1

print(f"Generated stories for {updated_count} approved candidates.")

if updated_count > 0:
    with open(CURATED_JSON, "w") as f:
        json.dump(candidates, f, indent=2)
    print("Successfully saved updated candidates to curated_candidates.json")
    
    # Run sheet regeneration
    regen_script = os.path.join(BASE_DIR, "scratch/regenerate_review_sheet.py")
    res = subprocess.run(["python3", regen_script], capture_output=True, text=True)
    print("Regenerate Sheet stdout:", res.stdout)
    if res.stderr:
        print("Regenerate Sheet stderr:", res.stderr)
else:
    print("No candidates needed story generation.")
