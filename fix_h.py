import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix lf-main-heading
css = re.sub(r'(\.lf-main-heading\s*\{[^}]*)font-weight:\s*700;([^}]*\})', r'\1font-weight: 500;\2', css)

# Fix ssi-delhi-contact-heading (it's an H3)
css = re.sub(r'(\.ssi-delhi-contact-heading\s*\{[^}]*)font-weight:\s*700;([^}]*\})', r'\1font-weight: 500;\2', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("styles.min.css", "w", encoding="utf-8") as f:
    f.write(css.replace('\n', '').replace('  ', ''))

print("Fixed CSS overrides.")
