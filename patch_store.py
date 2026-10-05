with open('store/index.html', 'r') as f:
    content = f.read()

old_nav = """            <div class="nav-actions">
                <a href="tel:+919090206090" class="phone-link"><span class="material-symbols-rounded">call</span>+91-9090206090</a>
                </div>
        </div>"""

new_nav = """            <div class="nav-actions">
                <a href="tel:+919090206090" class="phone-link"><span class="material-symbols-rounded">call</span>+91-9090206090</a>
                <button class="mobile-nav-toggle" id="mobileNavToggle" onclick="toggleMobileMenu()" aria-label="Toggle Navigation Menu">
                    <span class="material-symbols-rounded">menu</span>
                </button>
            </div>
        </div>"""

if old_nav in content:
    with open('store/index.html', 'w') as f:
        f.write(content.replace(old_nav, new_nav))
        print("Patched.")
