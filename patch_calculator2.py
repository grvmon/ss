import re

with open("assets/css/storage-calculator.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the previous block with a much more robust flex layout
old_styles = """
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

new_styles = """
/* Mobile Optimization for Calculator Items Grid */
@media (max-width: 600px) {
  .calc-inv-card {
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    justify-content: space-between;
    padding: 12px;
    gap: 8px;
    overflow: hidden;
    width: 100%;
    box-sizing: border-box;
  }
  .inv-card-header {
    width: auto;
    flex: 1;
    min-width: 0;
    margin-right: auto;
  }
  .inv-card-name {
    font-size: 0.85rem;
    white-space: normal;
    line-height: 1.2;
    word-break: break-word;
  }
  .inv-card-controls {
    width: auto;
    flex-shrink: 0;
    gap: 6px;
    padding: 4px;
    background: #f8fbff;
    border: 1px solid rgba(37, 99, 235, 0.1);
  }
  .inv-btn-dec, .inv-btn-inc {
    width: 26px;
    height: 26px;
    font-size: 0.9rem;
  }
  .inv-qty-display {
    min-width: 12px;
    font-size: 0.9rem;
  }
  .calc-inv-card.active-item .inv-card-controls {
    background: rgba(37, 99, 235, 0.12);
    border-color: transparent;
  }
}
"""

if old_styles in css:
    css = css.replace(old_styles, new_styles)
else:
    # If the exact string didn't match, just append it
    css += new_styles

with open("assets/css/storage-calculator.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied ultra-robust mobile flex patch.")
