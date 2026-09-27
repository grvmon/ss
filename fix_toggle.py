import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the specific mobile-nav-toggle rules
css = re.sub(
    r"\.mobile-nav-toggle \{\n\s*display: flex !important;\n\s*\}",
    ".mobile-nav-toggle {\n        display: flex !important;\n        visibility: visible !important;\n        opacity: 1 !important;\n        color: var(--text-dark, #111) !important;\n        z-index: 9999 !important;\n    }",
    css
)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Toggle fixed.")
