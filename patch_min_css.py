import re

with open("styles.min.css", "r", encoding="utf-8") as f:
    css = f.read()

# We don't know the exact format of the minified css, so let's just use regex
old_pattern = re.compile(r'\.phone-link\{[^}]*width:40px;height:40px;border-radius:var\(--radius-sm,8px\);background:transparent;[^}]*\}\.phone-link span\{font-size:26px;color:var\(--primary\);margin:0\}')

new_mobile = ".phone-link{font-size:0;width:42px;height:42px;border-radius:50%;background:var(--primary);box-shadow:0 4px 12px rgba(24,108,236,.25);display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform .2s ease,box-shadow .2s ease}.phone-link span{font-size:22px;color:#fff;margin:0}.phone-link:active{transform:scale(.95)}"

if old_pattern.search(css):
    css = old_pattern.sub(new_mobile, css)
    with open("styles.min.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Patched minified CSS.")
else:
    print("Could not find pattern in minified CSS.")
