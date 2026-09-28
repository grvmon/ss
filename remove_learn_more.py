import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to find and remove the Learn More links
pattern = r'<a href="[^"]+" class="explore-link"[^>]*>Learn More[^<]*<span[^>]*>[^<]*</span></a>'

html = re.sub(pattern, '', html)

# Bump CSS version to force cache refresh
html = re.sub(r'href="\.\./styles\.min\.css\?v=[0-9.]+"', r'href="../styles.min.css?v=8.1"', html)

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Removed Learn More links and cache-busted.")
