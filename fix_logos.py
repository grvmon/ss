import glob
import re
import os

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    depth = filepath.count('/')
    prefix = "../" * depth if depth > 0 else ""
    correct_logo = f"{prefix}assets/self-storage-india-logo.webp"

    # We need to replace the WordPress URL in the brand-logo img src
    new_html = re.sub(
        r'(<a[^>]*class="brand-logo"[^>]*>\s*<img[^>]*src=")(https://selfstorageindia.com/[^"]*Logo\.png)("[^>]*>)',
        rf'\g<1>{correct_logo}\g<3>',
        html
    )

    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Fixed {filepath}")

print("Done fixing logos.")
