with open("lead-form.min.js", "r", encoding="utf-8") as f:
    content = f.read()

# Swap tokens
content = content.replace("3719eaafdcaf84c2c122c957b23371a7ed8c735cc2fc4dc3c4234898eab5058e", "ab2c0d137452c6e44d4ab49aaf9d107d0881349743d2338ac3e06be64f6329b8")
content = content.replace("79d3731cf6d5263fe25ca7b3f44f6c0d42399f0924164df81f6e37141a5c3a7a99d60f9e5782124ac0715631e04021ff", "91ea25b27e38c66119c317f8814dd4df415a342fbb82279dc17fac58adca3bd871658a8b2696c9081e5b822911055b5b")

# Inject recaptcha check
search_str = 'L.append("fclid",uf);try{'
inject_str = 'L.append("fclid",uf);var _gr=document.getElementById("g-recaptcha-response");if(_gr&&_gr.value){L.append("g-recaptcha-response",_gr.value)}else{b&&(b.classList.add("lf-show"),b.textContent="Please complete the robot check.");M&&(M.disabled=!1,M.classList.remove("lf-loading"));D&&(D.textContent="Request Callback");clearTimeout(X);H=!1;return}try{'
content = content.replace(search_str, inject_str)

with open("lead-form.min.js", "w", encoding="utf-8") as f:
    f.write(content)
print("JS Patched!")
