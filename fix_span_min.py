import re
with open('styles.min.css', 'r') as f:
    content = f.read()

# in minified CSS it would be .phone-link span{display:none;font-size:1.2rem;color:var(--primary)}
pattern = re.compile(r'\.phone-link span\{display:none;font-size:1\.2rem;color:var\(--primary\)\}')
replacement = r'.phone-link span{display:inline-block;font-size:1.2rem;color:var(--primary)}'

new_content = pattern.sub(replacement, content)

if new_content != content:
    with open('styles.min.css', 'w') as f:
        f.write(new_content)
    print("styles.min.css patched")
else:
    print("Could not find pattern in styles.min.css")
