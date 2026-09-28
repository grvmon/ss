import os
import glob

html_files = glob.glob("*.html")
deleted_count = 0

for f in html_files:
    if f == "index.html":
        continue
    base = f[:-5] # remove .html
    # check if directory exists
    if os.path.isdir(base) and os.path.isfile(os.path.join(base, "index.html")):
        os.remove(f)
        deleted_count += 1
        print(f"Deleted duplicate root file: {f}")

print(f"Total deleted: {deleted_count}")
