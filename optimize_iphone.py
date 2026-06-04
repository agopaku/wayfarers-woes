import os
import time
from PIL import Image

def optimize_iphone_photos():
    base_dir = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog"
    src_dir = os.path.join(base_dir, "images/iphone")
    
    start_time = time.time()
    processed_count = 0
    total_original_size = 0
    total_new_size = 0
    
    if not os.path.exists(src_dir):
        print(f"Directory {src_dir} does not exist.")
        return
        
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
    print(f"Found {len(files)} iPhone photos to optimize in images/iphone.")
    
    for filename in files:
        src_path = os.path.join(src_dir, filename)
        orig_size = os.path.getsize(src_path)
        total_original_size += orig_size
        
        try:
            exif_data = None
            # Open and read EXIF first
            with Image.open(src_path) as img:
                exif_data = img.info.get('exif')
                
                # Check current dimensions
                width, height = img.size
                if max(width, height) <= 2048:
                    # Skip if already optimized
                    total_new_size += orig_size
                    continue
                
                # Resize keeping aspect ratio
                img.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
                
                # Temporary save path to avoid data loss on crash
                temp_path = src_path + ".tmp"
                if exif_data:
                    img.save(temp_path, "JPEG", quality=85, optimize=True, exif=exif_data)
                else:
                    img.save(temp_path, "JPEG", quality=85, optimize=True)
            
            # Swap temp file to original file
            os.replace(temp_path, src_path)
            
            new_size = os.path.getsize(src_path)
            total_new_size += new_size
            processed_count += 1
            
            if processed_count % 5 == 0:
                print(f"Optimized {processed_count} images...")
                
        except Exception as e:
            print(f"Error optimizing {filename}: {e}")
            if os.path.exists(src_path + ".tmp"):
                os.remove(src_path + ".tmp")
                
    elapsed = time.time() - start_time
    saved_bytes = total_original_size - total_new_size
    print(f"\nOptimization completed in {elapsed:.2f} seconds!")
    print(f"Optimized: {processed_count} files.")
    print(f"Original directory weight: {total_original_size / (1024*1024):.2f} MB")
    print(f"New directory weight: {total_new_size / (1024*1024):.2f} MB")
    if total_original_size > 0:
        print(f"Space saved: {saved_bytes / (1024*1024):.2f} MB ({(saved_bytes / total_original_size)*100:.1f}% reduction)")

if __name__ == "__main__":
    optimize_iphone_photos()
