import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

def get_rule(selector):
    match = re.search(r'(?<![a-zA-Z\-])' + re.escape(selector) + r'\s*\{([^}]*)\}', css)
    if not match:
        return {}
    rules = match.group(1)
    props = {}
    for line in rules.split(';'):
        if ':' in line:
            key, val = line.split(':', 1)
            props[key.strip()] = val.strip().replace(' !important', '')
    return props

def format_row(element, name, desktop_props, mobile_props=None):
    d_size = desktop_props.get('font-size', '-')
    d_weight = desktop_props.get('font-weight', '-')
    d_ls = desktop_props.get('letter-spacing', '-')
    d_lh = desktop_props.get('line-height', '-')
    
    if mobile_props:
        m_size = mobile_props.get('font-size', '-')
    else:
        m_size = "-"
        
    return f"| {element} | {name} | {d_size} | {m_size} | W: {d_weight}, LS: {d_ls}, LH: {d_lh} |"

print("| Element | Component Name | Desktop Font Size | Mobile Font Size | Decoration (Weight, Spacing, Height) |")
print("|---|---|---|---|---|")

# Base tags
h1 = get_rule('h1')
h2 = get_rule('h2')
h3 = get_rule('h3')

# Mobile overrides
mobile_h1_h2_match = re.search(r'\.section-header-centered h1,.*?h2\s*\{([^}]*)\}', css, re.DOTALL)
if mobile_h1_h2_match:
    mobile_h2_rules = {}
    for line in mobile_h1_h2_match.group(1).split(';'):
        if ':' in line:
            key, val = line.split(':', 1)
            mobile_h2_rules[key.strip()] = val.strip().replace(' !important', '')
else:
    mobile_h2_rules = {}

sub_p = get_rule('.section-header-centered p')

mobile_p_match = re.search(r'\.section-header-centered p,.*?p\s*\{([^}]*)\}', css, re.DOTALL)
if mobile_p_match:
    mobile_p_rules = {}
    for line in mobile_p_match.group(1).split(';'):
        if ':' in line:
            key, val = line.split(':', 1)
            mobile_p_rules[key.strip()] = val.strip().replace(' !important', '')
else:
    mobile_p_rules = {}

print(format_row('H1', 'Main Page Titles', h1, mobile_h2_rules))
print(format_row('H2', 'All Section Headings', h2, mobile_h2_rules))
print(format_row('H3', 'Large Cards / Inner Titles', h3))
print(format_row('p', 'Section Sub-headings', sub_p, mobile_p_rules))

