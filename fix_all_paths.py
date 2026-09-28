import glob
import re
import os

html_files = glob.glob("**/*.html", recursive=True)

for filepath in html_files:
    # Skip if we somehow grab a directory
    if not os.path.isfile(filepath):
        continue

    # Determine depth relative to root
    # e.g., index.html -> depth 0
    # e.g., folder/index.html -> depth 1
    # e.g., folder/sub/index.html -> depth 2
    # Normalize paths to use forward slashes
    norm_path = filepath.replace('\\', '/')
    depth = norm_path.count('/')
    
    prefix = '../' * depth if depth > 0 else ''
    # If depth is 0, we don't prepend anything. But wait, if they have 'assets/' it should stay 'assets/'.
    # If they have '../assets/', it should be 'assets/'.
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    original_html = html

    # 1. Fix CSS
    # Look for href="styles.css..." or href="../styles.css..." and replace with href="{prefix}styles.css..."
    html = re.sub(r'href="(?:\.\./)*styles\.css(\?[^"]+)?"', f'href="{prefix}styles.css\\1"', html)
    html = re.sub(r'href="(?:\.\./)*styles\.min\.css(\?[^"]+)?"', f'href="{prefix}styles.min.css\\1"', html)

    # 2. Fix JS
    html = re.sub(r'src="(?:\.\./)*app\.js(\?[^"]+)?"', f'src="{prefix}app.js\\1"', html)

    # 3. Fix Assets (only for src="assets/..." or href="assets/...")
    # Be careful not to replace https://selfstorageindia.com/assets/...
    # First, normalize all (../)+assets/ to assets/
    html = re.sub(r'(?:href|src)="(?:\.\./)+assets/([^"]+)"', r'\g<0>'.replace('../', ''), html) # wait, replacing in match is tricky
    
    def repl_asset(m):
        attr = m.group(1) # href or src
        path = m.group(2) # whatever comes after assets/
        return f'{attr}="{prefix}assets/{path}"'
        
    # Match href="assets/..." or src="assets/..." or href="../assets/..." etc
    html = re.sub(r'(href|src)="(?:\.\./)*assets/([^"]+)"', repl_asset, html)
    
    # Also fix poster="assets/..."
    def repl_poster(m):
        return f'poster="{prefix}assets/{m.group(1)}"'
    html = re.sub(r'poster="(?:\.\./)*assets/([^"]+)"', repl_poster, html)

    # 4. Fix Calculator link
    html = html.replace('"./storage-calculator/"', '"/self-storage-calculator/"')
    html = html.replace('"/storage-calculator/"', '"/self-storage-calculator/"')
    
    # 5. Fix /locations/ to /self-storage-delhi/ (Wait, what is the locations page?)
    # Is there a locations index page?
    # Actually, they usually link to `#locations` or `/self-storage-delhi`, `/self-storage-gurugram`. Let's just fix the storage-calculator link for now.

    if html != original_html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

print("Mass relative path repair complete.")
