import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# I want to update all h3 rules that explicitly set font-weight, line-height, letter-spacing
# to the new baseline (W:500, LS:-0.01em, LH:1.18).
# Or just remove them so they inherit from the base h3 rule, but since it's safer to be explicit,
# I will just regex replace them.

css = re.sub(r'(h3\s*\{[^}]*?font-weight:\s*)\d+;', r'\g<1>500;', css)
css = re.sub(r'(h3\s*\{[^}]*?line-height:\s*)[0-9.]+;', r'\g<1>1.18;', css)
css = re.sub(r'(h3\s*\{[^}]*?letter-spacing:\s*)-?[0-9.]+e?m?p?x?;', r'\g<1>-0.01em;', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("H3 overrides updated.")
