import re

with open("self-storage-calculator/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The breadcrumbs are currently here:
# <main style="padding-top: 74px; padding-bottom: 40px;">
#     <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 var(--space-xl);">
#         <!-- Breadcrumbs -->
#         <nav aria-label="Breadcrumb">
#             <ul class="ssi-breadcrumb">
#                 <li><a href="/"><span class="material-symbols-rounded" style="font-size: 15px;">home</span> Home</a></li>
#                 <li class="bc-sep"><span class="material-symbols-rounded" style="font-size: 13px;">chevron_right</span></li>
#                 <li class="bc-current" aria-current="page">Storage Space Calculator</li>
#             </ul>
#         </nav>
#     </div>
#
#     <section id="calculator" class="calc-section" style="padding-top: 2px;">

# Let's replace the whole block
old_block = """    <main style="padding-top: 74px; padding-bottom: 40px;">
        <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 var(--space-xl);">
            <!-- Breadcrumbs -->
            <nav aria-label="Breadcrumb">
                <ul class="ssi-breadcrumb">
                    <li><a href="/"><span class="material-symbols-rounded" style="font-size: 15px;">home</span> Home</a></li>
                    <li class="bc-sep"><span class="material-symbols-rounded" style="font-size: 13px;">chevron_right</span></li>
                    <li class="bc-current" aria-current="page">Storage Space Calculator</li>
                </ul>
            </nav>
        </div>

        <section id="calculator" class="calc-section" style="padding-top: 2px;">"""

new_block = """    <main style="padding-top: 74px; padding-bottom: 40px;">
        <section id="calculator" class="calc-section" style="padding-top: 16px;">
            <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 var(--space-xl);">
                <!-- Breadcrumbs -->
                <nav aria-label="Breadcrumb">
                    <ul class="ssi-breadcrumb">
                        <li><a href="/"><span class="material-symbols-rounded" style="font-size: 15px;">home</span> Home</a></li>
                        <li class="bc-sep"><span class="material-symbols-rounded" style="font-size: 13px;">chevron_right</span></li>
                        <li class="bc-current" aria-current="page">Storage Space Calculator</li>
                    </ul>
                </nav>
            </div>"""

if old_block in html:
    html = html.replace(old_block, new_block)
    with open("self-storage-calculator/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Fixed breadcrumb background by moving it into calc-section.")
else:
    print("Could not find the block to replace!")
