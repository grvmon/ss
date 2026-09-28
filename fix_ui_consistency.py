import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix all cards to 12px explicitly to match desktop --radius-card
css = re.sub(r'border-radius:\s*10px\s*!important;', 'border-radius: 12px !important;', css)
css = re.sub(r'border-radius:\s*10px;', 'border-radius: 12px;', css)
css = re.sub(r'border-radius:\s*14px;', 'border-radius: 12px;', css)
css = re.sub(r'border-radius:\s*16px;', 'border-radius: 12px;', css)
# Wait, pills and circles should not be 12px.
# border-radius: 50% is for circles.
# border-radius: 20px / 24px might be for pills.
# I'll let those be.

# Let's fix H2 consistency in mobile CSS
# Currently:
# .gallery-strip-header h2, .intro-header-block h2, .section-header-centered h1, .section-header-centered h2
# Let's add .ncr-blog-layout h2, .calc-banner-header h2 to this block
css = re.sub(
    r'\.gallery-strip-header h2,',
    r'.gallery-strip-header h2, .ncr-blog-layout h2, .calc-banner-header h2,',
    css
)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("UI consistency fixed.")
