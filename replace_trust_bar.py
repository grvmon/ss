import re

def replace_tb(filename, tb_file):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()
    with open(tb_file, "r", encoding="utf-8") as f:
        tb = f.read()
    
    new_html = re.sub(r'<section class="trust-bar">.*?</section>', tb.strip(), html, flags=re.DOTALL)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_html)

replace_tb("household-goods-storage/index.html", "trust_bar_hgs.html")
replace_tb("index.html", "trust_bar.html")
print("Replaced trust bars.")
