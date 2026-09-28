import re

with open("business-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to find and remove the Ideal for paragraph
pattern_to_remove = r'<p class="hero-ideal-list">\s*<strong>Ideal for:</strong> Commercial Inventory • Office Furniture • Document Archives • IT Hardware Storage\s*</p>'

html = re.sub(pattern_to_remove, '', html)

# Bump CSS version to force cache refresh
html = re.sub(r'href="\.\./styles\.min\.css\?v=[0-9.]+"', r'href="../styles.min.css?v=8.5"', html)

with open("business-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Removed Ideal for from business storage.")
