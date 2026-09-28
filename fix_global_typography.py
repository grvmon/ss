import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# The canonical standard from FAQ section:
# H2: font-size: clamp(1.3rem, 2vw, 1.7rem); font-weight: 600; line-height: 1.2; letter-spacing: -0.02em
# Sub-p: font-size: 17px; line-height: 1.65; color: var(--text-secondary)

# -------------------------------------------------------------------
# Parse CSS into blocks and find rules that contain h2 selectors
# then standardize their font-size
# -------------------------------------------------------------------
h2_clamp = "clamp(1.3rem, 2vw, 1.7rem)"

# All selector patterns that are H2-level headings on the page
h2_selectors = [
    r'\.section-header-centered h[12]',
    r'\.why-editorial-header h2',
    r'\.editorial-cta h2',
    r'\.cta-box h2',
    r'\.works-cta h2',
    r'\.ncr-blog-layout h2',
    r'\.gallery-strip-header h2',
    r'\.seo-details-section h2',
    r'\.intro-header-block h2',
    r'\.calc-banner-header h2',
    r'\.faq-cta-content h3',  # This is used as a section heading, not a card h3
    r'\.lf-main-heading',
    r'\.article-main-title',
    r'\.blog-detail-header h1',
    r'\.blog-detail-header h2',
]

# Find any H2 rules with non-standard sizes and fix them
# Strategy: find CSS blocks containing h2 and check font-size line
def fix_h2_block(match):
    block = match.group(0)
    if "font-size" in block:
        # Only fix if it's NOT already the correct clamp
        if h2_clamp not in block:
            # Replace any rem/px size that looks like a section heading (>1.2rem)
            block = re.sub(
                r'font-size:\s*(2\.2rem|2rem|1\.8rem|1\.5rem|1\.45rem|1\.4rem|1\.35rem|1\.3rem|28px|26px|24px|22px)',
                f'font-size: {h2_clamp}',
                block
            )
    return block

# Apply to specific known selectors
for sel in h2_selectors:
    # Find the CSS block for this selector
    pattern = re.compile(
        r'(' + sel + r'[^{]*\{[^}]*\})',
        re.DOTALL
    )
    css = pattern.sub(fix_h2_block, css)

# -------------------------------------------------------------------
# Standardize section-level subheading paragraphs
# These are the descriptive text lines below H2 headings
# Standard: font-size: 17px; line-height: 1.65;
# -------------------------------------------------------------------
# Fix gallery-strip-header p (already done to 17px in previous fix, but re-enforce)
# Fix any remaining direct subtitle-level p that uses rem instead of 17px
sub_p_selectors = [
    (r'\.section-header-centered p', '17px', '1.65'),
    (r'\.intro-header-block p', '17px', '1.65'),
    (r'\.why-editorial-header p', '17px', '1.65'),
    (r'\.gallery-strip-header p', '17px', '1.6'),
    (r'\.editorial-cta p', '17px', '1.65'),
    (r'\.cta-box p', '17px', '1.65'),
    (r'\.works-cta p', '17px', '1.65'),
]

for sel, size, lh in sub_p_selectors:
    pattern = re.compile(r'(' + sel + r'\s*\{[^}]*?)font-size:\s*[^;]+;', re.DOTALL)
    def make_replacer(s, fs):
        def replacer(m):
            return m.group(1) + f'font-size: {fs};'
        return replacer
    css = pattern.sub(make_replacer(sel, size), css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Global typography standardized to FAQ section standard.")
