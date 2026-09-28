import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace hardcoded mobile 16px paddings with var(--space-content-gutter) in content sections
def replace_mobile_paddings(match):
    block = match.group(0)
    if ".nav-container" in block:
        return block
    block = re.sub(r'padding:\s*0\s+16px\s*!important;', r'padding: 0 var(--space-content-gutter) !important;', block)
    block = re.sub(r'padding:\s*0\s+16px;', r'padding: 0 var(--space-content-gutter);', block)
    block = re.sub(r'padding:\s*0\s+20px;', r'padding: 0 var(--space-content-gutter);', block)
    return block

# Find all class blocks
css = re.sub(r'(\.[a-zA-Z0-9_-]+(?:[\s,][^{]*?)?\{[^{}]*\})', replace_mobile_paddings, css)

# Fix breadcrumb nav
css = re.sub(r'(\.breadcrumb-nav\s*\{[^}]*padding:\s*)(\d+px)\s+(\d+px)\s+(\d+px)', r'\1\2 var(--space-content-gutter) \4', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("styles.min.css", "w", encoding="utf-8") as f:
    f.write(css.replace('\n', '').replace('  ', ''))

print("Fixed mobile gutters and breadcrumbs.")
