import os
from PIL import Image

def verify():
    base_dir = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
    src_dir = os.path.join(base_dir, "images/ag-edits")
    
    errors = []
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    print(f"Verifying {len(files)} optimized images...")
    
    for filename in files:
        src_path = os.path.join(src_dir, filename)
        size = os.path.getsize(src_path)
        
        # Check size is reasonable (e.g. less than 1.5MB)
        if size > 1.5 * 1024 * 1024:
            errors.append(f"Image {filename} is too large: {size/(1024*1024):.2f} MB")
            
        try:
            with Image.open(src_path) as img:
                width, height = img.size
                
                # Check dimensions
                if max(width, height) > 2048:
                    errors.append(f"Image {filename} exceeds 2048px: {width}x{height}")
                    
                # Check EXIF segment
                exif = img.getexif()
                # Check if getexif has attributes, or exif data exists in img.info
                has_exif = len(exif) > 0 or img.info.get('exif') is not None
                if not has_exif:
                    errors.append(f"Image {filename} has no EXIF data.")
        except Exception as e:
            errors.append(f"Failed to open/parse {filename}: {e}")
            
    # Check directory weight
    total_size = sum(os.path.getsize(os.path.join(src_dir, f)) for f in files)
    print(f"Total directory size: {total_size/(1024*1024):.2f} MB")
    
    if len(errors) == 0:
        print("\nALL OPTIMIZATION VERIFICATION CHECKS PASSED SUCCESSFULLY! ✓✓✓")
        print("All images are <= 2048px, under 1.5MB, and EXIF metadata is preserved!")
    else:
        print("\nFOUND ERRORS DURING VERIFICATION:")
        for err in errors:
            print(f"✗ {err}")
        exit(1)

if __name__ == "__main__":
    verify()
