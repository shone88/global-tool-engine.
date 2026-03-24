import os

# Ovo je tvoja baza podataka. Ovde cemo kasnije dodati skraper da sam puni listu.
data = [
    {"name": "Customs Duty Calculator Serbia 2026", "rate": 0.10, "slug": "carina-srbija-2026"},
    {"name": "Germany Freelance Tax Estimator", "rate": 0.19, "slug": "germany-tax-calc"},
    {"name": "Crypto Profit Tax - Croatia", "rate": 0.12, "slug": "crypto-tax-cro"},
    {"name": "3D Printing Filament Usage Calc", "rate": 1.25, "slug": "3d-filament-calc"}
]

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} | Free Online Tool</title>
    <style>
        body {{ font-family: 'Courier New', monospace; background: #1a1a1a; color: #00ff00; padding: 50px; text-align: center; }}
        .container {{ border: 1px solid #00ff00; padding: 30px; display: inline-block; box-shadow: 5px 5px 0px #00ff00; }}
        input {{ background: #000; border: 1px solid #00ff00; color: #00ff00; padding: 10px; margin: 10px; }}
        button {{ background: #00ff00; color: #000; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{name}</h1>
        <p>Enter your value to get an instant 2026 estimate:</p>
        <input type="number" id="inp" placeholder="0.00">
        <button onclick="run()">CALCULATE</button>
        <h2 id="out">Result: --</h2>
    </div>
    <script>
        function run() {{
            let v = document.getElementById('inp').value;
            document.getElementById('out').innerText = "Result: " + (v * {rate}).toFixed(2);
        }}
    </script>
</body>
</html>
"""

def build():
    if not os.path.exists('public'): os.makedirs('public')
    for item in data:
        content = template.format(name=item['name'], rate=item['rate'])
        with open(f"public/{item['slug']}.html", "w", encoding="utf-8") as f:
            f.write(content)
    
    # Pravimo glavnu stranu (Index)
    with open("public/index.html", "w", encoding="utf-8") as f:
        links = "".join([f'<li><a href="{i["slug"]}.html" style="color:#00ff00">{i["name"]}</a></li>' for i in data])
        f.write(f"<html><body style='background:#1a1a1a;color:#00ff00;font-family:monospace;'><h1>Tool Hub 2026</h1><ul>{links}</ul></body></html>")

if __name__ == "__main__":
    build()
