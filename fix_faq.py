import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'(\.faq-item\s*\{[^}]*?)border-radius:\s*8px\s*!important;', r'\1border-radius: 12px !important;', css, flags=re.DOTALL)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("FAQ mobile radii standardized to 12px")
