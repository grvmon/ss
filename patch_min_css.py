import re

with open('styles.min.css', 'r') as f:
    css = f.read()

# For .phone-link, minified version is likely:
# .phone-link{font-size:0;width:42px;height:42px;border-radius:50%;background:var(--primary);box-shadow:0 4px 12px rgba(24,108,236,.25);display:inline-flex;align-items:center;justify-content:center;gap:0;padding:0;flex-shrink:0;transition:transform .2s ease,box-shadow .2s ease}.phone-link span{font-size:22px;color:#fff;margin:0}

css = re.sub(r'\.phone-link\{([^\}]*)display:inline-flex([^\}]*)\}', r'.phone-link{\1display:flex\2}', css)
css = re.sub(r'\.phone-link span\{([^\}]*)\}', r'.phone-link span{\1;line-height:0;display:flex;align-items:center;justify-content:center}', css)

with open('styles.min.css', 'w') as f:
    f.write(css)

print("styles.min.css updated")
