with open('styles.min.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Append override rules at end of minified CSS
append = """
@media (max-width: 1024px) {
    .nav-actions .phone-link { display: none !important; }
    .nav-actions .btn-primary { display: inline-flex !important; padding: 8px 14px; font-size: 0.82rem; font-weight: 600; border-radius: var(--radius-btn, 8px); white-space: nowrap; line-height: 1; }
}
@media (max-width: 768px) {
    .nav-actions .phone-link { display: none !important; }
    .nav-actions .btn-primary { display: inline-flex !important; padding: 8px 14px; font-size: 0.82rem; font-weight: 600; border-radius: var(--radius-btn, 8px); white-space: nowrap; line-height: 1; }
}
"""

with open('styles.min.css', 'a', encoding='utf-8') as f:
    f.write(append)

print("styles.min.css appended")
