import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# I will append new styles to the end to ensure they override earlier ones.
new_styles = """
/* Mobile Optimization for Calculator Items Grid */
@media (max-width: 600px) {
  .calc-inv-card {
    flex-direction: row;
    align-items: center;
    padding: 12px 14px;
    gap: 12px;
  }
  .inv-card-header {
    width: auto;
    flex: 1;
  }
  .inv-card-name {
    font-size: 0.9rem;
    white-space: normal; /* allow wrapping instead of ellipsis if name is long */
    line-height: 1.3;
  }
  .inv-card-controls {
    width: auto;
    gap: 12px;
    padding: 4px 8px;
    background: #f8fbff;
    border: 1px solid rgba(37, 99, 235, 0.1);
  }
  .calc-inv-card.active-item .inv-card-controls {
    background: rgba(37, 99, 235, 0.12);
    border-color: transparent;
  }
}
"""

with open("assets/css/storage-calculator.css", "a", encoding="utf-8") as f:
    f.write(new_styles)

print("Appended calculator mobile patch.")
