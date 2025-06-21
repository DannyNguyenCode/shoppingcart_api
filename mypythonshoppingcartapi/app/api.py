from flask import Blueprint, request, jsonify
from app.db import SessionLocal, engine
from sqlalchemy.exc import IntegrityError
from app import crud, models,services
from app.logic import company_logic,category_logic,product_logic,user_logic,address_logic,cart_logic,cart_item_logic,payment_method_logic,order_logic,order_item_logic,shipping_logic,invoice_logic

models.Base.metadata.create_all(bind=engine)
api_flask = Blueprint("api", __name__)

# ============ company ============


@api_flask.route("/companies/create",methods=["POST"])
def create_company():
    try:
        data = request.get_json()
        response, status = company_logic.create_company_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400



@api_flask.route("/companies", methods=["GET"])
def list_companies():
    try:
        response, status = company_logic.list_companies_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400 

@api_flask.route("/companies/<int:id>",methods=["GET"])
def get_company_by_id(id):
    try:
        response, status = company_logic.get_company_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/companies/<int:id>/update", methods=["PUT"])
def update_company(id):
    try:
        data = request.get_json()
        response, status = company_logic.update_company_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/companies/<int:id>/delete",methods=["DELETE"])
def delete_company(id):
    try:
        response, status = company_logic.delete_company_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


# ============ category ============


@api_flask.route("/categories/create",methods=["POST"])
def create_category():
    try:
        data = request.get_json()
        response, status = category_logic.create_category_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

    
@api_flask.route("/categories",methods=["GET"])
def list_categories():
    try:
        response, status = category_logic.list_categories_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/categories/<int:id>",methods=["GET"])
def get_category_by_id(id):
    try:
        response, status = category_logic.get_category_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/categories/<int:id>/update",methods=["PUT"])
def update_category(id):
    try:
        data=request.get_json()
        category = category_logic.update_category_logic(id,data)
        return jsonify(category),200
    except Exception as error:
        return jsonify({"error":f"{error}"})

@api_flask.route("/categories/<int:id>/delete", methods=["DELETE"])
def delete_category(id):
    try:
        response, status = category_logic.delete_category_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    

# ============ product ============

@api_flask.route("/products/create", methods=["POST"])
def create_product():
    try:
        data = request.get_json()
        response, status = product_logic.create_product_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/products", methods=["GET"])
def list_products():
    try:
        response, status = product_logic.product_list_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    try:
        response, status = product_logic.get_product_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/products/<int:id>/update", methods=["PUT"])
def update_product(id):
    try:
        data = request.get_json()
        response, status = product_logic.update_product_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


@api_flask.route("/products/<int:id>/delete", methods=["DELETE"])
def delete_product(id):
    try:
        response, status = product_logic.delete_product_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    

# ============ user ============
@api_flask.route("/users/create", methods=["POST"])    
def create_user():
    try:
        data = request.get_json()
        response, status = user_logic.create_user_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/users", methods=["GET"])
def list_users():
    try:
        response, status = user_logic.list_users_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    try:
        response, status = user_logic.get_user_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/users/<int:id>/update", methods=["PUT"])
def update_user(id):
    try:
        data = request.get_json()
        response, status = user_logic.update_user_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/users/<int:id>/delete", methods=["DELETE"])
def delete_user(id):
    try:
        response, status = user_logic.delete_user_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    
# ============ address ============

@api_flask.route("/addresses/create", methods=["POST"])
def create_address():
    try:
        data = request.get_json()
        response, status = address_logic.create_address_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/addresses", methods=["GET"])
def list_addresses():
    try:
        response, status = address_logic.list_addresses_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/addresses/<int:id>", methods=["GET"])
def get_address_by_id(id):
    try:
        response, status = address_logic.get_address_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/addresses/<int:id>/update", methods=["PUT"])
def update_address(id):
    try:
        data = request.get_json()
        response, status = address_logic.update_address_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/addresses/<int:id>/delete", methods=["DELETE"])
def delete_address(id):
    try:
        response, status = address_logic.delete_address_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    

# ============ cart ============

@api_flask.route("/carts/create", methods=["POST"])
def create_cart():
    try:
        data = request.get_json()
        response, status = cart_logic.create_cart_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/carts", methods=["GET"])
def list_carts():
    try:
        response, status = cart_logic.list_carts_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/carts/<int:id>", methods=["GET"])
def get_cart_by_id(id):
    try:
        response, status = cart_logic.get_cart_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/carts/<int:id>/update", methods=["PUT"])
def update_cart(id):
    try:
        data = request.get_json()
        response, status = cart_logic.update_cart_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/carts/<int:id>/delete", methods=["DELETE"])
def delete_cart(id):
    try:
        response, status = cart_logic.delete_cart_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400          

