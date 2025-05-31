from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '🧠 Lumos está funcionando com Flask!'

if __name__ == '__main__':
    app.run(debug=True)
