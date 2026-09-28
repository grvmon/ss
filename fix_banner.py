import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace .calc-banner-container's width and max-width
def fix_calc_banner(match):
    block = match.group(0)
    
    # Check if we already modified it
    if "width: calc(100%" in block:
        return block
        
    # Replace max-width
    block = re.sub(r'max-width:\s*1280px;', 'max-width: calc(1280px - (2 * var(--space-content-gutter)));\n    width: calc(100% - (2 * var(--space-content-gutter)));', block)
    
    return block

css = re.sub(r'(\.calc-banner-container\s*\{[^}]+\})', fix_calc_banner, css, count=1)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed calc-banner-container width.")
