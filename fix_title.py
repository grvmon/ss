import glob
import re

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Add title tag to mobile logo
    new_html = html.replace('alt="Self Storage India Logo" style="height: 32px;', 'title="Self Storage India Logo" alt="Self Storage India Logo" style="height: 32px;')

    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)

print("Added title attribute to mobile menu logo globally.")
