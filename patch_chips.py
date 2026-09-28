import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will append media queries for calc-banner-features and calc-feature-chip
new_css = """
@media (max-width: 768px) {
    .calc-banner-features {
        flex-wrap: nowrap !important;
        gap: 6px !important;
        width: 100%;
        justify-content: center;
    }
    .calc-feature-chip {
        font-size: clamp(9px, 2.6vw, 13px) !important;
        padding: 4px 6px !important;
        white-space: nowrap !important;
    }
}

@media (max-width: 360px) {
    .calc-feature-chip {
        font-size: clamp(8px, 2.4vw, 10px) !important;
        padding: 4px 4px !important;
        letter-spacing: -0.02em !important;
    }
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Patched chips.")
