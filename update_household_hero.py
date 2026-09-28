import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace H1
old_h1 = """<h1 class="hero-main-title">
                    Household Goods &amp; Furniture Storage in <span class="accent-text">Delhi/NCR</span>
                </h1>"""
new_h1 = """<h1 class="hero-main-title">
                    Household &amp; Furniture Storage in <span class="accent-text">Delhi/NCR</span>
                </h1>"""
html = html.replace(old_h1, new_h1)

# Replace P1
old_p1 = """<p class="hero-paragraph">
                    Rent clean, private, lockable storage rooms for 1BHK to 3BHK+ furniture during <strong>home renovation</strong>, <strong>house painting</strong>, or <strong>temporary relocation</strong>.
                </p>"""
new_p1 = """<p class="hero-paragraph">
                    Clean, private, lockable storage for 1BHK–3BHK+ furniture during renovation, painting, or temporary relocation.
                </p>"""
html = html.replace(old_p1, new_p1)

# Replace P2
old_p2 = """<p class="hero-paragraph">
                    Flexible month-to-month terms starting from 30 days with 24/7 CCTV security, biometric access, and partner pickup options across Delhi, Gurugram, and Noida.
                </p>"""
new_p2 = """<p class="hero-paragraph">
                    Flexible plans from 30 days, with 24/7 CCTV, biometric access, and pickup options across Delhi, Gurugram & Noida.
                </p>"""
html = html.replace(old_p2, new_p2)

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated.")
