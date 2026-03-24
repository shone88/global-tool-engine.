import os

# TVOJ ADSENSE KOD
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9205810258768369"
     crossorigin="anonymous"></script>
"""

# BAZA PODATAKA
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
    {"name": "Freelance Net Income Calculator", "rate": 0.70, "slug": "net-income-calc"}
]

# Obrati paznju: Koristimo {{ }} za CSS i JS da Python ne bi prijavio gresku
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} | Free 2026 Tool</title>
    {adsense}
    <style>
        body {{ font-family: monospace; background: #000; color: #39FF14; padding: 50px; text-align: center; }}
        .container {{ border: 2px solid #39FF14; padding: 30px; display: inline-block; }}
        input {{ background: #111; border: 1px solid #39FF14; color: #39FF14; padding: 10px; margin: 10px; }}
        button {{ background: #39FF14; color: #000; border: none; padding: 10px 20px; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{name}</h1>
        <input type="number" id="inp" placeholder="0.00">
        <button onclick="run()">CALCULATE</button>
        <h2 id="out">Result: --</h2>
    </div>
    <script>
        function run() {{
            let v = document.getElementById('inp').value;
            let res = (v * {rate}).toFixed(2);
            document.getElementById('out').innerText = "Result: " + res;
        }}
    </script>
</body>
</html>
"""

def build():
    if not os.path.exists('public'): os.makedirs('public')
    for item in data:
        # Prosledjujemo vrednosti u template
        content = template.format(
            name=item['name'], 
            rate=item['rate'], 
            adsense=adsense_code
        )
        with open(f"public/{item['slug']}.html", "w", encoding="utf-8") as f:
            f.write(content)
    
    # Generisanje pocetne strane
    with open("public/index.html", "w", encoding="utf-8") as f:
        links = "".join([f'<li><a href="{i["slug"]}.html" style="color:#39FF14">{i["name"]}</a></li>' for i in data])
        f.write(f"<html><head>{adsense_code}</head><body style='background:#000;color:#39FF14;font-family:monospace;'><h1>Asset Engine 2026</h1><hr><ul>{links}</ul></body></html>")

if __name__ == "__main__":
    build()
