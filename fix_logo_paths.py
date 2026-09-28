import re
import glob
import os

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Determine correct relative prefix
    depth = filepath.count(os.sep)
    if depth == 0:
        rel_prefix = "assets/"
    else:
        rel_prefix = "../assets/"
        
    # Replace ONLY inside src="..." attribute
    broken_src = 'src="https://selfstorageindia.com/assets/self-storage-india-logo.webp"'
    fixed_src = f'src="{rel_prefix}self-storage-india-logo.webp"'
    
    html = html.replace(broken_src, fixed_src)
    
    # Cache bust again just to be safe
    html = re.sub(r'href="(\.\./)?styles\.min\.css\?v=[0-9.]+"', r'href="\1styles.min.css?v=8.4"', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Logo src paths restored to relative.")
