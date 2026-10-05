import os

append = """
/* Responsive Media Utility */
img, video {
    max-width: 100%;
    height: auto;
}
/* Ensure long text doesn't break mobile layout */
body {
    overflow-wrap: break-word;
    word-break: break-word;
}
"""

for file in ['styles.css', 'styles.min.css']:
    if os.path.exists(file):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(append)

print("Global image responsive fix applied.")
