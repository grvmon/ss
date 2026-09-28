import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Standardize all major layout containers to exactly 1280px for a perfectly uniform grid
replacements = [
    (r'max-width:\s*1400px;', r'max-width: 1280px;'),
    (r'max-width:\s*1240px;', r'max-width: 1280px;'),
    (r'max-width:\s*1200px;', r'max-width: 1280px;'),
    (r'max-width:\s*1140px;', r'max-width: 1280px;'),
    (r'max-width:\s*1100px;', r'max-width: 1280px;')
]

for old, new in replacements:
    css = re.sub(old, new, css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Standardized all layout containers to 1280px.")
