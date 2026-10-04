with open("lead-form.min.js", "r", encoding="utf-8") as f:
    content = f.read()

# Swap tokens
content = content.replace("ab90d9124bda14347cdea243b8cd62234c61df6ed89b9d37ec7a8b5ecd033eaa", "c6eb63f6236417682faed4a4b1e543deb24e980554474aadc6154b75e0dfdcb5")
content = content.replace("6aa318a3320f1b0607908f79e477e5b26120ae8a8442240da64c1bb2942bd6ab212b9a280ddf65cf2dbed3a61f3cfb83", "1c727e96dbfbb6c6d7b69df02c0bf8c3d062a16f4b987fb5d78cf4d6426d299bc5fad13f2c784a33a9182cc807619d30")

# Inject recaptcha check
search_str = 'L.append("fclid",uf);try{'
inject_str = 'L.append("fclid",uf);var _gr=document.getElementById("g-recaptcha-response");if(_gr&&_gr.value){L.append("g-recaptcha-response",_gr.value)}else{b&&(b.classList.add("lf-show"),b.textContent="Please complete the robot check.");M&&(M.disabled=!1,M.classList.remove("lf-loading"));D&&(D.textContent="Request Callback");clearTimeout(X);H=!1;return}try{'
content = content.replace(search_str, inject_str)

with open("lead-form.min.js", "w", encoding="utf-8") as f:
    f.write(content)
print("JS Patched!")
