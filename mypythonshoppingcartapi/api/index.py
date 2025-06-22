from flask import Flask, jsonify
from flask_smorest import Api
from app.api import api_flask  # existing Flask routes
from app.swaggerapi import company_blp,category_blp,product_blp,user_blp,address_blp,cart_blp,cart_item_blp,payment_method_blp,order_blp,order_item_blp,shipping_blp,invoice_blp  # smorest blueprint

app = Flask(__name__)
app.config["API_TITLE"] = "Shopping Cart API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
app.register_blueprint(api_flask, url_prefix="/api")  # existing routes
api.register_blueprint(company_blp)  # new smorest-based API
api.register_blueprint(category_blp)
api.register_blueprint(product_blp)
api.register_blueprint(user_blp)
api.register_blueprint(address_blp)
api.register_blueprint(cart_blp)
api.register_blueprint(cart_item_blp)
api.register_blueprint(payment_method_blp)
api.register_blueprint(order_blp)
api.register_blueprint(order_item_blp)
api.register_blueprint(shipping_blp)
api.register_blueprint(invoice_blp)

if __name__ == "__main__":
    app.run(debug=True)
