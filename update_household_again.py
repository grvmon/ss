with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<h1 class="hero-main-title">'
end_marker = '<!-- CTA buttons group -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    replacement = """<h1 class="hero-main-title">
                    Household &amp; Furniture Storage in <span class="accent-text">Delhi/NCR</span>
                </h1>
                <p class="hero-paragraph">
                    Clean, private, lockable storage for 1BHK–3BHK+ furniture during renovation, painting, or temporary relocation.
                </p>
                <p class="hero-paragraph">
                    Flexible plans from 30 days, with 24/7 CCTV, biometric access, and pickup options across Delhi, Gurugram & Noida.
                </p>
                
                """
    
    new_html = html[:start_idx] + replacement + html[end_idx:]
    with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated household storage hero successfully.")
else:
    print("Markers not found.")
