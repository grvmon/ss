import os

append = """
/* Hide phone link globally in mobile header */
@media (max-width: 1024px) {
    .nav-actions .phone-link { display: none !important; }
}
@media (max-width: 768px) {
    .nav-actions .phone-link { display: none !important; }
}
"""

for file in ['styles.css', 'styles.min.css']:
    if os.path.exists(file):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(append)

print("CSS updated to hide call icon on all mobile headers.")
