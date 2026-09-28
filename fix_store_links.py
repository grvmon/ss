import re
import glob

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace absolute path references
    html = html.replace('href="/store#locations"', 'href="/self-storage-calculator/#locations"')
    html = html.replace('href="/store"', 'href="/self-storage-calculator/"')
    html = html.replace('href="/store/"', 'href="/self-storage-calculator/"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Fixed internal links.")
