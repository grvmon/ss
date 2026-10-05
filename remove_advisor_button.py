import os
import re

button_pattern = re.compile(r'<button class="btn btn-primary" onclick="if \(window\.openAdvisorModal\) \{ window\.openAdvisorModal\(\); \} else \{ openQuoteModal\(\'?.*?\'?\); \}">Talk to an Advisor</button>')

def process_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') or file.endswith('.txt'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = button_pattern.sub('', content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

process_dir('/Users/gauravmongia/Desktop/SSI')
print("Done")
