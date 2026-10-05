with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# In the @media (max-width: 768px) block:
# 1. Hide phone-link from header (circular button)
# 2. Show btn-primary (Talk to an Advisor) on ALL pages (not just /store)

old = """    .nav-actions .btn-primary {
        display: none !important;
    }
    .page-store .nav-actions .btn-primary {
        display: inline-flex !important;
        padding: 8px 14px;
        font-size: 0.82rem;
        font-weight: 600;
        border-radius: var(--radius-btn);
        white-space: nowrap;
        line-height: 1;
    }
    .mobile-nav-toggle {"""

new = """    .nav-actions .btn-primary {
        display: inline-flex !important;
        padding: 8px 14px;
        font-size: 0.82rem;
        font-weight: 600;
        border-radius: var(--radius-btn);
        white-space: nowrap;
        line-height: 1;
    }
    /* Hide phone-link circular icon in header on mobile — floating call btn handles calls */
    .nav-actions .phone-link {
        display: none !important;
    }
    .mobile-nav-toggle {"""

if old in content:
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content.replace(old, new))
    print("styles.css patched")
else:
    print("Could not find target block in styles.css")

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Also fix in the 1024px media query
old1024 = """    .nav-actions .btn-primary {
        display: none !important;
    }

    /* Zero-exit /store page exception */
    .page-store .mobile-nav-toggle {"""

new1024 = """    .nav-actions .btn-primary {
        display: none !important;
    }
    /* Hide phone-link in header on mobile — floating btn handles it */
    .nav-actions .phone-link {
        display: none !important;
    }

    /* Zero-exit /store page exception */
    .page-store .mobile-nav-toggle {"""

if old1024 in content:
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(content.replace(old1024, new1024))
    print("styles.css 1024 block patched")
else:
    print("Could not find 1024 block in styles.css")
