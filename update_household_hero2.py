import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the "Ideal for" paragraph
pattern_to_remove = r'<p class="hero-ideal-list">\s*<strong>Ideal for:</strong> Home Renovation • Temporary Relocation • House Painting • Travelling Abroad • 1BHK–3BHK Furniture\s*</p>'

html = re.sub(pattern_to_remove, '', html)

# Bump CSS version to force cache refresh
html = re.sub(r'href="\.\./styles\.min\.css\?v=[0-9.]+"', r'href="../styles.min.css?v=8.0"', html)

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated and cache-busted.")
