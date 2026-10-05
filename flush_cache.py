import os
import glob
from datetime import datetime

timestamp = datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
cache_line = f"\n<!-- Cache Bust 23: {timestamp} -->"

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(cache_line)
print("Cache flushed in all .html files.")
