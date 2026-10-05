import os

file = 'lead-form.js'
old_token1 = "fedbdee437014154ed2bb16453017bf1804b43155bb724c59474e33ae8f3d9ed"
new_token1 = "f16e947a58c920d3d9bbb4b80e92c047ca04ed4d68bb240204297c44c42d8001"
old_token2 = "5b244f2d61e9bc1a1dd7c8178a8cb743242ac4d88a14ea9a5ea5f84e811f0e0d3d3885fbd8ccbbc43c019981f23d6ba8"
new_token2 = "e9726bf6b19e499bf582aa195c8e5d128958792568633ff8fe046537f9cb109d26d208f333e4ee6aef5c1bebc25b1097"

if os.path.exists(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace(old_token1, new_token1)
    content = content.replace(old_token2, new_token2)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
