import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Simple regex to extract blocks
blocks = re.findall(r'(\.[a-zA-Z0-9_-]*container[a-zA-Z0-9_-]*)\s*\{([^}]+)\}', css)
for name, content in blocks:
    mw = re.search(r'max-width:\s*([^;]+);', content)
    pd = re.search(r'(?<!-)padding:\s*([^;]+);', content)
    pl = re.search(r'padding-left:\s*([^;]+);', content)
    pr = re.search(r'padding-right:\s*([^;]+);', content)
    
    out = [name]
    out.append(f"MW: {mw.group(1).strip() if mw else 'None'}")
    out.append(f"PAD: {pd.group(1).strip() if pd else 'None'}")
    if pl: out.append(f"PL: {pl.group(1).strip()}")
    if pr: out.append(f"PR: {pr.group(1).strip()}")
    
    print(" | ".join(out))
