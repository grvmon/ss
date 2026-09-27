import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    hgs = f.read()

# Remove everything after the first </html>
first_html = hgs.find('</html>')
if first_html != -1:
    hgs = hgs[:first_html + 7]

# Fix relative paths for the injected footer/modals
hgs = hgs.replace('src="app.min.js', 'src="../app.min.js')
hgs = hgs.replace('src="lead-form.min.js', 'src="../lead-form.min.js')
hgs = hgs.replace('src="storage-advisor.min.js', 'src="../storage-advisor.min.js')

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(hgs)
print("Duplicate content and paths fixed.")
