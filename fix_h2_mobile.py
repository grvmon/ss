import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add .ncr-blog-layout h2 to the mobile override block
css = css.replace('.gallery-strip-header h2 {', '.gallery-strip-header h2,\n    .ncr-blog-layout h2 {')

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
