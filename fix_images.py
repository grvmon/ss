import os
import re
import difflib

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

# Known exact replacements
MANUAL_FIXES = {
    'facility_3.webp': 'rsz_businesses_need_document_storage1200px.webp',  # Fallback image in assets/blog
    'manjali_cover.jpg': '../assets/manjali_cover.jpg',
    'self-storage-india-logo.png': '../assets/self-storage-india-logo.png'
}

def get_all_assets():
    assets = []
    for f in os.listdir('assets/blog'):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            assets.append(f)
    return assets

def get_closest_match(broken_name, available_assets):
    # Try exact match with – replaced by -
    clean_broken = broken_name.replace('–', '-').replace('%E2%80%93', '-')
    for asset in available_assets:
        if asset == clean_broken:
            return asset
    
    # Try difflib
    matches = difflib.get_close_matches(clean_broken, available_assets, n=1, cutoff=0.6)
    if matches:
        return matches[0]
        
    return None

def fix_images():
    available_assets = get_all_assets()
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
                    if ref.startswith('http') or ref.startswith('//'): continue
                    
                    if ref.startswith('/'):
                        img_path = os.path.join('.', ref[1:])
                    else:
                        img_path = os.path.normpath(os.path.join(root, ref))
                        
                    if not os.path.exists(img_path):
                        filename = os.path.basename(ref)
                        new_ref = None
                        
                        if filename in MANUAL_FIXES:
                            if MANUAL_FIXES[filename].startswith('../'):
                                # if it's in the root folder
                                depth = root.count(os.sep)
                                prefix = '../' * depth if depth > 0 else ''
                                new_ref = prefix + MANUAL_FIXES[filename].lstrip('../')
                            else:
                                new_ref = ref.replace(filename, MANUAL_FIXES[filename])
                        else:
                            closest = get_closest_match(filename, available_assets)
                            if closest:
                                new_ref = ref.replace(filename, closest)
                                
                        if new_ref:
                            # Replace in content
                            content = content.replace(f'"{ref}"', f'"{new_ref}"')
                            content = content.replace(f"'{ref}'", f"'{new_ref}'")
                            fixed_count += 1
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Fixed {fixed_count} broken image references across {files_modified} files.")

if __name__ == '__main__':
    fix_images()
