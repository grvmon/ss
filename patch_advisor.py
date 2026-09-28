import re

with open("storage-advisor.js", "r", encoding="utf-8") as f:
    js = f.read()

target_minimized = """    var startMinimized = (typeof window.advisorStartMinimized !== 'undefined') ?
      Boolean(window.advisorStartMinimized) :
      (window.location.pathname.indexOf('storage-calculator') !== -1 ||
       !!document.querySelector('.storage-calculator-section') ||
       !!document.getElementById('ssiCalcApp') ||
       document.body.classList.contains('page-storage-calculator'));"""

replacement = """    var startMinimized = (typeof window.advisorStartMinimized !== 'undefined') ? Boolean(window.advisorStartMinimized) : false;"""

js = js.replace(target_minimized, replacement)

with open("storage-advisor.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Removed all minification constraints.")
