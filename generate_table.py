import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def is_external(url):
    return url.startswith('http://') or url.startswith('https://') or url.startswith('//')

def generate_markdown():
    broken_images = {}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
                meta_images = re.findall(r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
                meta_images2 = re.findall(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\']', content, re.IGNORECASE)
                
                all_images = set(img_srcs + meta_images + meta_images2)
                
                page_broken = set()
                for src in all_images:
                    if not src or is_external(src): continue
                    
                    if src.startswith('/'):
                        img_path = os.path.join('.', src[1:])
                    else:
                        img_path = os.path.normpath(os.path.join(root, src))
                        
                    if not os.path.exists(img_path):
                        page_broken.add(src)
                        
                if page_broken:
                    clean_path = filepath.replace('./', '/')
                    # Only include if it's a blog post (has no nested folders, or is under blog/)
                    # To simplify, we just show everything that has a broken image.
                    broken_images[clean_path] = list(page_broken)

    print("| Page URL path | Broken Image Reference(s) |")
    print("|--------------|-------------------------|")
    for page, imgs in sorted(broken_images.items()):
        formatted_imgs = "<br>".join(sorted(imgs))
        print(f"| `{page}` | `{formatted_imgs}` |")

if __name__ == '__main__':
    generate_markdown()
