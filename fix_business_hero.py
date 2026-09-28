with open("business-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<h1 class="hero-main-title">'
end_marker = '<!-- CTA buttons group -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    replacement = """<h1 class="hero-main-title">
                    Secure Business Storage Solutions in <span class="accent-text">Delhi/NCR</span>
                </h1>
                <p class="hero-paragraph">
                    Store commercial inventory, office furniture, legal archives, IT servers in clean, pest-controlled, private lockable warehouse units.
                </p>
                <p class="hero-paragraph">
                    Enjoy 24/7 CCTV surveillance, 100% private key access, full GST tax invoicing, and seamless partner logistics transport options across Delhi, Gurugram, and Noida.
                </p>
                <p class="hero-paragraph" style="font-weight: 500; font-size: 0.85rem !important;">
                    Ideal for: Commercial Inventory • Office Furniture • Document Archives • IT Hardware Storage
                </p>
                
                """
    
    new_html = html[:start_idx] + replacement + html[end_idx:]
    with open("business-storage/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated business storage hero successfully.")
else:
    print("Markers not found.")
