import re

# Fix 1: Fix the white line - change navbar bg to match hero gradient top color
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# The hero starts with #F8FAFC. The navbar is white #ffffff.
# The visual "white line" is actually the scrolled hero area being white 
# vs the very slight gradient of F8FAFC. Both colors look like white.
# The REAL issue: looking at the screenshot, it's actually the BROWSER/OS WINDOW CHROME
# creating a border. But let's make navbar match hero bg perfectly.

# Make navbar use same bg as hero gradient start
css = css.replace(
    '.navbar {\n    position: fixed;\n    top: 0;\n    left: 0;\n    right: 0;\n    z-index: 100;\n    background: #ffffff;',
    '.navbar {\n    position: fixed;\n    top: 0;\n    left: 0;\n    right: 0;\n    z-index: 100;\n    background: #F8FAFC;'
)
css = css.replace(
    '.navbar.scrolled {\n    background: #ffffff;',
    '.navbar.scrolled {\n    background: #ffffff; /* Stays white after scroll */'
)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("navbar background matched to hero")
