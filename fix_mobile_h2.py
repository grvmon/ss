with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Expand the mobile override to catch every h2-level heading
old = """    .section-header-centered h1,
    .section-header-centered h2,
    .intro-header-block h2,
    .why-editorial-header h2,
    .editorial-cta h2,
    .cta-box h2,
    .works-cta h2,
    .gallery-strip-header h2,
    .ncr-blog-layout h2 {
        font-size: 1.45rem !important;
        line-height: 1.22 !important;
        letter-spacing: -0.02em !important;
        margin-top: 0 !important;
        margin-bottom: 8px !important;
        font-weight: 700 !important;
    }"""

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
        line-height: 1.22 !important;
        letter-spacing: -0.02em !important;
        margin-top: 0 !important;
        margin-bottom: 8px !important;
        font-weight: 600 !important;
    }"""

css = css.replace(old, new)

# Also standardize mobile subheading p override
old_p = """    .section-header-centered p,
    .intro-header-block p,
    .gallery-strip-header p {
        font-size: 0.90rem !important;
        line-height: 1.48 !important;
        max-width: 100% !important;
        margin-bottom: 0 !important;
        color: var(--text-secondary, #5B6675) !important;
        text-align: center !important;
    }"""

new_p = """    .section-header-centered p,
    .intro-header-block p,
    .gallery-strip-header p,
    .why-editorial-header p,
    .editorial-cta p,
    .cta-box p,
    .works-cta p {
        font-size: 0.90rem !important;
        line-height: 1.55 !important;
        max-width: 100% !important;
        margin-bottom: 0 !important;
        color: var(--text-secondary, #5B6675) !important;
    }"""

css = css.replace(old_p, new_p)

with open("styles.css", "w") as f:
    f.write(css)
print("Mobile overrides expanded.")
