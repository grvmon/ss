import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace width: 300px; max-width: 85vw; with wider settings
css = css.replace(
    "width: 300px;\n        max-width: 85vw;", 
    "width: 380px;\n        max-width: 95vw;"
)

# Append fluid typography for dropdown paragraphs inside the nav-links
new_css = """
@media (max-width: 1024px) {
    .nav-links .dropdown-info p {
        font-size: clamp(10px, 3.2vw, 12px) !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    .nav-links .dropdown-item {
        padding: 10px 8px !important;
        gap: 10px !important;
    }
    
    .nav-links .dropdown-icon {
        width: 38px !important;
        height: 38px !important;
        font-size: 1.25rem !important;
        flex-shrink: 0 !important;
    }
}

@media (max-width: 360px) {
    .nav-links .dropdown-info p {
        font-size: clamp(9px, 2.9vw, 11px) !important;
        letter-spacing: -0.02em !important;
    }
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Patched mobile menu.")
