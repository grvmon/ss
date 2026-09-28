import os

target = """class="nav-link">Blogs</a>
            </nav>"""

# Sometimes spaces might differ, so let's use regex
import re
pattern = re.compile(r'(<a[^>]*class="nav-link"[^>]*>Blogs</a>\s*)</nav>')

replacement = r'''\1
                <a href="/self-storage-calculator/" class="btn btn-primary nav-mobile-cta">
                    <span class="material-symbols-rounded" style="font-size: 1.2rem;">calculate</span> Storage Calculator
                </a>
            </nav>'''

count = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                html = f.read()
            
            if "nav-mobile-cta" not in html and pattern.search(html):
                new_html = pattern.sub(replacement, html)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_html)
                count += 1

print(f"Patched {count} files.")
