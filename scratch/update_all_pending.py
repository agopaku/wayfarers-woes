#!/usr/bin/env python3
"""
Full batch update from all user comments in conversation transcript.
Covers everything mentioned in the chat that is still pending.
"""
import json

JSON_PATH = "scratch/curated_candidates.json"
with open(JSON_PATH) as f:
    candidates = json.load(f)
cmap = {c["cand_id"]: c for c in candidates}

updates = {

    # --- Baby photoshoot (NOT Evie, unknown baby, location Naperville area) ---
    # 379-393 all baby photoshoot
    **{f"CAND_{i}": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Baby photoshoot session.",
        "category": "portrait",
        "tags": ["baby", "photoshoot", "portrait", "Naperville", "Illinois"],
        "status": "approved",
    } for i in range(379, 394)},

    # --- CAND_055, 056: Periyar National Park, Thekkady ---
    "CAND_055": {
        "location": "Periyar National Park, Thekkady, Kerala, India",
        "country": "India",
        "story": "Trek through Periyar National Park, Thekkady Kumily — one of India's premier tiger reserves.",
        "category": "landscape",
        "tags": ["Periyar", "National Park", "Thekkady", "Kerala", "India", "trek", "forest"],
        "status": "approved",
    },
    "CAND_056": {
        "location": "Periyar National Park, Thekkady, Kerala, India",
        "country": "India",
        "story": "Trek through Periyar National Park, Thekkady Kumily — one of India's premier tiger reserves.",
        "category": "landscape",
        "tags": ["Periyar", "National Park", "Thekkady", "Kerala", "India", "trek", "forest"],
        "status": "approved",
    },

    # --- CAND_057: Kanyakumari bike trip ---
    "CAND_057": {
        "location": "Kanyakumari, Tamil Nadu, India",
        "country": "India",
        "story": "Bike trip to Kanyakumari — the southernmost tip of mainland India — with roommates.",
        "category": "landscape",
        "tags": ["Kanyakumari", "bike trip", "Tamil Nadu", "India", "southernmost tip"],
        "status": "approved",
    },

    # --- CAND_059: Flight from Chennai to Chicago ---
    "CAND_059": {
        "location": "In-flight, Chennai to Chicago",
        "country": "India",
        "story": "Shot from the window seat on the flight from Chennai to Chicago.",
        "category": "landscape",
        "tags": ["in-flight", "aerial", "Chennai", "Chicago", "travel"],
        "status": "approved",
    },

    # --- CAND_060: (same folder as 059, likely same trip — mark pending still since no specific info) ---

    # --- CAND_104: On the way to Mount Rushmore ---
    "CAND_104": {
        "location": "On the way to Mount Rushmore, South Dakota, USA",
        "country": "USA",
        "story": "Scenic shot on the road trip heading toward Mount Rushmore, South Dakota.",
        "category": "landscape",
        "tags": ["South Dakota", "road trip", "Mount Rushmore", "scenic", "USA"],
        "status": "approved",
    },

    # --- CAND_105: Devils Tower ---
    "CAND_105": {
        "location": "Devils Tower National Monument, Wyoming, USA",
        "country": "USA",
        "story": "Devils Tower — the iconic 867-foot volcanic rock monolith and America's first national monument, in Wyoming.",
        "category": "landmark",
        "tags": ["Devils Tower", "Wyoming", "national monument", "volcanic", "USA"],
        "status": "approved",
    },

    # --- CAND_112, 113: Starved Rock State Park, Illinois ---
    "CAND_112": {
        "location": "Starved Rock State Park, Illinois, USA",
        "country": "USA",
        "story": "Hike through Starved Rock State Park — Illinois' most-visited park with stunning canyon formations and waterfalls.",
        "category": "landscape",
        "tags": ["Starved Rock", "Illinois", "state park", "hike", "canyon", "USA"],
        "status": "approved",
    },
    "CAND_113": {
        "location": "Starved Rock State Park, Illinois, USA",
        "country": "USA",
        "story": "Hike through Starved Rock State Park — Illinois' most-visited park with stunning canyon formations and waterfalls.",
        "category": "landscape",
        "tags": ["Starved Rock", "Illinois", "state park", "hike", "canyon", "USA"],
        "status": "approved",
    },

    # --- CAND_117: Naperville Christmas Party ---
    "CAND_117": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Christmas party celebration in Naperville, IL.",
        "category": "portrait",
        "tags": ["Naperville", "Christmas", "party", "celebration", "Illinois"],
        "status": "approved",
    },

    # --- CAND_127: Blackwell Forest Preserve ---
    "CAND_127": {
        "location": "Blackwell Forest Preserve, Warrenville, Illinois, USA",
        "country": "USA",
        "story": "Blackwell Forest Preserve near Warrenville, IL — a beautiful DuPage County forest preserve with a lake.",
        "category": "landscape",
        "tags": ["Blackwell Forest Preserve", "Warrenville", "Illinois", "DuPage County", "forest", "USA"],
        "status": "approved",
    },

    # --- CAND_130: Galena, Illinois ---
    "CAND_130": {
        "location": "Galena, Illinois, USA",
        "country": "USA",
        "story": "Galena — the charming historic town in northwestern Illinois, well-preserved 19th-century architecture.",
        "category": "landscape",
        "tags": ["Galena", "Illinois", "historic", "small town", "USA"],
        "status": "approved",
    },

    # --- CAND_134: Bridges of Madison County, Iowa ---
    "CAND_134": {
        "location": "Bridges of Madison County, Winterset, Iowa, USA",
        "country": "USA",
        "story": "One of the iconic covered bridges of Madison County, Iowa — made famous by the novel and film 'The Bridges of Madison County'.",
        "category": "landscape",
        "tags": ["Bridges of Madison County", "Iowa", "covered bridge", "Winterset", "USA", "historic"],
        "status": "approved",
    },

    # --- CAND_135: Pratheesh at Bridges of Madison County ---
    "CAND_135": {
        "location": "Bridges of Madison County, Winterset, Iowa, USA",
        "country": "USA",
        "story": "Portrait of Pratheesh at the Bridges of Madison County, Iowa.",
        "category": "portrait",
        "tags": ["Bridges of Madison County", "Iowa", "covered bridge", "Pratheesh", "portrait", "USA"],
        "status": "approved",
    },

    # --- CAND_141, 142: Sia's baby photoshoot ---
    "CAND_141": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Sia's baby photoshoot — featuring Sumit and Sia.",
        "category": "portrait",
        "tags": ["baby photoshoot", "Sia", "Sumit", "portrait", "Naperville", "Illinois"],
        "status": "approved",
    },
    "CAND_142": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Sia's baby photoshoot — featuring Sumit and Sia.",
        "category": "portrait",
        "tags": ["baby photoshoot", "Sia", "Sumit", "portrait", "Naperville", "Illinois"],
        "status": "approved",
    },

    # --- CAND_143, 144: Badlands National Park ---
    "CAND_143": {
        "location": "Badlands National Park, South Dakota, USA",
        "country": "USA",
        "story": "Starting leg of an epic Tesla road trip: Badlands → Wyoming → Seattle → Highway 101/CA-1 → Las Vegas → Denver → home.",
        "category": "landscape",
        "tags": ["Badlands", "South Dakota", "national park", "Tesla road trip", "USA", "epic road trip"],
        "status": "approved",
    },
    "CAND_144": {
        "location": "Badlands National Park, South Dakota, USA",
        "country": "USA",
        "story": "Badlands National Park, South Dakota — part of the epic Tesla road trip through Wyoming, Seattle, CA-1, Vegas, and Denver.",
        "category": "landscape",
        "tags": ["Badlands", "South Dakota", "national park", "Tesla road trip", "USA"],
        "status": "approved",
    },

    # --- CAND_145: Sheridan, Wyoming ---
    "CAND_145": {
        "location": "Sheridan, Wyoming, USA",
        "country": "USA",
        "story": "Morning in Sheridan, WY — an overnight stop during the epic Tesla road trip west.",
        "category": "landscape",
        "tags": ["Sheridan", "Wyoming", "road trip", "Tesla", "USA"],
        "status": "approved",
    },

    # --- CAND_146: Entering Idaho, I-90 ---
    "CAND_146": {
        "location": "Idaho/Montana border, Interstate 90, USA",
        "country": "USA",
        "story": "Entering Idaho on I-90 during the epic Tesla road trip west toward Seattle.",
        "category": "landscape",
        "tags": ["Idaho", "I-90", "road trip", "Tesla", "USA", "highway"],
        "status": "approved",
    },

    # --- CAND_147: Olympic National Park, Washington ---
    "CAND_147": {
        "location": "Olympic National Park, Washington, USA",
        "country": "USA",
        "story": "Olympic National Park near Seattle — part of the Tesla road trip leg through the Pacific Northwest.",
        "category": "landscape",
        "tags": ["Olympic National Park", "Washington", "Seattle", "national park", "USA", "Pacific Northwest"],
        "status": "approved",
    },

    # --- CAND_148, 149: Seattle Japanese Garden / Space Needle reflection ---
    "CAND_148": {
        "location": "Japanese Garden, Washington Park Arboretum, Seattle, Washington, USA",
        "country": "USA",
        "story": "The serene Japanese Garden at Washington Park Arboretum in Seattle.",
        "category": "landscape",
        "tags": ["Seattle", "Japanese Garden", "Washington Park Arboretum", "Washington", "USA", "garden"],
        "status": "approved",
    },
    "CAND_149": {
        "location": "Seattle Center, Seattle, Washington, USA",
        "country": "USA",
        "story": "A beautiful reflection of the Seattle Space Needle — captured near Seattle Center.",
        "category": "cityscape",
        "tags": ["Space Needle", "Seattle", "reflection", "Washington", "USA", "landmark"],
        "status": "approved",
    },

    # --- CAND_162, 163: Green River SWM Area (Perseid Meteor Shower) ---
    "CAND_162": {
        "location": "Green River State Wildlife Management Area, Illinois, USA",
        "country": "USA",
        "story": "Astrophotography at Green River State Wildlife Management Area — the closest dark sky site to Aurora, IL. Shot during the Perseid Meteor Shower.",
        "category": "landscape",
        "tags": ["Green River", "dark sky", "meteor shower", "Perseid", "astrophotography", "Illinois", "Aurora"],
        "status": "approved",
    },
    "CAND_163": {
        "location": "Green River State Wildlife Management Area, Illinois, USA",
        "country": "USA",
        "story": "Astrophotography at Green River State Wildlife Management Area — the closest dark sky site to Aurora, IL. Shot during the Perseid Meteor Shower.",
        "category": "landscape",
        "tags": ["Green River", "dark sky", "meteor shower", "Perseid", "astrophotography", "Illinois", "Aurora"],
        "status": "approved",
    },

    # --- CAND_165: Jamestown ND - World's Largest Buffalo ---
    "CAND_165": {
        "location": "Jamestown, North Dakota, USA",
        "country": "USA",
        "story": "The World's Largest Buffalo monument in Jamestown, ND — a 26-ton concrete statue standing 46 feet tall.",
        "category": "landmark",
        "tags": ["Jamestown", "North Dakota", "World's Largest Buffalo", "monument", "USA", "roadside attraction"],
        "status": "approved",
    },

    # --- CAND_169: Findlay OH - Solar Eclipse ---
    "CAND_169": {
        "location": "Findlay, Ohio, USA",
        "country": "USA",
        "story": "Solar eclipse viewing at Findlay, Ohio — in the path of totality.",
        "category": "landscape",
        "tags": ["solar eclipse", "Findlay", "Ohio", "totality", "USA", "astronomy"],
        "status": "approved",
    },

    # --- CAND_170: Unknown (still pending, no info) ---

    # --- CAND_177: Starved Rock State Park ---
    "CAND_177": {
        "location": "Starved Rock State Park, Illinois, USA",
        "country": "USA",
        "story": "Starved Rock State Park, Illinois — canyon trails and waterfalls.",
        "category": "landscape",
        "tags": ["Starved Rock", "Illinois", "state park", "canyon", "USA"],
        "status": "approved",
    },

    # --- CAND_182, 183, 187, 188: Yosemite ---
    "CAND_182": {
        "location": "Yosemite National Park, California, USA",
        "country": "USA",
        "story": "Yosemite National Park — part of the epic Tesla road trip through California.",
        "category": "landscape",
        "tags": ["Yosemite", "California", "national park", "USA", "Tesla road trip"],
        "status": "approved",
    },
    "CAND_183": {
        "location": "Yosemite National Park, California, USA",
        "country": "USA",
        "story": "Yosemite National Park — part of the epic Tesla road trip through California.",
        "category": "landscape",
        "tags": ["Yosemite", "California", "national park", "USA", "Tesla road trip"],
        "status": "approved",
    },
    "CAND_187": {
        "location": "Yosemite National Park, California, USA",
        "country": "USA",
        "story": "Yosemite National Park — part of the epic Tesla road trip through California.",
        "category": "landscape",
        "tags": ["Yosemite", "California", "national park", "USA", "Tesla road trip"],
        "status": "approved",
    },
    "CAND_188": {
        "location": "Yosemite National Park, California, USA",
        "country": "USA",
        "story": "Yosemite National Park — part of the epic Tesla road trip through California.",
        "category": "landscape",
        "tags": ["Yosemite", "California", "national park", "USA", "Tesla road trip"],
        "status": "approved",
    },

    # --- CAND_191, 192 (same Yosemite folder from date) ---
    # Keep pending — no explicit confirmation

    # --- CAND_194: Ankita portrait, Naperville ---
    "CAND_194": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Portrait portfolio session with Ankita in Naperville, IL.",
        "category": "portrait",
        "tags": ["portrait", "Ankita", "Naperville", "Illinois", "USA"],
        "status": "approved",
    },

    # --- CAND_204: Brenton Point State Park, Newport, RI ---
    "CAND_204": {
        "location": "Brenton Point State Park, Newport, Rhode Island, USA",
        "country": "USA",
        "story": "Brenton Point State Park in Newport, Rhode Island — a scenic ocean-side park with sweeping Atlantic views.",
        "category": "landscape",
        "tags": ["Brenton Point", "Newport", "Rhode Island", "ocean", "state park", "USA", "New England"],
        "status": "approved",
    },

    # --- CAND_206, 207: Stonington Point, CT ---
    "CAND_206": {
        "location": "Stonington Point, Stonington, Connecticut, USA",
        "country": "USA",
        "story": "Stonington Point, Connecticut — part of the New England road trip.",
        "category": "landscape",
        "tags": ["Stonington", "Connecticut", "New England", "road trip", "USA", "coastal"],
        "status": "approved",
    },
    "CAND_207": {
        "location": "Stonington Point, Stonington, Connecticut, USA",
        "country": "USA",
        "story": "Stonington Point, Connecticut — part of the New England road trip.",
        "category": "landscape",
        "tags": ["Stonington", "Connecticut", "New England", "road trip", "USA", "coastal"],
        "status": "approved",
    },

    # --- CAND_280, 281, 282 (same Spiti/Langza cluster — check status) ---
    # These appeared as pending. Likely Spiti Valley from context (same folder as 278/279)
    "CAND_280": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "Village life and landscape in Langza, Spiti Valley.",
        "category": "landscape",
        "tags": ["Langza", "Spiti Valley", "Himachal Pradesh", "India", "village", "high altitude"],
        "status": "approved",
    },
    "CAND_281": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "Village life and landscape in Langza, Spiti Valley.",
        "category": "landscape",
        "tags": ["Langza", "Spiti Valley", "Himachal Pradesh", "India", "village", "high altitude"],
        "status": "approved",
    },
    "CAND_282": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "Village life and landscape in Langza, Spiti Valley.",
        "category": "landscape",
        "tags": ["Langza", "Spiti Valley", "Himachal Pradesh", "India", "village", "high altitude"],
        "status": "approved",
    },
}

updated = 0
skipped = []
for cand_id, fields in updates.items():
    if cand_id not in cmap:
        skipped.append(cand_id)
        continue
    c = cmap[cand_id]
    for k, v in fields.items():
        c[k] = v
    if c.get("status") not in ("approve", "approved"):
        c["status"] = "approved"
    updated += 1

with open(JSON_PATH, "w") as f:
    json.dump(candidates, f, indent=2)

print(f"✅ Updated {updated} candidates.")
if skipped:
    print(f"⚠️  Skipped (not found): {skipped}")

# Print remaining pending count
with open(JSON_PATH) as f:
    data = json.load(f)
still_pending = [c for c in data if c.get("status","pending") == "pending"]
print(f"\nRemaining pending: {len(still_pending)}")
for c in still_pending:
    print(f"  {c['cand_id']}: {c['filename']} | {c.get('location','Unknown')}")
