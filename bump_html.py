import os
import re
import datetime

timestamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
cache_comment = f"\n<!-- Cache Bust 25: {timestamp} -->"

modified_count = 0

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(cache_comment)
            modified_count += 1

print(f"Bumped cache on {modified_count} HTML files")
