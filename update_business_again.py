with open("business-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<span class="hero-tagline-accent">'
end_marker = '<!-- CTA buttons group -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    replacement = """<span class="hero-tagline-accent">BUSINESS &amp; OFFICE STORAGE</span>
                </div>
                <h1 class="hero-main-title">
                    Secure Business Storage in <span class="accent-text">Delhi/NCR</span>
                </h1>
                <p class="hero-paragraph">
                    Private, lockable storage for <strong>inventory, office furniture, archives, and IT equipment</strong> in clean, pest-controlled units.
                </p>
                <p class="hero-paragraph">
                    <strong>24/7 CCTV, private access, GST invoicing</strong>, and pickup options across Delhi, Gurugram &amp; Noida.
                </p>
                
                """
    
    new_html = html[:start_idx] + replacement + html[end_idx:]
    with open("business-storage/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated business storage hero successfully.")
else:
    print("Markers not found.")
