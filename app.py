from flask import Flask

app = Flask(__name__)

@app.route('/')
def merhaba():
    return "<h1>başardık.</h1>"

if __name__ == '__main__':
    app.run(debug=True)