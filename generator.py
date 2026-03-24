import os

# 1. TVOJ ADSENSE PODACI
adsense_id = "ca-pub-9205810258768369"
adsense_code = f"""
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={adsense_id}"
     crossorigin="anonymous"></script>
"""

# TVOJ GLAVNI DOMEN (Obavezno za Sitemap)
base_url = "https://global-tool-engine.vercel.app"

# 2. BAZA PODATAKA
data = [
    {"name": "Customs Duty Serbia 2026", "rate": 0.10, "slug": "carina-srbija-2026"},
    {"name": "Germany Freelance Tax 2026", "rate": 0.19, "slug": "germany-tax-calc"},
    {"name": "Crypto Profit Tax Croatia", "rate": 0.12, "slug": "crypto-tax-cro"},
    {"name": "3D Printing Material Cost", "rate": 1.25, "slug": "3d-filament-calc"},
    {"name": "Estonia VAT 2026", "rate": 0.22, "slug": "ee-vat-2026"},
    {"name": "CNC Machining Hourly Rate", "rate": 45.0, "slug": "cnc-rate-calc"},
    {"name": "UK Corporation Tax 2026", "rate": 0.25, "slug": "uk-corp-tax"},
    {"name": "Solar Panel ROI Calculator", "rate": 0.85, "slug": "solar-roi"},
    {"name": "Italy Digital Nomad Tax", "rate": 0.05, "slug": "italy-nomad-tax"},
    {"name": "ChatGPT API Cost Estimator", "rate": 0.002, "slug": "ai-api-cost"},
    {"name": "Dubai Real Estate Tax", "rate": 0.04, "slug": "dubai-property-tax"},
    {"name": "Gold Import Duty India", "rate": 0.15, "slug": "india-gold-duty"},
    {"name": "Switzerland Dividend Tax", "rate": 0.35, "slug": "swiss-tax-calc"},
    {"name": "Norway Carbon Tax 2026", "rate": 0.07, "slug": "norway-carbon-tax"},
    {"name": "Freelance VAT Montenegro", "rate": 0.21, "slug": "cg-pdv-calc"},
    {"name": "Tesla Supercharger Cost Est.", "rate": 0.45, "slug": "ev-charge-cost"}
]

# 3. HTML TEMPLATE
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Free Professional 2026 Tool</title>
    {adsense}
    <style>
        body {{ font-family: 'Courier New', monospace; background: #000; color: #39FF14; padding: 20px; text-align: center; }}
        .container {{ border: 2px solid #39FF14; padding: 30px; display: inline-block; box-shadow: 10px 10px 0px #1A1A1A; max-width: 600px; }}
        input {{ background: #111; border: 1px solid #39FF14; color: #39FF14; padding: 15px; margin: 10px; font-size: 1.2em; width: 80%; }}
        button {{ background: #39FF14; color: #000; border: none; padding: 15px 30px; cursor: pointer; font-weight: bold; width: 80%; }}
        .links {{ margin-top: 30px; font-size: 0.8em; }}
        a {{ color: #39FF14; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{name}</h1>
        <p>Official 2026 Industry Algorithm</p>
        <hr style="border: 0.5px solid #39FF14;">
        <input type="number" id="inp" placeholder="Enter amount...">
        <br>
        <button onclick="run()">RUN CALCULATION</button>
        <h2 id="out" style="margin-top: 20px;">RESULT: --</h2>
    </div>
    <div class="links">
        <a href="index.html">Main Dashboard</a> | <a href="privacy.html">Privacy Policy</a>
    </div>
    <script>
        function run() {{
            let v = document.getElementById('inp').value;
            if(v) {{
                let r = (v * {rate}).toFixed(2);
                document.getElementById('out').innerText = "RESULT: " + r;
            }}
        }}
    </script>
</body>
</html>
"""

def build():
    if not os.path.exists('public'): os.makedirs('public')
    
    # 4. ADS.TXT
    with open("public/ads.txt", "w", encoding="utf-8") as f:
        f.write(f"google.com, {adsense_id.replace('ca-', '')}, DIRECT, f08c47fec0942fa0")
    
    # 5. SITEMAP.XML (NOVO - Za Google indeksiranje)
    sitemap_entries = [f"<url><loc>{base_url}/index.html</loc></url>", f"<url><loc>{base_url}/privacy.html</loc></url>"]
    
    # 6. GENERISANJE STRANICA I SITEMAP ULAZA
    for item in data:
        content = template.format(name=item['name'], rate=item['rate'], adsense=adsense_code)
        with open(f"public/{item['slug']}.html", "w", encoding="utf-8") as f:
            f.write(content)
        sitemap_entries.append(f"<url><loc>{base_url}/{item['slug']}.html</loc></url>")
    
    with open("public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{" ".join(sitemap_entries)}</urlset>')

    # 7. INDEX I PRIVACY (Standardno)
    links = "".join([f'<li><a href="{i["slug"]}.html">{i["name"]}</a></li>' for i in data])
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(f"<html><head>{adsense_code}<style>body{{background:#000;color:#39FF14;font-family:monospace;padding:50px;}}a{{color:#39FF14;text-decoration:none;}}</style></head><body><h1>GLOBAL ENGINE 2026</h1><hr><ul style='list-style:none;padding:0;'>{links}</ul><br><a href='privacy.html' style='font-size:0.8em;'>Privacy Policy</a></body></html>")
    
    with open("public/privacy.html", "w", encoding="utf-8") as f:
        f.write(f"<html><body style='background:#000;color:#39FF14;font-family:monospace;padding:50px;'><h1>Privacy Policy</h1><p>We use Google AdSense. No personal data collected.</p><a href='index.html' style='color:#39FF14'>Back</a></body></html>")

if __name__ == "__main__":
    build()
