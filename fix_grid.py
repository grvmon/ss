import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("grid-template-columns: 1fr 1fr !important;", "grid-template-columns: repeat(3, 1fr) !important;")
css = re.sub(r"\.hero-trust-indicators \.trust-indicator-item:nth-child\(5\) \{\n\s*grid-column: 1 / -1;\n\s*\}\n", "", css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Grid fixed.")
