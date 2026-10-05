with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

hide_rule = """
    .page-store .nav-actions .phone-link {
        display: none !important;
    }
"""

if hide_rule not in content:
    # Just append it at the end for both media queries
    append = """
@media (max-width: 1024px) {
    .page-store .nav-actions .phone-link {
        display: none !important;
    }
}
@media (max-width: 768px) {
    .page-store .nav-actions .phone-link {
        display: none !important;
    }
}
"""
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(append)
    print("Added page-store hiding to styles.css")

