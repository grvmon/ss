import os

files_to_update = ['storage-advisor.js', 'storage-advisor.min.js']
old_token1 = "5b597ab74326550702419ec4a9a08ea15a9ab29f796a40a5a22e8fb7a3c306d8"
new_token1 = "f16e947a58c920d3d9bbb4b80e92c047ca04ed4d68bb240204297c44c42d8001"
old_token2 = "76ff4728564a2c1404c0ec2e90f23d7065dc45c7314781dd4e037041a995e8e3c5ec7a40ca380b2a36b3060fc1e58284"
new_token2 = "e9726bf6b19e499bf582aa195c8e5d128958792568633ff8fe046537f9cb109d26d208f333e4ee6aef5c1bebc25b1097"

for file in files_to_update:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(old_token1, new_token1)
        content = content.replace(old_token2, new_token2)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
