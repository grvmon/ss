import glob
import re

for filepath in glob.glob("**/*.html", recursive=True):
    depth = filepath.count('/')
    if depth >= 2:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
        match = re.search(r'<img[^>]*class="brand-logo-img"[^>]*>', html)
        if match:
            print(f"{filepath}: {match.group(0)}")
