import glob
import re

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    depth = filepath.count('/')
    prefix = "../" * depth if depth > 0 else ""
    correct_logo_src = f"{prefix}assets/self-storage-india-logo.webp"

    def replacer(match):
        header = match.group(0)
        # Replace the mobile logo src inside the header
        header = re.sub(
            r'<img src="https://selfstorageindia\.com/[^"]*" alt="Self Storage India Logo" style="height: 32px; width: auto; object-fit: contain;">', 
            f'<img src="{correct_logo_src}" alt="Self Storage India Logo" style="height: 32px; width: auto; object-fit: contain;">', 
            header
        )
        return header

    new_html = re.sub(r'<header class="navbar" id="navbar">.*?</header>', replacer, html, flags=re.DOTALL)
    
    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)

print("Fixed mobile logo relative paths.")
