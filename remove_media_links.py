import os, re
import datetime

timestamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S IST %Y")
cache_comment = f"\n<!-- Cache Bust 31: {timestamp} -->"

pattern = re.compile(r'<a href="[^"]+" target="_blank" rel="noopener" class="logo-item" title="([^"]+)">(\s*<img[^>]+>\s*)</a>')
modified_files = 0

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, count = pattern.subn(r'<div class="logo-item" title="\1">\2</div>', content)
            
            if count > 0:
                new_content += cache_comment
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files += 1

print(f"Removed links from {modified_files} files.")
