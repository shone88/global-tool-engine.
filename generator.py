import os

# TVOJ ADSENSE KOD (Verifikovan tvoj ca-pub ID)
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9205810258768369"
     crossorigin="anonymous"></script>
"""

# MASTER BAZA PODATAKA - Ovo su "long-tail" ključne reči koje donose pare
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
    {"name": "Freelance Net Income Calculator", "rate": 0.70, "slug": "net-income-calc"},
    {"name": "Austria Income Tax 2026", "rate": 0.35, "slug": "austria-tax"},
    {"name": "Poland B2B Tax Calculator", "rate": 0.12, "slug": "poland-b2b-calc"},
    {"name": "Dubai Company Setup Fee", "rate": 5000, "slug": "dubai-setup-calc"},
    {"name": "USA Sales Tax Estimator", "rate": 0.08, "slug": "usa-sales-tax"},
    {"name": "France Wealth Tax 2026", "rate": 0.015, "slug": "france-wealth-tax"},
    {"name": "Norway Carbon Tax 2026", "rate": 0.07, "slug": "norway-carbon-tax"},
    {"name": "Spain Property Tax (IBI)", "rate": 0.011, "slug": "spain-property-tax"},
    {"name": "Sweden Luxury Car Tax", "rate": 0.20, "slug": "sweden-car-tax"},
    {"name": "Switzerland Dividend Tax", "rate": 0.35, "slug": "swiss-dividend-calc"},
    {"name": "Ireland Exit Tax Crypto", "rate": 0.33, "slug": "ireland-exit-tax"},
    {"name": "RAPID Robot Path Offset", "rate": 1.0, "slug": "rapid-offset-calc"},
    {"name": "Python Automation Efficiency", "rate": 0.95, "slug": "python-efficiency"},
    {"name": "Global Inflation Estimator", "rate": 1.04, "slug": "global-inflation"},
    {"name": "Gold Import Duty India", "rate": 0.15, "slug": "india-gold-duty"},
    {"name": "Singapore GST 2026", "rate": 0.09, "slug": "singapore-gst-calc"},
    {"name": "Netherlands Box 3 Tax", "rate": 0.36, "slug": "netherlands-box3"},
    {"name": "Portugal Crypto Tax 2026", "rate": 0.28, "slug": "portugal-crypto-tax"},
    {"name": "Belgium Energy Surcharge", "rate": 0.15, "slug": "belgium-energy-calc"},
    {"name": "Canada Federal Tax 2026", "rate": 0.15, "slug": "canada-federal-tax"},
    {"name": "Australia Superannuation Calc", "rate": 0.11, "slug": "aus-super-calc"}
]

template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{name}} | Free Professional 2026 Tool</title>
    {adsense_code}
    <style>
        body {{ font-family: 'Courier New', monospace; background: #000; color: #39FF14; padding: 20px; text-align: center; }}
        .container {{ border: 2px solid #39FF14; padding: 30px; display: inline-block; box-shadow: 10px 10px 0px #1A1A1A; max-width: 90%; }}
        input {{ background: #111; border: 1px solid #39FF14; color: #39FF14; padding: 15px; margin: 10px; font-size: 1.2em; width: 80%; }}
        button {{ background: #39FF14; color: #000; border: none; padding: 15px 30px; cursor: pointer; font-weight: bold; font-size: 1.1em; width: 80%; }}
        button:hover {{ background: #32CD32; }}
        .links {{ margin-top: 30px; text-align: left; }}
        a {{ color: #39FF14; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{{name}}</h1>
        <p>Real-time 2026 algorithm for instant calculation.</p>
        <hr style="border: 0.5px solid #39FF14;">
        <br>
        <input type="number" id="inp" placeholder="Enter value (e.g. 1000)">
        <br>
        <button onclick="run()">EXECUTE CALCULATION</button>
        <h2 id="out" style="margin-top: 20px;">RESULT: --</h2>
    </div>
    <div class="links">
        <a href="index.html">← Back to Dashboard</a>
    </div>
    <script>
        function run() {{
            let v = document.getElementById('inp').value;
            if(v) {{
                let r = (v * {{rate}}).toFixed(2);
                document.getElementById('out').innerText = "RESULT: " + r;
            }}
        }}
    </script>
</body>
</html>
"""

def build():
    if not os.path.exists('public'): os.makedirs('public')
    for item in data:
        content = template.format(name=item['name'], rate=item['rate'])
        with open(f"public/{{item['slug']}}.html", "w", encoding="utf-8") as f:
            f.write(content)
    
    # Glavna index stranica
    with open("public/index.html", "w", encoding="utf-8") as f:
        links = "".join([f'<li><a href="{{i["slug"]}}.html">{{i["name"]}}</a></li>' for i in data])
        f.write(f"""
        <html>
        <head>
            {adsense_code}
            <title>Global Asset Engine 2026</title>
            <style>
                body {{ background:#000; color:#39FF14; font-family:monospace; padding:50px; }}
                a {{ color:#39FF14; text-decoration:none; }}
                li {{ line-height: 2.5; font-size: 1.2em; border-bottom: 1px solid #222; }}
                li:hover {{ background: #111; }}
            </style>
        </head>
        <body>
            <h1>GLOBAL ASSET ENGINE 2026</h1>
            <p>Automated micro-calculators for global industries.</p>
            <hr>
            <ul style='list-style:none; padding:0;'>{links}</ul>
        </body>
        </html>
        """)

if __name__ == "__main__":
    build()
