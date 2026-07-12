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

if __name__ == "__main__":
    app.run(debug=True, port=5000)