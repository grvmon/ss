import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Decorative Icons
# Regex looks for material-symbols-rounded span without aria-hidden
content = re.sub(r'(<span class="[^"]*material-symbols-rounded[^"]*")(?!\s+aria-hidden)', r'\1 aria-hidden="true"', content)

# 2. aria-live polite
content = content.replace('aria-live="assertive"', 'aria-live="polite"')

# 3. spellcheck="false" on email
# Make sure we don't duplicate it if it's already there
if 'spellcheck="false"' not in content:
    content = re.sub(r'(<input[^>]*type="email"[^>]*)', r'\1 spellcheck="false"', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html A11y and UX fixes applied.")
