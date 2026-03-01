from flask import Flask, request, render_template_string

app = Flask(__name__)

# Bu bizim giriş sayfamızın tasarımı (HTML)
HTML_SAYFASI = """
<!DOCTYPE html>
<html>
<head>
    <title>Giriş Yap</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; margin-top: 50px; }
        .login-box { border: 1px solid #ccc; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px #eee; }
        input { display: block; margin-bottom: 10px; padding: 8px; width: 200px; }
        button { width: 100%; padding: 10px; background-color: #0095f6; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Giriş Yap</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def ana_sayfa():
    return render_template_string(HTML_SAYFASI)

@app.route('/login', methods=['POST'])
def login():
    kullanici = request.form.get('username')
    sifre = request.form.get('password')
    
    # Şimdilik bilgileri sadece terminale yazdıralım (Test amaçlı)
    print(f"--- YENİ GİRİŞ DENEMESİ ---")
    print(f"Kullanıcı: {kullanici}")
    print(f"Şifre: {sifre}")
    
    return f"<h1>Sisteme ulaştı!</h1><p>Girilen kullanıcı adı: {kullanici}</p>"

if __name__ == "__main__":
    app.run()