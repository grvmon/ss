import re
import glob

for filepath in glob.glob("**/*.html", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace the JS onclick window.open
    html = html.replace("window.open('/storage-calculator'", "window.open('/self-storage-calculator/'")
    html = html.replace("window.open('/storage-calculator/'", "window.open('/self-storage-calculator/'")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Fixed onclick links.")
