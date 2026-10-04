with open("lead-form.min.js", "r", encoding="utf-8") as f:
    content = f.read()

# Swap tokens
content = content.replace("c6eb63f6236417682faed4a4b1e543deb24e980554474aadc6154b75e0dfdcb5", "3719eaafdcaf84c2c122c957b23371a7ed8c735cc2fc4dc3c4234898eab5058e")
content = content.replace("1c727e96dbfbb6c6d7b69df02c0bf8c3d062a16f4b987fb5d78cf4d6426d299bc5fad13f2c784a33a9182cc807619d30", "79d3731cf6d5263fe25ca7b3f44f6c0d42399f0924164df81f6e37141a5c3a7a99d60f9e5782124ac0715631e04021ff")

# Remove recaptcha check
search_str = 'L.append("fclid",uf);var _gr=document.getElementById("g-recaptcha-response");if(_gr&&_gr.value){L.append("g-recaptcha-response",_gr.value)}else{b&&(b.classList.add("lf-show"),b.textContent="Please complete the robot check.");M&&(M.disabled=!1,M.classList.remove("lf-loading"));D&&(D.textContent="Request Callback");clearTimeout(X);H=!1;return}try{'
replace_str = 'L.append("fclid",uf);try{'
content = content.replace(search_str, replace_str)

with open("lead-form.min.js", "w", encoding="utf-8") as f:
    f.write(content)
print("JS Reverted!")
