import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove the .offerings-section specific p and h2 overrides
css = re.sub(r'\.offerings-section \.section-header-centered p\s*\{[^}]*\}', '', css)
css = re.sub(r'\.offerings-section \.section-header-centered h2\s*\{[^}]*\}', '', css)

# Let's ensure ALL .section-header-centered p and .intro-header-block p are unified
# They are currently 17px.

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Typography consistency fixed.")
