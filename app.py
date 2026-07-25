from sys import version

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Server is alive"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/about")
def about():
    return jsonify({"name": "Rayna Lyn Rupita", "role": "Backend Intern"})

@app.route("/contact")
def contact():
    return jsonify({"email": "r5@gmail.com", "linkedIn": "Rayna Lyn A. Rupita"})

@app.route("/status")
def status():
    return jsonify({"service": "smallest-backend", "uptime_check":"ok", "version":"1.0.0"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)