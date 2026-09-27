import re

with open("storage-advisor.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the setTimeout and onFirstScroll block
pattern = r"/\* Timed entrance animation - smooth, prompt 350ms entrance \*/.*?window\.addEventListener\(\"scroll\", onFirstScroll, \{ passive: true \}\);"
replacement = """/* Show only after scrolling past the first fold (approx 400px or half screen height) */
    var handleScrollVisibility = function() {
      if (floatingUnit) {
        if (window.scrollY > Math.min(window.innerHeight * 0.5, 400)) {
          if (!floatingUnit.classList.contains("is-visible")) {
            floatingUnit.classList.add("is-visible");
          }
        } else {
          if (floatingUnit.classList.contains("is-visible")) {
            floatingUnit.classList.remove("is-visible");
          }
        }
      }
    };
    window.addEventListener("scroll", handleScrollVisibility, { passive: true });
    // Run once on load just in case they load halfway down the page
    handleScrollVisibility();"""

new_js = re.sub(pattern, replacement, js, flags=re.DOTALL)

with open("storage-advisor.js", "w", encoding="utf-8") as f:
    f.write(new_js)
print("JS updated.")
