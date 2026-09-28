css = open("styles.css").read()

# ============================================================
# FIX 1: Standardize ALL H2 font-weight to 700 (bold, consistent)
# why-editorial-header uses 600 — bump to 700 to match the rest
css = css.replace(
    ".why-editorial-header h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 600;",
    ".why-editorial-header h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 700;"
)

# editorial-cta h2 was 600 — bump to 700
css = css.replace(
    ".editorial-cta h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 600;",
    ".editorial-cta h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 700;"
)
css = css.replace(
    ".cta-box h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 600;",
    ".cta-box h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 700;"
)
css = css.replace(
    ".works-cta h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 600;",
    ".works-cta h2 {\n    font-size: clamp(1.3rem, 2vw, 1.7rem);\n    font-weight: 700;"
)

# ============================================================
# FIX 2: ncr-blog-layout h2 mobile — remove text-align: center (it's a left-aligned section)
css = css.replace(
    "    .gallery-strip-header h2,\n    .ncr-blog-layout h2 {\n        font-size: 1.45rem !important;\n        line-height: 1.22 !important;\n        letter-spacing: -0.02em !important;\n        margin-top: 0 !important;\n        margin-bottom: 8px !important;\n        font-weight: 700 !important;\n        text-align: center !important;\n    }",
    "    .gallery-strip-header h2,\n    .ncr-blog-layout h2 {\n        font-size: 1.45rem !important;\n        line-height: 1.22 !important;\n        letter-spacing: -0.02em !important;\n        margin-top: 0 !important;\n        margin-bottom: 8px !important;\n        font-weight: 700 !important;\n    }"
)

# Also add missing H2 components to mobile override block
css = css.replace(
    "    .section-header-centered h1,\n    .section-header-centered h2,\n    .intro-header-block h2,\n    .gallery-strip-header h2,\n    .ncr-blog-layout h2 {",
    "    .section-header-centered h1,\n    .section-header-centered h2,\n    .intro-header-block h2,\n    .why-editorial-header h2,\n    .editorial-cta h2,\n    .cta-box h2,\n    .works-cta h2,\n    .gallery-strip-header h2,\n    .ncr-blog-layout h2 {"
)

# ============================================================
# FIX 3: gallery-strip-header p  — standardize to 17px to match section subtitles
css = css.replace(
    ".gallery-strip-header p {\n    font-size: 15px;",
    ".gallery-strip-header p {\n    font-size: 17px;"
)

# ============================================================
# FIX 4: CTA box p sizes — standardize to 17px to match section subtitles
css = css.replace(
    ".editorial-cta p {\n    font-size: 0.95rem;",
    ".editorial-cta p {\n    font-size: 17px;"
)
css = css.replace(
    ".cta-box p {\n    font-size: 0.98rem;",
    ".cta-box p {\n    font-size: 17px;"
)
css = css.replace(
    ".works-cta p {\n    font-size: 0.95rem;",
    ".works-cta p {\n    font-size: 17px;"
)

# ============================================================
# FIX 5: lf-main-heading — use clamp instead of hardcoded 24px
css = css.replace(
    ".lf-main-heading {\n  font-family: var(--lf-font-sans);\n  font-size: 24px;",
    ".lf-main-heading {\n  font-family: var(--lf-font-sans);\n  font-size: clamp(1.3rem, 2vw, 1.7rem);"
)

open("styles.css", "w").write(css)
print("Typography fully standardized.")
