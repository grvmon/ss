import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'(\.advisor-modal-head h2\s*\{[^}]*?)font-size:\s*22px;', r'\g<1>font-size: 1.45rem;', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
