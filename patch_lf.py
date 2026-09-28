import re

with open("lead-form.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* Force 1-line fitting for headings */
.lf-main-heading {
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  font-size: clamp(14px, 5.5vw, 24px) !important;
}

.lf-sub-heading {
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  font-size: clamp(11px, 3.3vw, 13.5px) !important;
  max-width: none !important;
}

@media (max-width: 400px) {
  .lf-main-heading {
    font-size: clamp(12px, 4.8vw, 20px) !important;
  }
  .lf-sub-heading {
    font-size: clamp(10px, 3.1vw, 12px) !important;
  }
}
"""

with open("lead-form.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Patched lead form CSS.")
