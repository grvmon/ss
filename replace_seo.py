import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_content = """<section id="self-storage-guide" class="container" style="padding-bottom: 80px;">
            <div class="content-wrapper" style="max-width: 900px; margin: 0 auto;">
                <div class="ncr-blog-layout">
                    <h2><span class="accent-word">What Can I Store?</span></h2>
                    <p>At Self Storage India, our private lockable rooms are designed to accommodate a wide variety of storage needs for both households and businesses across Delhi NCR.</p>
                    <ul class="blog-features-list">
                        <li><strong>Household Goods & Furniture:</strong> Safely store sofas, beds, appliances, and seasonal items during a move, renovation, or downsizing.</li>
                        <li><strong>Business Inventory & Documents:</strong> Free up expensive commercial real estate by storing excess stock, promotional materials, and archived files.</li>
                        <li><strong>Luggage & Boxes:</strong> Ideal for students, frequent travelers, or expats needing a safe place for boxes and suitcases.</li>
                        <li><strong>Vehicles & Equipment:</strong> We provide dedicated spaces for storing specialized equipment or business assets safely.</li>
                    </ul>
                </div>

                <div class="ncr-blog-layout" style="margin-top: 40px;">
                    <h2><span class="accent-word">How Much Storage Space</span> Do I Need?</h2>
                    <p>Choosing the right size ensures you only pay for what you actually use. We offer a wide range of unit sizes designed to fit everything from a few boxes to an entire multi-bedroom home.</p>
                    <ul class="blog-features-list">
                        <li><strong>Box Storage (Under 20 sq. ft.):</strong> Perfect for 10-15 standard boxes, luggage, or a few small furniture items.</li>
                        <li><strong>Small Rooms (20 - 50 sq. ft.):</strong> Fits the contents of a 1-bedroom apartment, including a mattress set, sofa, and multiple boxes.</li>
                        <li><strong>Medium Rooms (50 - 100 sq. ft.):</strong> Ideal for a 2-bedroom home, accommodating large appliances, dining sets, and bulky furniture.</li>
                        <li><strong>Large Warehouses (100+ sq. ft.):</strong> Best for businesses storing palletized inventory or households moving 3-4 bedroom homes.</li>
                    </ul>
                    <p>Unsure of your requirements? Use our <a href="/storage-calculator/">Storage Space Calculator</a> or call our advisors to get a precise estimate based on your exact inventory.</p>
                </div>

                <div class="ncr-blog-layout" style="margin-top: 40px;">
                    <h2><span class="accent-word">How Self Storage Works</span></h2>
                    <p>We've streamlined the entire storage process to make it completely effortless for you, from packing to moving in.</p>
                    <ol class="blog-features-list" style="list-style-type: decimal; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 12px;">
                        <li><strong>Consult & Choose:</strong> Speak with our storage advisors to determine the exact size you need and get a transparent quote.</li>
                        <li><strong>Pack & Move:</strong> Pack your items yourself, or opt for our comprehensive packing and partner transport support (available at an additional cost) where professionals handle the logistics from your doorstep.</li>
                        <li><strong>Lock & Keep the Key:</strong> Move your belongings into your private room. You lock it with your own padlock and retain the only key, guaranteeing 100% privacy.</li>
                        <li><strong>Access Anytime:</strong> Visit your storage room during our flexible operating hours whenever you need to retrieve or add items.</li>
                    </ol>
                </div>

                <div class="ncr-blog-layout" style="margin-top: 40px;">
                    <h2>Storage Facilities Across <span class="accent-word">Delhi NCR</span></h2>
                    <p>With strategic locations across the National Capital Region, a premium storage facility is always within your reach.</p>
                    <ul class="blog-features-list">
                        <li><strong><a href="/self-storage-gurugram/">Gurugram (Sector 34)</a>:</strong> Our flagship warehouse facility easily accessible from Golf Course Extension and Sohna Road.</li>
                        <li><strong><a href="/self-storage-delhi/">Delhi (Dwarka)</a>:</strong> Conveniently located to serve South West Delhi, Janakpuri, and Airport areas.</li>
                        <li><strong><a href="/self-storage-noida/">Noida (Sector 59)</a>:</strong> A massive storage hub catering to Noida, Greater Noida, and East Delhi businesses and residents.</li>
                    </ul>
                    <p>Every single facility is equipped with 24/7 CCTV surveillance, pest-control measures, and rigorous access protocols to ensure maximum security for your valuables.</p>
                </div>
            </div>
        </section>"""

# We want to replace everything from <section id="self-storage-ncr"> to the closing </section> right before <!-- FAQ Section -->
pattern = re.compile(r'<section id="self-storage-ncr">.*?</section>', re.DOTALL)
html = pattern.sub(new_content, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SEO sections replaced.")
