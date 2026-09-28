import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace border-radius: 20px and 24px for large boxes with var(--radius-card)
# The pills have padding: 6px 14px or something small.
# Large boxes have padding > 20px. 
# But it's easier to just find the classes.

classes_to_fix = [
    ".cta-box", 
    ".article-cta-box", 
    ".ceo-quote-banner", 
    ".value-feature-card", 
    ".accreditation-wrapper", 
    ".works-cta-card",
    ".calc-banner-inner",
    ".in-article-cta",
    ".ceo-story-card"
]

for cls in classes_to_fix:
    # Use regex to find the class block and replace 20px/24px with var(--radius-card)
    pattern = rf'({cls}\s*{{[^}}]*?)border-radius:\s*(20px|24px);'
    css = re.sub(pattern, r'\1border-radius: var(--radius-card);', css, flags=re.DOTALL)
    
    # Also handle responsive overrides
    pattern2 = rf'({cls}\s*{{[^}}]*?)border-radius:\s*(20px|24px)\s*!important;'
    css = re.sub(pattern2, r'\1border-radius: var(--radius-card) !important;', css, flags=re.DOTALL)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Large border radii standardized to var(--radius-card) (12px)")
