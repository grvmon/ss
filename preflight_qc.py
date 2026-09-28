import os
import glob

html_files = glob.glob("**/*.html", recursive=True)

core_pages = [
    "index.html", 
    "self-storage-calculator/index.html",
    "self-storage-gurugram/index.html",
    "self-storage-delhi/index.html",
    "self-storage-noida/index.html",
    "household-goods-storage/index.html",
    "business-storage/index.html"
]

report = []
for page in core_pages:
    if os.path.exists(page):
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Checks
            has_cache_bust = "styles.min.css?v=" in content
            has_mobile_cta = "nav-mobile-cta" in content
            has_zoho = "xnQsjsdp" in content
            
            report.append({
                "page": page,
                "cache": has_cache_bust,
                "mobile_cta": has_mobile_cta,
                "zoho": has_zoho
            })

for r in report:
    print(f"Page: {r['page']} | Cache: {r['cache']} | Mobile CTA: {r['mobile_cta']} | Zoho: {r['zoho']}")
