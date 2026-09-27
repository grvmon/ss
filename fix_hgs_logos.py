import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Meta Images
html = html.replace('https://selfstorageindia.com/wp-content/uploads/2025/07/Self-Storage-India-Logo.png', '../assets/self-storage-india-logo.webp')

# Header Logo
html = re.sub(
    r'<img src="https://selfstorageindia.com/wp-content/uploads/2025/07/Self-Storage-India-Logo.png" alt="Self Storage India Logo" class="brand-logo-img".*?>',
    '<img src="../assets/self-storage-india-logo.webp" alt="Self Storage India Logo" class="brand-logo-img" fetchpriority="high" width="240" height="68" decoding="async">',
    html
)

# Footer Logos
html = re.sub(
    r'<img src="https://selfstorageindia.com/wp-content/uploads/2025/07/Self-Storage-India-Logo-300x63.png" alt=".*?" loading="lazy" decoding="async" width="240" height="50">',
    '<img src="../assets/self-storage-india-logo.webp" alt="Self Storage India Logo" loading="lazy" decoding="async" width="240" height="68">',
    html
)
html = re.sub(
    r'<img src="https://selfstorageindia.com/wp-content/uploads/2024/09/ss_warehouse_white_bg_449_60-1-300x40.webp" alt=".*?" loading="lazy" decoding="async" width="240" height="32">',
    '<img src="../assets/self-storage-warehouse-logo.webp" alt="Self Storage Warehouse Division Official Logo" loading="lazy" decoding="async" width="240" height="32">',
    html
)
html = re.sub(
    r'<img src="https://selfstorageindia.com/wp-content/uploads/2024/09/Logo_SSAMember-Reflex_kiztzz-300x198.webp" alt=".*?" loading="lazy" decoding="async" width="120" height="79">',
    '<img src="../assets/self-storage-association-member.webp" alt="Self Storage Association Asia Official Member Certification Badge" loading="lazy" decoding="async" width="120" height="79">',
    html
)

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Header and Footer Logos fixed.")
