import re

with open("household-goods-storage/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove existing schema scripts
html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL)

# Build unified schema graph
unified_schema = """
    <!-- SCHEMA GRAPH -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://selfstorageindia.com/#organization",
          "name": "Self Storage India",
          "url": "https://selfstorageindia.com/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://selfstorageindia.com/wp-content/uploads/2025/07/Self-Storage-India-Logo.png",
            "width": 300,
            "height": 60
          },
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+91-9090206090",
            "contactType": "customer service",
            "areaServed": "IN",
            "availableLanguage": ["en", "hi"]
          }
        },
        {
          "@type": "WebPage",
          "@id": "https://selfstorageindia.com/household-goods-storage/#webpage",
          "url": "https://selfstorageindia.com/household-goods-storage/",
          "name": "Household Goods Storage in Delhi NCR | Self Storage India",
          "description": "Rent secure temporary household & furniture storage in Delhi, Gurugram & Noida. Ideal for renovation & moving with 24/7 CCTV & transport.",
          "isPartOf": {
            "@id": "https://selfstorageindia.com/#organization"
          }
        },
        {
          "@type": "Service",
          "@id": "https://selfstorageindia.com/household-goods-storage/#service",
          "name": "Household Goods & Furniture Storage in Delhi NCR",
          "serviceType": "Household Storage",
          "provider": {
            "@id": "https://selfstorageindia.com/#organization"
          },
          "areaServed": [
            { "@type": "City", "name": "Delhi" },
            { "@type": "City", "name": "Gurugram" },
            { "@type": "City", "name": "Noida" }
          ],
          "description": "Clean, secure, pest-controlled temporary household storage and short-term furniture rooms across Delhi NCR for home renovation, house relocation, and short-term stay.",
          "mainEntityOfPage": {
            "@id": "https://selfstorageindia.com/household-goods-storage/#webpage"
          }
        },
        {
          "@type": "BreadcrumbList",
          "@id": "https://selfstorageindia.com/household-goods-storage/#breadcrumb",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://selfstorageindia.com/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Household Goods Storage",
              "item": "https://selfstorageindia.com/household-goods-storage/"
            }
          ]
        },
        {
          "@type": "FAQPage",
          "@id": "https://selfstorageindia.com/household-goods-storage/#faq",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "Can I rent temporary storage for home renovation or house painting?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes! We specialize in temporary furniture storage during house painting, modular kitchen renovation, or full home remodeling. Keep your sofas, beds, TVs, and wooden furniture 100% dust-free and safe in private lockable rooms."
              }
            },
            {
              "@type": "Question",
              "name": "What is the minimum rental duration for temporary relocation storage?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Our minimum rental term is just 30 days on flexible month-to-month plans. You can extend your temporary storage room for as long as your home relocation, construction, or travel abroad requires without long-term contracts."
              }
            },
            {
              "@type": "Question",
              "name": "How does Self Storage India work?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Select your desired room size, pack your items (or request our team's help), and move them in. You lock the room and keep the key, ensuring complete privacy and exclusive access."
              }
            },
            {
              "@type": "Question",
              "name": "What can I store in household storage?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "You can store household furniture, appliances, electronics, luggage, and packed boxes. Prohibited items include hazardous, illegal, or perishable goods."
              }
            },
            {
              "@type": "Question",
              "name": "How secure are my belongings?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Our facilities feature 24/7 CCTV surveillance, perimeter alarms, secure access control, fire safety measures, and on-site security guards. You hold the only key to your lock."
              }
            },
            {
              "@type": "Question",
              "name": "Can I access my storage whenever I need?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes! We offer easy access 7 days a week during our extended operating hours, allowing you to retrieve or add items whenever it's convenient."
              }
            },
            {
              "@type": "Question",
              "name": "Do you provide packing and transport assistance in Delhi NCR?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes! While Self Storage India focuses on providing secure self-storage units, we partner with reliable third-party logistics and moving providers who can assist with professional packing and door-to-door transport."
              }
            },
            {
              "@type": "Question",
              "name": "Is insurance available?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes, we offer flexible insurance options to protect your stored goods against unforeseen events, giving you complete peace of mind."
              }
            },
            {
              "@type": "Question",
              "name": "What storage sizes are available?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "We offer a wide range of unit sizes, from small lockers for personal items or documents, up to large rooms capable of storing 3BHK+ households."
              }
            }
          ]
        }
      ]
    }
    </script>
"""

# Insert schema just before </head>
html = html.replace('</head>', unified_schema + '\n</head>')

with open("household-goods-storage/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Schema unified and updated.")
