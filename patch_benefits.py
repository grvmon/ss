import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
@media (max-width: 768px) {
    .why-benefit-item {
        font-size: clamp(9px, 3.1vw, 13px) !important;
        white-space: nowrap !important;
        gap: 6px !important;
    }
    .why-benefit-item .check-icon {
        font-size: clamp(14px, 4.5vw, 18px) !important;
    }
}
@media (max-width: 360px) {
    .why-benefit-item {
        font-size: clamp(8px, 3vw, 11px) !important;
        letter-spacing: -0.01em !important;
    }
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Patched benefit items.")
