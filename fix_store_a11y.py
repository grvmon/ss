import re

with open('store/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(<span class="[^"]*material-symbols-rounded[^"]*")(?!\s+aria-hidden)', r'\1 aria-hidden="true"', content)
content = content.replace('aria-live="assertive"', 'aria-live="polite"')
if 'spellcheck="false"' not in content:
    content = re.sub(r'(<input[^>]*type="email"[^>]*)', r'\1 spellcheck="false"', content)

with open('store/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("store/index.html A11y and UX fixes applied.")
