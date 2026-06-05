#!/usr/bin/env python3
"""
Batch update script for confirmed locations from user input.
Covers: Green River (meteor shower), Land Between the Lakes, Illickal Kallu,
Michigan fall colors (Harbor Springs), Goa, Naperville, Spiti Valley villages,
Chicago, San Francisco, Great Smokies, Arkansas, Las Vegas, Grand Canyon, etc.
"""

import json
import sys

JSON_PATH = "scratch/curated_candidates.json"

with open(JSON_PATH) as f:
    candidates = json.load(f)

cmap = {c["cand_id"]: c for c in candidates}

updates = {
    # --- Green River SWM Area – Meteor Shower ---
    "CAND_242": {
        "location": "Green River State Wildlife Management Area, Kentucky",
        "country": "USA",
        "story": "Captured during a meteor shower expedition at Green River State Wildlife Management Area.",
        "category": "landscape",
        "tags": ["meteor shower", "night sky", "astrophotography", "Kentucky", "Green River"],
    },
    "CAND_375": {
        "location": "Green River State Wildlife Management Area, Kentucky",
        "country": "USA",
        "story": "Captured during a meteor shower expedition at Green River State Wildlife Management Area.",
        "category": "landscape",
        "tags": ["meteor shower", "night sky", "astrophotography", "Kentucky", "Green River"],
    },

    # --- Land Between the Lakes ---
    "CAND_243": {
        "location": "Land Between the Lakes, Kentucky/Tennessee",
        "country": "USA",
        "story": "Landscape from the Land Between the Lakes National Recreation Area, a unique peninsula between Lake Barkley and Kentucky Lake.",
        "category": "landscape",
        "tags": ["Land Between the Lakes", "national recreation area", "Kentucky", "Tennessee", "lake"],
    },

    # --- Illickal Kallu, Kerala ---
    "CAND_244": {
        "location": "Illickal Kallu, Kerala, India",
        "country": "India",
        "story": "Scenic landscape at Illickal Kallu (Illickal Rock), a popular trekking destination in Idukki district, Kerala.",
        "category": "landscape",
        "tags": ["Illickal Kallu", "Kerala", "trekking", "Western Ghats", "India"],
    },
    "CAND_245": {
        "location": "Illickal Kallu, Kerala, India",
        "country": "India",
        "story": "Scenic view at Illickal Kallu (Illickal Rock) in Kerala's Western Ghats.",
        "category": "landscape",
        "tags": ["Illickal Kallu", "Kerala", "trekking", "Western Ghats", "India"],
    },

    # --- Gift from Ranjith ---
    "CAND_246": {
        "location": "India",
        "country": "India",
        "story": "A gift from travel buddy Ranjith, commemorating all the trips done together in India.",
        "category": "other",
        "tags": ["gift", "friendship", "travel memories", "India", "Ranjith"],
    },

    # --- Michigan Fall Colors – Harbor Springs ---
    "CAND_247": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_248": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_249": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_250": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_251": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_252": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "Fall foliage colors during a Michigan road trip near Harbor Springs.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage"],
    },
    "CAND_378": {
        "location": "Harbor Springs, Michigan, USA",
        "country": "USA",
        "story": "A farmhouse nestled amid brilliant fall foliage along a lake near Harbor Springs, Michigan.",
        "category": "landscape",
        "tags": ["fall colors", "autumn", "Michigan", "Harbor Springs", "foliage", "farmhouse", "lake"],
    },

    # --- Goa – Shweta ---
    "CAND_253": {
        "location": "Goa, India",
        "country": "India",
        "story": "Portrait of Shweta in Goa, India.",
        "category": "portrait",
        "tags": ["Goa", "India", "portrait", "Shweta"],
    },

    # --- Naperville – Evie, Christmas ---
    "CAND_257": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Evie at a Christmas celebration in Naperville, Illinois.",
        "category": "portrait",
        "tags": ["Naperville", "Christmas", "celebration", "Evie", "Illinois"],
    },
    "CAND_270": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Portrait of Evie in Naperville, Illinois.",
        "category": "portrait",
        "tags": ["Naperville", "Evie", "portrait", "Illinois"],
    },
    "CAND_272": {
        "location": "Naperville, Illinois, USA",
        "country": "USA",
        "story": "Portrait of Evie in Naperville, Illinois.",
        "category": "portrait",
        "tags": ["Naperville", "Evie", "portrait", "Illinois"],
    },

    # --- Spiti Valley / Hikkim ---
    "CAND_273": {
        "location": "Hikkim, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "At Hikkim, home to the world's highest post office at 14,567 ft (4,440 m) above sea level.",
        "category": "landscape",
        "tags": ["Hikkim", "Spiti Valley", "world's highest post office", "Himachal Pradesh", "India", "altitude"],
    },
    "CAND_274": {
        "location": "Hikkim, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "At Hikkim, home to the world's highest post office at 14,567 ft (4,440 m) above sea level.",
        "category": "landscape",
        "tags": ["Hikkim", "Spiti Valley", "world's highest post office", "Himachal Pradesh", "India", "altitude"],
    },
    "CAND_275": {
        "location": "Hikkim, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "At Hikkim, home to the world's highest post office at 14,567 ft (4,440 m) above sea level.",
        "category": "landscape",
        "tags": ["Hikkim", "Spiti Valley", "world's highest post office", "Himachal Pradesh", "India", "altitude"],
    },
    "CAND_276": {
        "location": "Hikkim, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "At Hikkim, home to the world's highest post office at 14,567 ft (4,440 m) above sea level.",
        "category": "landscape",
        "tags": ["Hikkim", "Spiti Valley", "world's highest post office", "Himachal Pradesh", "India", "altitude"],
    },

    # --- Langza Homestay (already approved but update story if needed) ---
    "CAND_277": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "The warm host lady of our Tangzi Homestay in Langza village, Spiti Valley.",
        "category": "portrait",
        "tags": ["Langza", "Spiti Valley", "homestay", "Tangzi", "portrait", "Himachal Pradesh"],
    },

    # --- Langza village ceremony ---
    "CAND_278": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "A traditional village gathering in Langza — a Buddhist exorcism ceremony where the lama priest performed rituals to ward off evil spirits from a village member. The 30–45 minute ceremony concluded with the distribution of 'Chhang' (locally brewed barley alcohol), which the community calls 'Theertham' — reflecting the beautiful blend of Buddhist and folk traditions in Spiti.",
        "category": "street",
        "tags": ["Langza", "Spiti Valley", "ceremony", "village", "exorcism", "Buddhist ritual", "Chhang", "Himachal Pradesh"],
    },
    "CAND_279": {
        "location": "Langza, Spiti Valley, Himachal Pradesh, India",
        "country": "India",
        "story": "A traditional village gathering in Langza — a Buddhist exorcism ceremony where the lama priest performed rituals to ward off evil spirits from a village member. The 30–45 minute ceremony concluded with the distribution of 'Chhang' (locally brewed barley alcohol), which the community calls 'Theertham' — reflecting the beautiful blend of Buddhist and folk traditions in Spiti.",
        "category": "street",
        "tags": ["Langza", "Spiti Valley", "ceremony", "village", "exorcism", "Buddhist ritual", "Chhang", "Himachal Pradesh"],
    },

    # --- Willis Tower – Chicago ---
    "CAND_320": {
        "location": "Willis Tower (Skydeck), Chicago, Illinois, USA",
        "country": "USA",
        "story": "Sunset view of Chicago's western suburbs from the Skydeck at Willis Tower. The perfectly straight grid of city streets radiates to the horizon, with Lake Michigan visible to the left and snow on the ground below.",
        "category": "cityscape",
        "tags": ["Willis Tower", "Skydeck", "Chicago", "sunset", "cityscape", "aerial", "Illinois", "winter"],
    },

    # --- Lake Geneva ---
    "CAND_324": {
        "location": "Lake Geneva, Wisconsin, USA",
        "country": "USA",
        "story": "Scenic views along Lake Geneva, a charming resort town in southern Wisconsin.",
        "category": "landscape",
        "tags": ["Lake Geneva", "Wisconsin", "lake", "scenic", "USA"],
    },

    # --- Mount Rushmore ---
    "CAND_325": {
        "location": "Mount Rushmore National Memorial, Keystone, South Dakota, USA",
        "country": "USA",
        "story": "An atmospheric view of Mount Rushmore from the approach highway, shrouded in soft morning mist. The four presidential faces of Washington, Jefferson, Roosevelt, and Lincoln are carved into the granite of the Black Hills.",
        "category": "landmark",
        "tags": ["Mount Rushmore", "South Dakota", "national memorial", "presidents", "Black Hills", "Keystone"],
    },

    # --- San Francisco Boat Tour ---
    "CAND_326": {
        "location": "San Francisco Bay, California, USA",
        "country": "USA",
        "story": "Views from a boat tour of San Francisco Bay.",
        "category": "landscape",
        "tags": ["San Francisco", "bay", "boat tour", "California", "Golden Gate"],
    },
    "CAND_327": {
        "location": "San Francisco Bay, California, USA",
        "country": "USA",
        "story": "Views from a boat tour of San Francisco Bay.",
        "category": "landscape",
        "tags": ["San Francisco", "bay", "boat tour", "California", "Golden Gate"],
    },
    "CAND_328": {
        "location": "San Francisco Bay, California, USA",
        "country": "USA",
        "story": "Views from a boat tour of San Francisco Bay.",
        "category": "landscape",
        "tags": ["San Francisco", "bay", "boat tour", "California", "Golden Gate"],
    },

    # --- Charlies Bunion hike – Great Smokies ---
    "CAND_332": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_333": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_334": {
        "location": "Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Our Airbnb cabin nestled in the Great Smoky Mountains — a cozy base for exploring the Smokies.",
        "category": "landscape",
        "tags": ["Great Smoky Mountains", "Airbnb", "cabin", "Tennessee", "national park"],
    },
    "CAND_335": {
        "location": "Tail of the Dragon (US-129), Deals Gap, Tennessee/North Carolina, USA",
        "country": "USA",
        "story": "The legendary Tail of the Dragon — 318 curves in 11 miles on US-129 at Deals Gap, one of America's most famous driving roads in the Smokies.",
        "category": "landscape",
        "tags": ["Tail of the Dragon", "US-129", "Deals Gap", "Great Smokies", "driving", "road trip"],
    },
    "CAND_336": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_347": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_348": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_350": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_361": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_365": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },
    "CAND_366": {
        "location": "Charlie's Bunion, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "Views from the Charlie's Bunion hike along the Appalachian Trail in Great Smoky Mountains National Park.",
        "category": "landscape",
        "tags": ["Charlie's Bunion", "Great Smoky Mountains", "hiking", "Appalachian Trail", "Tennessee", "national park"],
    },

    # --- Arkansas Bike Trip / White Rock Mountain ---
    "CAND_338": {
        "location": "White Rock Mountain, Ozark National Forest, Arkansas, USA",
        "country": "USA",
        "story": "A scenic bike trip through White Rock Mountain in the Ozark National Forest, Arkansas.",
        "category": "landscape",
        "tags": ["White Rock Mountain", "Arkansas", "bike trip", "Ozark National Forest", "scenic"],
    },

    # --- Cades Cove – Smokies ---
    "CAND_373": {
        "location": "Cades Cove, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "The scenic 11-mile Cades Cove loop drive in Great Smoky Mountains National Park — a valley with historic homesteads and abundant wildlife.",
        "category": "landscape",
        "tags": ["Cades Cove", "Great Smoky Mountains", "scenic loop", "Tennessee", "national park", "valley"],
    },
    "CAND_374": {
        "location": "Cades Cove, Great Smoky Mountains National Park, Tennessee, USA",
        "country": "USA",
        "story": "The scenic 11-mile Cades Cove loop drive in Great Smoky Mountains National Park — a valley with historic homesteads and abundant wildlife.",
        "category": "landscape",
        "tags": ["Cades Cove", "Great Smoky Mountains", "scenic loop", "Tennessee", "national park", "valley"],
    },

    # --- Grand Canyon Panoramic ---
    "CAND_376": {
        "location": "Grand Canyon National Park, Arizona, USA",
        "country": "USA",
        "story": "A sweeping panoramic view of the Grand Canyon — one of Earth's most awe-inspiring natural wonders.",
        "category": "landscape",
        "tags": ["Grand Canyon", "Arizona", "panorama", "national park", "canyon", "landscape"],
    },

    # --- Bike Trip – Valparai Ghat Road (South India) ---
    "CAND_293": {
        "location": "Valparai Ghat Road, Anamalai Hills, Tamil Nadu, India",
        "country": "India",
        "story": "A moody monsoon portrait on a Royal Enfield motorcycle on the misty Valparai ghat road (TN-11 registered bike — Coimbatore), deep in the Western Ghats forest during the June 2015 bike trip.",
        "category": "portrait",
        "tags": ["bike trip", "Royal Enfield", "Tamil Nadu", "Western Ghats", "monsoon", "Valparai", "motorcycle", "India"],
    },
    "CAND_294": {
        "location": "Valparai Ghat Road, Anamalai Hills, Tamil Nadu, India",
        "country": "India",
        "story": "Bike trip through the dramatic Valparai ghat road in the Anamalai Hills, Tamil Nadu during the 2015 monsoon.",
        "category": "landscape",
        "tags": ["bike trip", "Tamil Nadu", "Western Ghats", "monsoon", "Valparai", "motorcycle", "India", "ghat road"],
    },
    "CAND_295": {
        "location": "Valparai Ghat Road (Loam's View Point), Anamalai Hills, Tamil Nadu, India",
        "country": "India",
        "story": "An aerial view of the spectacular Valparai ghat road with 40 numbered hairpin bends winding down the Anamalai Hills toward the Aliyar reservoir visible in the valley below. Shot from near Loam's View Point during the June 2015 bike trip.",
        "category": "landscape",
        "tags": ["Valparai", "ghat road", "hairpin bends", "Anamalai Hills", "Tamil Nadu", "Aliyar reservoir", "Western Ghats", "India", "aerial", "switchbacks"],
    },
}

updated_count = 0
skipped = []
for cand_id, fields in updates.items():
    if cand_id not in cmap:
        skipped.append(cand_id)
        continue
    c = cmap[cand_id]
    for key, val in fields.items():
        c[key] = val
    if c.get("status") != "approved":
        c["status"] = "approved"
    updated_count += 1

with open(JSON_PATH, "w") as f:
    json.dump(candidates, f, indent=2)

print(f"✅ Updated {updated_count} candidates.")
if skipped:
    print(f"⚠️  Skipped (not found): {skipped}")
