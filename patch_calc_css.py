with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix justify-content in calc-mobile-bar
css = css.replace("justify-content: flex-start;", "justify-content: space-between;")

# Hide calc-visual-column on mobile
old_media = """@media (max-width: 1024px) {
  .calc-container {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .calc-visual-column {
    position: relative;
    top: 0;
  }"""

new_media = """@media (max-width: 1024px) {
  .calc-container {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .calc-visual-column {
    display: none !important;
  }"""

css = css.replace(old_media, new_media)

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Patched calculator CSS.")
