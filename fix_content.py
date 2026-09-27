import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix security deposit / hidden fees
html = html.replace("Yes! Our pricing is completely transparent with no hidden fees or security deposit traps. We offer flexible monthly billing, so you only pay for the exact unit size and duration you require.",
                    "Yes! Our pricing is completely transparent. We offer flexible monthly billing, so you only pay for the exact unit size and duration you require, alongside a standard refundable security deposit.")

# Fix transport wording
html = html.replace("Yes! We provide comprehensive packing, logistics, loading, and partner transport support services across Delhi NCR, making your storage experience completely effortless.",
                    "Yes! We offer packing and loading assistance, and can arrange transport across Delhi NCR through our trusted third-party partners (available at an additional cost) to make your storage experience effortless.")

# Fix insurance wording
html = html.replace("Yes, we offer comprehensive insurance options for added protection and total peace of mind regarding your belongings.",
                    "Yes, we can facilitate insurance coverage options through our insurance partners for added protection and peace of mind regarding your belongings.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Content fixed.")
