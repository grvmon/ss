import os

core_pages = [
    "index.html", 
    "self-storage-calculator/index.html",
    "self-storage-gurugram/index.html",
    "household-goods-storage/index.html"
]

for page in core_pages:
    if os.path.exists(page):
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
            
            has_mobile_cta = "nav-mobile-cta" in content
            has_zoho = "xnQsjsdp" in content
            has_cache_v10 = "styles.min.css?v=10.0" in content or "styles.css?v=10.0" in content
            
            print(f"[{'PASS' if (has_mobile_cta and has_zoho and has_cache_v10) else 'FAIL'}] {page}")
