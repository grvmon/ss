#!/usr/bin/env python3
"""
Image optimization script:
- Upscales small offering images to 900px wide (Lanczos)
- Converts all target images to WebP at quality 85
- Caps large images at 1280px wide
- Skips logos and vector-style PNGs
"""

import sys
import os
sys.path.insert(0, '/Users/preetimishra/Library/Python/3.9/lib/python/site-packages')

from PIL import Image

ASSETS = os.path.dirname(os.path.abspath(__file__))

# (source_filename, target_webp_name, min_width_to_upscale, max_width)
IMAGES = [
    # Offering cards — small, need upscale to 900px
    ("business_storage_new.png", "business_storage_new.webp", 900, 900),
    ("home_storage_new.png",     "home_storage_new.webp",     900, 900),
    ("luggage_storage_new.png",  "luggage_storage_new.webp",  900, 900),
    # Location section
    ("dwarka_storage.png",       "dwarka_storage.webp",       None, 1280),
    ("gurugram_storage.png",     "gurugram_storage.webp",     None, 1280),
    ("noida_storage.png",        "noida_storage.webp",        None, 1280),
    # Gallery / facility
    ("facility_1.jpg",           "facility_1.webp",           None, 1280),
    ("facility_2.jpg",           "facility_2.webp",           None, 1280),
    ("facility_3.jpg",           "facility_3.webp",           None, 1280),
    ("facility_4.jpg",           "facility_4.webp",           None, 1280),
    ("gurugram_clean_corridor_enhanced.jpg", "gurugram_clean_corridor_enhanced.webp", None, 1280),
    # Testimonial avatars — keep at 200px (they're tiny circles)
    ("client_nitin.jpg",   "client_nitin.webp",   None, 200),
    ("client_nandini.jpg", "client_nandini.webp", None, 200),
    ("client_roselin.jpg", "client_roselin.webp", None, 200),
]

def process(src, dst, force_width, max_width):
    src_path = os.path.join(ASSETS, src)
    dst_path = os.path.join(ASSETS, dst)
    if not os.path.exists(src_path):
        print(f"  SKIP (not found): {src}")
        return

    img = Image.open(src_path).convert("RGB")
    orig_w, orig_h = img.size

    # Determine target width
    if force_width:
        target_w = force_width
    elif max_width and orig_w > max_width:
        target_w = max_width
    else:
        target_w = orig_w

    # Scale height proportionally
    target_h = int(orig_h * target_w / orig_w)

    if (target_w, target_h) != (orig_w, orig_h):
        img = img.resize((target_w, target_h), Image.LANCZOS)
        print(f"  {src}: {orig_w}x{orig_h} → {target_w}x{target_h}")
    else:
        print(f"  {src}: {orig_w}x{orig_h} (no resize)")

    img.save(dst_path, "WEBP", quality=85, method=6)
    src_size = os.path.getsize(src_path)
    dst_size = os.path.getsize(dst_path)
    saved = (src_size - dst_size) / src_size * 100
    print(f"    {src_size//1024}KB → {dst_size//1024}KB ({saved:.0f}% smaller) ✓ {dst}")

print("=== Optimizing & converting to WebP ===\n")
for src, dst, force_w, max_w in IMAGES:
    process(src, dst, force_w, max_w)

print("\n=== Done ===")
