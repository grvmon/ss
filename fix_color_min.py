import re
with open('styles.min.css', 'r') as f:
    content = f.read()

# Replace the base .phone-link span in minified if it exists
# We'll just explicitly append a desktop-only rule at the end of styles.min.css to force the desktop icon color and display.

append_css = """
@media (min-width: 769px) {
    .phone-link span {
        display: inline-flex !important;
        align-items: center !important;
        font-size: 1.2rem !important;
        color: var(--text-secondary, #334155) !important;
    }
}
"""

with open('styles.min.css', 'a') as f:
    f.write(append_css)

print("styles.min.css patched via append")
