import glob
import re

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Bump CSS versions
    new_html = re.sub(r'(styles\.min\.css\?v=)\d+\.\d+', r'\g<1>8.5', html)
    new_html = re.sub(r'(styles\.css\?v=)\d+\.\d+', r'\g<1>8.5', new_html)
    new_html = re.sub(r'(storage-calculator\.css\?v=)\d+\.\d+', r'\g<1>8.5', new_html)

    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)

print("Bumped CSS version to v=8.5 in all HTML files.")
