from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    # Integração com o bot (usando Flask)
    data = request.json
    # Processar mensagens...
    return "OK"

if __name__ == "__main__":
    app.run(port=5000)