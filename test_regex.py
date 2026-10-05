import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<a href="[^"]+" target="_blank" rel="noopener" class="logo-item" title="([^"]+)">(\s*<img[^>]+>\s*)</a>')
new_content, count = pattern.subn(r'<div class="logo-item" title="\1">\2</div>', content)

print(f"Replaced {count} occurrences in index.html")
