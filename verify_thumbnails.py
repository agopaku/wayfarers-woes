import os
import json

base_dir = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
src_dir = os.path.join(base_dir, "images/ag-edits")
dest_dir = os.path.join(base_dir, "images/ag-edits-thumbnails")
gallery_json = os.path.join(base_dir, "gallery.json")

errors = []

# Check that ag-edits-thumbnails folder exists
if not os.path.exists(dest_dir):
    errors.append(f"Directory does not exist: {dest_dir}")
else:
    # Get lists of files
    src_files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    dest_files = sorted([f for f in os.listdir(dest_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    print(f"Original ag-edits images: {len(src_files)}")
    print(f"Generated ag-edits-thumbnails: {len(dest_files)}")
    
    if len(src_files) != len(dest_files):
        errors.append(f"Count mismatch: {len(src_files)} source files vs {len(dest_files)} thumbnails.")
        
    # Check that all source files have a matching thumbnail
    missing = []
    for f in src_files:
        if f not in dest_files:
            missing.append(f)
            
    if missing:
        errors.append(f"Missing thumbnails for files: {missing[:5]}")
        
    # Check average file size of thumbnails
    sizes = [os.path.getsize(os.path.join(dest_dir, f)) for f in dest_files]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    max_size = max(sizes) if sizes else 0
    
    print(f"Average thumbnail size: {avg_size/1024:.2f} KB")
    print(f"Max thumbnail size: {max_size/1024:.2f} KB")
    
    if avg_size > 200 * 1024:
        errors.append(f"Average thumbnail size is too large: {avg_size/1024:.2f} KB")
        
# Check that index.html and gallery.html references remain correct
js_path = os.path.join(base_dir, "gallery-page.js")
with open(js_path, "r") as f:
    js = f.read()
if "images/ag-edits-thumbnails/" not in js:
    errors.append("gallery-page.js does not seem to replace image paths with thumbnail paths.")
else:
    print("✓ gallery-page.js includes thumbnail replacement logic.")

if len(errors) == 0:
    print("\nALL THUMBNAIL VERIFICATION CHECKS PASSED SUCCESSFULLY! ✓✓✓")
else:
    print("\nFOUND ERRORS DURING THUMBNAIL VERIFICATION:")
    for err in errors:
        print(f"✗ {err}")
    exit(1)
