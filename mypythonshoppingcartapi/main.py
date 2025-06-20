from app.api import app
from flask import Flask
from app.api import app
from app.swaggerapi import swaggerapp

application = Flask(__name__)

application.register_blueprint(app, url_prefix="/api")
application.register_blueprint(swaggerapp, url_prefix="/docs")

if __name__ == "__main__":
    application.run(debug=True)
