from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Bienvenue sur l'API test !")

def api_start():
    app.run()
