import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

pattern = r'\.section-header-centered h1,\s*\.section-header-centered h1,\s*\.section-header-centered h2,\s*\.intro-header-block h2,\s*\.why-editorial-header h2,\s*\.editorial-cta h2,\s*\.cta-box h2,\s*\.works-cta h2,\s*\.gallery-strip-header h2,\s*\.ncr-blog-layout h2\s*\{[^}]*\}'

new = """    .section-header-centered h1,
    .section-header-centered h2,
    .intro-header-block h2,
    .why-editorial-header h2,
    .editorial-cta h2,
    .cta-box h2,
    .works-cta h2,
    .gallery-strip-header h2,
    .ncr-blog-layout h2,
    .seo-details-section h2,
    .lf-main-heading,
    h2 {
        font-size: 1.45rem !important;
        line-height: 1.18 !important;
        letter-spacing: -0.01em !important;
        margin-top: 0 !important;
        margin-bottom: 8px !important;
        font-weight: 500 !important;
    }"""

css = re.sub(pattern, new, css)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Mobile H2 fixed.")
