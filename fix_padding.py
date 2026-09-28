import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix .household-need__container padding
css = re.sub(r'(\.household-need__container,\s*\.business-need__container\s*\{[^}]*?)padding:\s*0 24px;', r'\1padding: 0 var(--space-xl);', css, flags=re.DOTALL)

# Fix .blog-detail-container padding
css = re.sub(r'(\.blog-detail-container\s*\{[^}]*?)padding:\s*92px 24px 70px;', r'\1padding: 92px var(--space-xl) 70px;', css, flags=re.DOTALL)

# Fix .blog-detail-container mobile padding
css = re.sub(r'(\.blog-detail-container\s*\{[^}]*?)padding:\s*84px 16px 50px;', r'\1padding: 84px var(--space-xl) 50px;', css, flags=re.DOTALL)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Standardized container horizontal padding.")
