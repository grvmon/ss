import os

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* Mobile only CTA in nav drawer */
.nav-mobile-cta {
    display: none !important;
}

@media (max-width: 1024px) {
    .nav-mobile-cta {
        display: flex !important;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-top: auto; /* Push to bottom */
        margin-bottom: 20px;
        padding: 12px 16px;
        width: 100%;
        border-radius: var(--radius-btn, 8px);
    }
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Patched styles.css.")
