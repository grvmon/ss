with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<h1 class="hero-main-title">'
end_marker = '<!-- CTA buttons group -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    replacement = """<h1 class="hero-main-title">
                    Temporary Household &amp; Furniture Storage in <span class="accent-text">Delhi/NCR</span>
                </h1>
                <p class="hero-paragraph">
                    Rent clean, private, lockable storage rooms for 1BHK to 3BHK+ furniture during home renovation, house painting, or temporary relocation.
                </p>
                <p class="hero-paragraph">
                    Flexible month-to-month terms starting from 30 days with 24/7 CCTV security, biometric access, and partner pickup options across Delhi, Gurugram, and Noida.
                </p>
                <p class="hero-paragraph" style="font-weight: 500; font-size: 0.85rem !important;">
                    Ideal for: Home Renovation • Temporary Relocation • House Painting • Travelling Abroad • 1BHK–3BHK Furniture
                </p>
                
                """
    
    new_html = html[:start_idx] + replacement + html[end_idx:]
    with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated successfully.")
else:
    print("Markers not found.")
