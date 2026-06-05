import os
import json

HD_PICTURES_DIR = "/Volumes/Pictures/Pictures"
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

target_lower = {name.lower(): name for name in target_names}
found_mapping = {}

print("Scanning...")
for root, dirs, files in os.walk(HD_PICTURES_DIR):
    # Skip thumbnail/preview directories to speed up
    if any(p in root for p in ["ag-edits-thumbnails", "previews"]):
        continue
    for file in files:
        file_l = file.lower()
        if file_l in target_lower:
            found_mapping[file_l] = os.path.join(root, file)

print(f"Found {len(found_mapping)} of {len(target_names)} target files.")

# Save results
with open("scratch/found_scan_results.json", "w") as f:
    json.dump(found_mapping, f, indent=2)
print("Wrote results to scratch/found_scan_results.json")
