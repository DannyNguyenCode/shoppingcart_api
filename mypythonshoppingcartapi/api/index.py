from app.api import api_flask
from flask import Flask,jsonify
from app.swaggerapi import swaggerapp

app = Flask(__name__)

app.register_blueprint(api_flask, url_prefix="/api")
app.register_blueprint(swaggerapp, url_prefix="/docs")


@app.route("/")
def hello():
    return jsonify(message="Hello from Flask on Vercel!")

if __name__ == "__main__":
    app.run(debug=True)
