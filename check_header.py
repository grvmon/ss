import glob
import re

for filepath in glob.glob("business-storage/index.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    match = re.search(r'<a[^>]*class="brand-logo"[^>]*>.*?</a>', html, re.DOTALL)
    if match:
        print(f"File: {filepath} => {match.group(0).strip()}")
    else:
        print(f"File: {filepath} => NO BRAND LOGO")
