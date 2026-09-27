import re

with open("trust_bar.html", "r", encoding="utf-8") as f:
    tb = f.read()

# Replace div with a for links
links = {
    'Press Trust of India': 'https://www.ptinews.com/story/business/Self-Storage-India-launches-facility-in-Noida--plans-to-add-2-3-centres-by-March-25/1151608',
    'The Week Live': 'https://www.theweek.in/wire-updates/business/2023/12/18/del46-self-storage-india.html',
    'Times of India': 'https://timesofindia.indiatimes.com/business/india-business/self-storage-india-launches-facility-in-noida-plans-to-add-2-3-centres-by-march-25/articleshow/106095593.cms',
    'Republic World': 'https://www.republicworld.com/business-news/india-business/self-storage-india-launches-facility-in-noida-plans-to-add-2-3-centres-by-march-25/',
    'The Economic Times': 'https://economictimes.indiatimes.com/industry/services/property-/-cstruction/self-storage-india-launches-facility-in-noida-plans-to-add-2-3-centres-by-march-25/articleshow/106094382.cms',
    'Inside Self Storage': 'https://www.insideselfstorage.com/asia-self-storage/self-storage-india-opens-new-facility-in-noida-plans-further-expansion'
}

for title, url in links.items():
    tb = re.sub(
        rf'<div class="logo-item" title="{title}">\s*(<img.*?>)\s*</div>',
        f'<a href="{url}" target="_blank" rel="noopener" class="logo-item" title="{title}">\n                        \\1\n                    </a>',
        tb
    )

# Also fix the img paths from assets/ to ../assets/ because this is for household-goods-storage
tb_hgs = tb.replace('src="assets/', 'src="../assets/')

with open("trust_bar_hgs.html", "w", encoding="utf-8") as f:
    f.write(tb_hgs)

with open("trust_bar.html", "w", encoding="utf-8") as f:
    f.write(tb)

print("Trust bar links fixed.")
