import os
import re
from urllib.parse import urlparse

# Directories/files to skip
SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def is_external(url):
    return url.startswith('http://') or url.startswith('https://') or url.startswith('//')

def check_images():
    broken_images = {} # {page_path: [broken_img_1, broken_img_2]}
    total_pages = 0
    total_images = 0

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                total_pages += 1
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Find all img src attributes
                img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
                
                # Find all og:image or twitter:image attributes
                meta_images = re.findall(r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
                meta_images2 = re.findall(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\']', content, re.IGNORECASE)
                
                all_images = set(img_srcs + meta_images + meta_images2)
                
                for src in all_images:
                    if not src: continue
                    total_images += 1
                    
                    if is_external(src):
                        continue # Skip checking external URLs for now
                        
                    # Handle root-relative paths like /assets/logo.png
                    if src.startswith('/'):
                        # Assuming root is the current directory
                        img_path = os.path.join('.', src[1:])
                    else:
                        # Handle relative paths like ../assets/logo.png or assets/logo.png
                        img_path = os.path.normpath(os.path.join(root, src))
                        
                    if not os.path.exists(img_path):
                        if filepath not in broken_images:
                            broken_images[filepath] = set()
                        broken_images[filepath].add(src)

    print(f"Total Pages Checked: {total_pages}")
    print(f"Total Images Checked: {total_images}")
    print("---BROKEN IMAGES---")
    for page, imgs in broken_images.items():
        print(f"PAGE: {page}")
        for img in imgs:
            print(f"  BROKEN: {img}")

if __name__ == '__main__':
    check_images()