# ============ cart_item ============

@api_flask.route("/cart_items/create", methods=["POST"])
def create_cart_item():
    try:
        data = request.get_json()
        response, status = cart_item_logic.create_cart_item_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/cart_items", methods=["GET"])
def list_cart_items():
    try:
        response, status = cart_item_logic.list_cart_items_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/cart_items/<int:id>", methods=["GET"])
def get_cart_item_by_id(id):
    try:
        response, status = cart_item_logic.get_cart_item_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/cart_items/<int:id>/update", methods=["PUT"])
def update_cart_item(id):
    try:
        data = request.get_json()
        response, status = cart_item_logic.update_cart_item_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/cart_items/<int:id>/delete", methods=["DELETE"])
def delete_cart_item(id):
    try:
        response, status = cart_item_logic.delete_cart_item_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400


# ============ payment_method ============

@api_flask.route("/payment_methods/create", methods=["POST"])
def create_payment_method():
    try:
        data = request.get_json()
        response, status = payment_method_logic.create_payment_method_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/payment_methods", methods=["GET"])
def list_payment_methods():
    try:
        response, status = payment_method_logic.list_payment_methods_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/payment_methods/<int:id>", methods=["GET"])
def get_payment_method(id):
    try:
        response, status = payment_method_logic.get_payment_method_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/payment_methods/<int:id>/update", methods=["PUT"])
def update_payment_method(id):
    try:
        data = request.get_json()
        response, status = payment_method_logic.update_payment_method_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/payment_methods/<int:id>/delete", methods=["DELETE"])
def delete_payment_method(id):
    try:
        response, status = payment_method_logic.delete_payment_method_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    

# ============ order ============

@api_flask.route("/orders/create", methods=["POST"])
def create_order():
    try:
        data = request.get_json()
        response, status = order_logic.create_order_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/orders", methods=["GET"])
def list_orders():
    try:
        response, status = order_logic.list_orders_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/orders/<int:id>", methods=["GET"])
def get_order(id):
    try:
        response, status = order_logic.get_order_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/orders/<int:id>/update", methods=["PUT"])
def update_order(id):
    try:
        data = request.get_json()
        response, status = order_logic.update_order_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/orders/<int:id>/delete", methods=["DELETE"])
def delete_order(id):
    try:
        response, status = order_logic.delete_order_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400     

# ============ order_item ============

@api_flask.route("/order_items/create", methods=["POST"])
def create_order_item():
    try:
        data = request.get_json()
        response, status = order_item_logic.create_order_item_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/order_items", methods=["GET"])
def list_order_items():
    try:
        response, status = order_item_logic.list_order_items_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/order_items/<int:id>", methods=["GET"])
def get_order_item(id):
    try:
        response, status = order_item_logic.get_order_item_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/order_items/<int:id>/update", methods=["PUT"])
def update_order_item(id):
    try:
        data = request.get_json()
        response, status = order_item_logic.update_order_item_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/order_items/<int:id>/delete", methods=["DELETE"])
def delete_order_item(id):
    try:
        response, status = order_item_logic.delete_order_item_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    
# ============ shipping ============


@api_flask.route("/shippings/create", methods=["POST"])
def create_shipping():
    try:
        data = request.get_json()
        response, status = shipping_logic.create_shipping_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/shippings", methods=["GET"])
def list_shippings():
    try:
        response, status = shipping_logic.list_shippings_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/shippings/<int:id>", methods=["GET"])
def get_shipping(id):
    try:
        response, status = shipping_logic.get_shipping_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/shippings/<int:id>/update", methods=["PUT"])
def update_shipping(id):
    try:
        data = request.get_json()
        response, status = shipping_logic.update_shipping_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/shippings/<int:id>/delete", methods=["DELETE"])
def delete_shipping(id):
    try:
        response, status = shipping_logic.delete_shipping_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400
    
# ============ invoice ============

@api_flask.route("/invoices/create", methods=["POST"])
def create_invoice():
    try:
        data = request.get_json()
        response, status = invoice_logic.create_invoice_logic(**data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/invoices", methods=["GET"])
def list_invoices():
    try:
        response, status = invoice_logic.list_invoices_logic()
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/invoices/<int:id>", methods=["GET"])
def get_invoice_by_id(id):
    try:
        response, status = invoice_logic.get_invoice_by_id_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/invoices/<int:id>/update", methods=["PUT"])
def update_invoice(id):
    try:
        data = request.get_json()
        response, status = invoice_logic.update_invoice_logic(id, **data)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

@api_flask.route("/invoices/<int:id>/delete", methods=["DELETE"])
def delete_invoice(id):
    try:
        response, status = invoice_logic.delete_invoice_logic(id)
        return jsonify(response), status
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400