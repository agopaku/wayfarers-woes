import os
import time
from PIL import Image

def generate_iphone_thumbnails():
    base_dir = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
    src_dir = os.path.join(base_dir, "images/iphone")
    dest_dir = os.path.join(base_dir, "images/iphone-thumbnails")
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")
        
    start_time = time.time()
    generated_count = 0
    skipped_count = 0
    
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    print(f"Found {len(files)} files to process in images/iphone.")
    
    for filename in files:
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        # Skip if thumbnail already exists and is newer than source file
        if os.path.exists(dest_path) and os.path.getmtime(dest_path) > os.path.getmtime(src_path):
            skipped_count += 1
            continue
            
        try:
            with Image.open(src_path) as img:
                # Calculate thumbnail size maintaining aspect ratio
                max_size = 800
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Save as compressed JPEG
                img.save(dest_path, "JPEG", quality=85, optimize=True)
                generated_count += 1
                
                if generated_count % 10 == 0:
                    print(f"Processed {generated_count} images...")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
    elapsed = time.time() - start_time
    print(f"\nThumbnail generation finished in {elapsed:.2f} seconds!")
    print(f"Generated: {generated_count} iPhone thumbnails.")
    print(f"Skipped (already exist): {skipped_count} iPhone thumbnails.")

if __name__ == "__main__":
    generate_iphone_thumbnails()
