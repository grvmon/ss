import os
import re

# Pattern: og:url content that was accidentally rewritten to ../assets/blog/<slug>
pattern = re.compile(r'(<meta property="og:url" content=")\.\.\/assets\/blog\/([^"]+)(")')

fixed = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d != '.git']
    for f in files:
        if f == "index.html":
            path = os.path.join(root, f)
            # Derive slug from directory path
            slug = os.path.relpath(root, ".").replace("\\", "/")
            if slug == ".":
                continue
            
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            
            original = content
            
            def replace_og_url(m):
                return m.group(1) + f"https://selfstorageindia.com/{slug}/" + m.group(3)
            
            content = pattern.sub(replace_og_url, content)
            
            if content != original:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(content)
                fixed += 1
                print(f"Fixed: {path}")

print(f"\nTotal fixed: {fixed}")
