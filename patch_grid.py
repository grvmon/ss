import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace repeat(2, 1fr) with repeat(2, minmax(0, 1fr)) for mobile calc-banner-items
css = css.replace("grid-template-columns: repeat(2, 1fr);", "grid-template-columns: repeat(2, minmax(0, 1fr));")
css = css.replace("grid-template-columns: repeat(4, 1fr);", "grid-template-columns: repeat(4, minmax(0, 1fr));")

# Also ensure height stretches and content centers perfectly
# Just adding height: 100% to calc-banner-item
css = css.replace(".calc-banner-item {\n    display: flex;", ".calc-banner-item {\n    display: flex;\n    height: 100%;\n    width: 100%;\n    box-sizing: border-box;")

# We need to make sure the text wraps and centers
css = css.replace(".calc-item-name {\n    font-family", ".calc-item-name {\n    font-family")

# Let's write it back
with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Patched grid.")
