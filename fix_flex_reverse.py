with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

import re

# Find the 1024px media query
target = """@media (max-width: 1024px) {
  .calc-container {
    grid-template-columns: 1fr;
    gap: 20px;
  }"""

replacement = """@media (max-width: 1024px) {
  .calc-container {
    display: flex;
    flex-direction: column-reverse;
    gap: 20px;
  }"""

css = css.replace(target, replacement)

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied column-reverse to mobile layout.")
