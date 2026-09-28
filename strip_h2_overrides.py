import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will replace any explicit font-weight, line-height, letter-spacing inside an h2 block 
# with the correct global properties if they exist, or just standardize them.
# The safest way is to just do a blanket regex on blocks containing "h2" but that might be brittle.
# Let's target the exact properties inside these specific selectors.

# Standardize desktop blocks
css = re.sub(r'(\.section-header-centered h1,\s*\n\.section-header-centered h2\s*\{[^}]*?font-weight:\s*)\d+;', r'\g<1>500;', css)
css = re.sub(r'(\.section-header-centered h1,\s*\n\.section-header-centered h2\s*\{[^}]*?letter-spacing:\s*)-[0-9.]+e?m?;', r'\g<1>-0.01em;', css)
css = re.sub(r'(\.section-header-centered h1,\s*\n\.section-header-centered h2\s*\{[^}]*?line-height:\s*)[0-9.]+;', r'\g<1>1.18;', css)

h2_selectors = [
    r'\.why-editorial-header h2', r'\.editorial-cta h2', r'\.cta-box h2', r'\.works-cta h2',
    r'\.ncr-blog-layout h2', r'\.gallery-strip-header h2,\s*\n\s*\.ncr-blog-layout h2',
    r'\.calc-banner-header h2', r'\.seo-details-section h2', r'\.ssi-noida-blog h2\.article-main-title',
    r'\.ssi-noida-blog h2\.article-section-title', r'\.article-content h2', r'\.ceo-story-card h2',
    r'\.values-section-head h2', r'\.advisor-modal-head h2'
]

for sel in h2_selectors:
    # Font weight
    css = re.sub(r'(' + sel + r'\s*\{[^}]*?font-weight:\s*)\d+;', r'\g<1>500;', css)
    # Line height
    css = re.sub(r'(' + sel + r'\s*\{[^}]*?line-height:\s*)[0-9.]+;', r'\g<1>1.18;', css)
    # Letter spacing
    css = re.sub(r'(' + sel + r'\s*\{[^}]*?letter-spacing:\s*)-?[0-9.]+e?m?p?x?;', r'\g<1>-0.01em;', css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Overrides stripped/standardized.")
