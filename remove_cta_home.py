import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the Talk to an Advisor button
pattern = re.compile(r'\s*<button class="btn btn-primary"[^>]*>Talk to an Advisor</button>')

new_content = pattern.sub('', content)

if new_content != content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed from index.html")
else:
    print("Not found in index.html")
