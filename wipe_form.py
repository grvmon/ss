import os
import re

SKIP_DIRS = {'.git', 'assets', 'node_modules'}

def process_html():
    files_modified = 0
    
    zoho_script = "<script id='formScript932919000016189095' src='https://crm.zoho.in/crm/WebFormServeServlet?rid=f87f8ad958187952ffcd4e53a71bd02b3b10fd47f0a7fe3ca0f02ccd9630a38accfd1d3b4dad84fe060ca2a20956f8b7gid7d8117022dc9d72282644cd246251f5f80dfb5e9e000c7ad27a77e7682edbcf8&script=$sYG'></script>"
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original_content = content
                
                # Regex to match the entire form
                # From <form class="lf-form" id="lfForm" ...> up to the closing </form> for lfForm
                pattern = re.compile(r'<form class="lf-form" id="lfForm".*?</form>', re.DOTALL)
                
                # Replace with the Zoho script
                content = re.sub(pattern, zoho_script, content)
                
                # Remove google recaptcha api.js from head since Zoho script injects its own if needed
                content = content.replace('<script src="https://www.google.com/recaptcha/api.js" async defer></script>\n', '')
                
                # Remove the g-recaptcha div we injected earlier just in case it's floating
                content = re.sub(r'<div class="g-recaptcha"[^>]+></div>', '', content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_modified += 1
                    
    print(f"Replaced custom form with Zoho script in {files_modified} HTML files.")

if __name__ == '__main__':
    process_html()
