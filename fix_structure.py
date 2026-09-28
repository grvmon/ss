import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the premature </section> before "What Can I Store?"
html = re.sub(
    r'(</section>)\s*(<h2><span class="accent-word">What Can I Store\?</span></h2>)',
    r'<div class="ncr-blog-layout" style="margin-top: 40px;">\n                    \2',
    html
)

# 2. Check if business-storage/index.html has the same issue? Let's fix that one too if needed.
# For now, just rewrite household-goods-storage
with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Fixed structure in household-goods-storage/index.html")
