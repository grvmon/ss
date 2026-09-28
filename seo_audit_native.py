import json
from html.parser import HTMLParser

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.images = []
        self.schemas = []
        self.in_script = False
        self.current_script_type = ""
        self.current_script_content = ""
        self.current_heading = None
        self.current_heading_text = ""

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.current_heading = tag
            self.current_heading_text = ""
            
        if tag == 'img':
            self.images.append({
                'src': attr_dict.get('src', ''),
                'alt': attr_dict.get('alt', 'MISSING'),
                'title': attr_dict.get('title', 'MISSING')
            })
            
        if tag == 'script':
            self.in_script = True
            self.current_script_type = attr_dict.get('type', '')
            self.current_script_content = ""

    def handle_data(self, data):
        if self.current_heading:
            self.current_heading_text += data
            
        if self.in_script and self.current_script_type == 'application/ld+json':
            self.current_script_content += data

    def handle_endtag(self, tag):
        if tag == self.current_heading:
            self.headings.append({
                'tag': tag.upper(),
                'text': self.current_heading_text.strip().replace('\\n', ' ')
            })
            self.current_heading = None
            
        if tag == 'script':
            self.in_script = False
            if self.current_script_type == 'application/ld+json' and self.current_script_content.strip():
                try:
                    schema_data = json.loads(self.current_script_content)
                    self.schemas.append(schema_data)
                except Exception as e:
                    pass

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

parser = SEOParser()
parser.feed(html)

print("=== HEADINGS ===")
for h in parser.headings:
    print(f"{h['tag']}: {h['text']}")

print("\n=== IMAGES ===")
for img in parser.images:
    print(f"IMG: {img['src']} | ALT: {img['alt']} | TITLE: {img['title']}")

print("\n=== SCHEMAS ===")
for s in parser.schemas:
    print(json.dumps(s, indent=2))
