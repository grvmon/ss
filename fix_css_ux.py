import os

append = """
/* Vercel Web Interface Guidelines UX Improvements */
h1, h2, .hero-main-title, .section-title {
    text-wrap: balance;
}
:target {
    scroll-margin-top: 100px;
}
@media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
"""

for file in ['styles.css', 'styles.min.css']:
    if os.path.exists(file):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(append)

print("CSS typography and motion fixes applied.")
