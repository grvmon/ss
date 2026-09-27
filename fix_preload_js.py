with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

preload_js = """
// Prevent transition jerk on load
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.body.classList.remove('preload');
    }, 50);
});
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js + "\n" + preload_js)
print("Added preload removal to app.js.")
