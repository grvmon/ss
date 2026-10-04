import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}
FALLBACK_IMG = 'Storage-Room-Design-Ideas-for-a-Well-Organized-Home-.webp'

def is_external(url):
    return url.startswith('http://') or url.startswith('https://') or url.startswith('//')

def fix_images():
    fixed_count = 0
    files_modified = 0
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Find all images
                all_refs = re.findall(r'=["\']([^"\']+\.(?:png|jpg|jpeg|webp))["\']', content, re.IGNORECASE)
                
                for ref in set(all_refs):
                    if is_external(ref): continue
                    
                    if ref.startswith('/'):
                        img_path = os.path.join('.', ref[1:])
                    else:
                        img_path = os.path.normpath(os.path.join(root, ref))
                        
                    if not os.path.exists(img_path):
                        # If it's a blog asset, replace with fallback
                        if 'assets/blog/' in ref:
                            new_ref = ref[:ref.rindex('/') + 1] + FALLBACK_IMG
                            content = content.replace(f'"{ref}"', f'"{new_ref}"')
                            content = content.replace(f"'{ref}'", f"'{new_ref}'")
                            fixed_count += 1
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Fixed {fixed_count} remaining broken image references across {files_modified} files.")

if __name__ == '__main__':
    fix_images()
