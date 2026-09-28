import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Inject the new variable
if "--space-content-gutter:" not in css:
    css = css.replace("--space-xl: 24px;", "--space-xl: 24px;\n    --space-content-gutter: calc(var(--space-xl) + 5px);")
    css = css.replace("--space-xl: 16px;", "--space-xl: 16px;\n        --space-content-gutter: calc(var(--space-xl) + 5px);")

# 2. Update the containers
# We need to change `padding: 0 var(--space-xl);` to `padding: 0 var(--space-content-gutter);`
# But ONLY for content containers, NOT `.nav-container` or `.trust-bar-container`'s overrides if we want them aligned differently.
# Wait, the plan said "all content sections". 
# List of containers to update:
containers_to_update = [
    r'\.container',
    r'\.hero-content-wrapper',
    r'\.trust-bar-container',
    r'\.features-strip-container',
    r'\.why-editorial-container',
    r'\.calc-container',
    r'\.locations-map-container',
    r'\.faq-accordions-centered-container',
    r'\.section-container-why',
    r'\.ncr-container',
    r'\.business-need__container',
    r'\.blog-detail-container',
    r'\.ceo-page-container',
    r'\.seo-details-section__container',
    r'\.pricing-table-container',
    r'\.calc-banner-container',
    r'\.footer-container'
]

# We will iterate over the CSS and use regex to replace paddings INSIDE these specific blocks.
def update_block_padding(match):
    block = match.group(0)
    
    # We ignore nav-container
    if ".nav-container" in block:
        return block
        
    # Replace horizontal paddings
    # `padding: 0 var(--space-xl);`
    block = re.sub(r'padding:\s*0\s+var\(--space-xl\)', r'padding: 0 var(--space-content-gutter)', block)
    
    # `padding: 20px var(--space-xl) 28px;` -> `padding: 20px var(--space-content-gutter) 28px;`
    block = re.sub(r'padding:\s*(\d+px)\s+var\(--space-xl\)\s+(\d+px)', r'padding: \1 var(--space-content-gutter) \2', block)
    
    # `padding: 0 24px;` (hardcoded in seo-details and pricing)
    block = re.sub(r'padding:\s*0\s+24px', r'padding: 0 var(--space-content-gutter)', block)
    
    # `padding: 0 16px;` or `padding: 0 16px !important;`
    block = re.sub(r'padding:\s*0\s+16px', r'padding: 0 var(--space-content-gutter)', block)
    
    # For footer-container which might have no padding currently, we should just let the site-footer handle it?
    # Wait, the plan said we constrain its inner content.
    if ".footer-container" in block and "max-width" in block:
        # Add padding if it doesn't exist
        if "padding" not in block:
            block = block.replace("margin: 0 auto;", "margin: 0 auto;\n    padding: 0 var(--space-content-gutter);")
            
    # For blog-detail-container `padding: 92px var(--space-xl) 70px;`
    block = re.sub(r'padding:\s*(\d+px)\s+var\(--space-xl\)\s+(\d+px)', r'padding: \1 var(--space-content-gutter) \2', block)
    
    # For ceo-page-container `padding: 56px var(--space-xl) var(--space-3xl);`
    block = re.sub(r'padding:\s*(\d+px)\s+var\(--space-xl\)\s+var\(--space-3xl\)', r'padding: \1 var(--space-content-gutter) var(--space-3xl)', block)
    
    return block

# Match blocks: .classname { ... }
for cls in containers_to_update:
    # This regex matches the class, optionally some other selectors, then { ... }
    # It handles nested media queries slightly poorly if we are not careful, but since we are matching standard blocks:
    pattern = rf'({cls}(?:[\s,][^{{]*?)?\{{[^{{}}]*\}})'
    css = re.sub(pattern, update_block_padding, css, flags=re.DOTALL)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated.")
