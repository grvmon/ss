import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Task 2: SEO Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Household Goods Storage in Delhi NCR | Self Storage India</title>',
    html
)
html = re.sub(
    r'<meta property="og:title" content=".*?">',
    '<meta property="og:title" content="Household Goods Storage in Delhi NCR | Self Storage India">',
    html
)
html = re.sub(
    r'<meta name="twitter:title" content=".*?">',
    '<meta name="twitter:title" content="Household Goods Storage in Delhi NCR | Self Storage India">',
    html
)

# Task 1: H1
html = re.sub(
    r'<h1 class="hero-main-title">.*?</h1>',
    '<h1 class="hero-main-title">\n                    Household Goods &amp; Furniture Storage in <span class="accent-text">Delhi/NCR</span>\n                </h1>',
    html,
    flags=re.DOTALL
)

# Task 27: Staging noindex
if '<meta name="robots" content="noindex, nofollow">' not in html:
    html = html.replace('<head>', '<head>\n    <!-- STAGING ONLY -->\n    <meta name="robots" content="noindex, nofollow">')

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SEO and H1 updated.")
