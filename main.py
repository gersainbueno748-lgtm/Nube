from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Microservicio Flask funcionando en Render 🚀"

if __name__ == "__main__":
    # Esto se usa solo cuando corres localmente (python main.py)
    app.run(host="0.0.0.0", port=5000)
