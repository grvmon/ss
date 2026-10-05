import os

for file in ['lead-form.js', 'lead-form.min.js', 'storage-advisor.js', 'storage-advisor.min.js']:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('Connecting with Advisor...', 'Connecting with Advisor…')
        content = content.replace('Requesting...', 'Requesting…')
        content = content.replace('Loading...', 'Loading…')
        content = content.replace('Submitting...', 'Submitting…')
        content = content.replace('Please wait...', 'Please wait…')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
print("JS typography fixed.")
