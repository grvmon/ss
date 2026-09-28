css = open("styles.css").read()

# FIX 1: Footer padding — remove left/right 24px so blue bg goes fully edge to edge
# Inner .footer-container already has max-width + auto margins for content centering
css = css.replace(
    ".site-footer {\n    background: linear-gradient(135deg, #186CEC 0%, #0F52BA 100%);\n    padding: 50px 24px 40px;",
    ".site-footer {\n    background: linear-gradient(135deg, #186CEC 0%, #0F52BA 100%);\n    padding: 50px 0 40px;"
)

# FIX 2: FAQ section bottom border creates a visible line + space before footer
# Remove the bottom border — the footer's own top border/gradient is the separator
css = css.replace(
    ".faq-section {\n    padding: var(--space-section) 0;\n    background-color: #ffffff;\n    border-top: 1px solid var(--border);\n    border-bottom: 1px solid var(--border);\n}",
    ".faq-section {\n    padding: var(--space-section) 0 40px;\n    background-color: #ffffff;\n    border-top: 1px solid var(--border);\n}"
)

open("styles.css", "w").write(css)
print("Footer fixed.")
