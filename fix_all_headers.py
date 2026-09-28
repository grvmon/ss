import glob
import re

# We will read the ideal header from household-goods-storage/index.html
with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    hh_html = f.read()

header_match = re.search(r'<header class="navbar" id="navbar">.*?</header>', hh_html, re.DOTALL)
if not header_match:
    print("Could not find ideal header!")
    exit(1)

ideal_header = header_match.group(0)
# Make links absolute so they work on all depth levels, or keep them absolute.
# Actually, the user's site is at the root. So /assets/ is fine.
# In the ideal header, the logo src is '../assets/self-storage-india-logo.webp'.
# We should change it to '/assets/self-storage-india-logo.webp' so it works everywhere.
ideal_header = ideal_header.replace('src="../assets/self-storage-india-logo.webp"', 'src="/assets/self-storage-india-logo.webp"')

# Also remove 'active' classes from the ideal header so it's a neutral template
ideal_header = ideal_header.replace('class="nav-link active"', 'class="nav-link"')
ideal_header = ideal_header.replace('class="dropdown-item active"', 'class="dropdown-item"')

count = 0
for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # We replace whatever the <header> block is with our ideal header
    new_html = re.sub(r'<header class="navbar" id="navbar">.*?</header>', ideal_header, html, flags=re.DOTALL)
    
    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        count += 1
        
print(f"Standardized header across {count} files.")
