from flask import Blueprint,jsonify
from flask_restx import Api, Resource,fields
from app.logic import company_logic,category_logic,product_logic,user_logic,address_logic,cart_logic,cart_item_logic,payment_method_logic,order_logic,order_item_logic,shipping_logic,invoice_logic

swaggerapp = Blueprint("swagger", __name__)
api = Api(swaggerapp, version="1.0", title="Shopping Cart API", description="API with Swagger UI")

# ============ company ============
company_ns = api.namespace("companies", description="Company operations")
company_model = api.model("Company", {
    "id": fields.Integer(required=True, description="Company ID"),
    "name": fields.String(required=False, description="Company name")
})

@company_ns.route("/")
class CompanyList(Resource):
    @company_ns.expect(company_model)
    @company_ns.doc("create_company")

    def post(self):
        try:
            data = api.payload
            response,status =company_logic.create_company_logic(**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
    @company_ns.doc("list_companies")
    def get(self):
        try:
            response,status = company_logic.list_companies_logic()
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
    

@company_ns.route("/<int:id>")
@company_ns.param('id', 'The company identifier')
class Company(Resource):
    @company_ns.doc("get_company_by_id")
    def get(self,id):
        try:
            response,status = company_logic.get_company_by_id_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
    @company_ns.expect(company_model)
    @company_ns.doc("update_company")
    def put(self,id):
        try:
            data = api.payload
            response,status = company_logic.update_company_logic(id,**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
    
    @company_ns.doc("delete_company")
    def delete(self,id):
        try:
            response,status = company_logic.delete_company_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400

# ============ category ============
category_ns = api.namespace("categories", description="Category operations")
category_model = api.model("Category", {
    "id": fields.Integer(required=True, description="Category ID"),
    "name": fields.String(required=False, description="Category name")
})

@category_ns.route("/")
class CategoryList(Resource):
    @category_ns.expect(category_model)
    @category_ns.doc("create_category")
    def post(self):
        try:
            data = api.payload
            response,status =category_logic.create_category_logic(**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
    @category_ns.doc("list_categories")
    def get(self):
        try:
            response,status = category_logic.list_categories_logic()
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        

@category_ns.route("/<int:id>")
@category_ns.param('id', 'The category identifier')
class Category(Resource):
    @category_ns.doc("get_category_by_id")
    def get(self,id):
        try:
            response,status = category_logic.get_category_by_id_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
    @category_ns.expect(category_model)
    @category_ns.doc("update_category")
    def put(self,id):
        try:
            data = api.payload
            response,status = category_logic.update_category_logic(id,**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
    
    @category_ns.doc("delete_category")
    def delete(self,id):
        try:
            response,status = category_logic.delete_category_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        

 # ============ product ============       

product_ns = api.namespace("products", description="Product operations")
product_model = api.model("Product", {
    "id": fields.Integer(required=True, description="Product ID"),
    "name": fields.String(required=True, description="Product name"),
    "price":fields.Float(required=True, description="Product price"),
    "description":fields.String(required=True, description="Product description"),
    "category_id":fields.Integer(required=True, description="Associated category ID"),
    "stock_quantity":fields.Integer(required=True, description="Quantity in stock"),
    "company_id":fields.Integer(required=True, description="Associated company ID")
})


@product_ns.route("/")
class ProductList(Resource):
    @product_ns.expect(product_model)
    @product_ns.doc("create_product")
    def post(self):
        try:
            data = api.payload
            response,status =product_logic.create_product_logic(**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
    @product_ns.doc("list_products")
    def get(self):
        try:
            response,status = product_logic.product_list_logic()
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        

@product_ns.route("/<int:id>")
@product_ns.param('id', 'The product identifier')
class Product(Resource):
    @product_ns.doc("get_product_by_id")
    def get(self,id):
        try:
            response,status = product_logic.get_product_by_id_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
    @product_ns.expect(product_model)
    @product_ns.doc("update_product")
    def put(self,id):
        try:
            data = api.payload
            response,status = product_logic.update_product_logic(id,**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
    
    @product_ns.doc("delete_product")
    def delete(self,id):
        try:
            response,status = product_logic.delete_product_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"},400
        
# ============ user ============

user_ns = api.namespace("users", description="User operations")

user_model = api.model("User", {
    "id": fields.Integer(required=True, description="User ID"),
    "full_name": fields.String(required=True, description="Full name"),
    "email": fields.String(required=True, description="Email address"),
    "password": fields.String(required=True, description="User password"),
    "phone": fields.String(required=True, description="Phone number")
})

@user_ns.route("/")
class UserList(Resource):
    @user_ns.expect(user_model)
    @user_ns.doc("create_user")
    def post(self):
        try:
            data = api.payload
            response, status = user_logic.create_user_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @user_ns.doc("list_users")
    def get(self):
        try:
            response, status = user_logic.list_users_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


@user_ns.route("/<int:id>")
@user_ns.param('id', 'The user identifier')
class User(Resource):
    @user_ns.doc("get_user_by_id")
    def get(self, id):
        try:
            response, status = user_logic.get_user_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @user_ns.expect(user_model)
    @user_ns.doc("update_user")
    def put(self, id):
        try:
            data = api.payload
            response, status = user_logic.update_user_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @user_ns.doc("delete_user")
    def delete(self, id):
        try:
            response, status = user_logic.delete_user_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

# ============ address ===========

address_ns = api.namespace("addresses", description="Address operations")

address_model = address_ns.model("Address", {
    "id": fields.Integer(required=True, description="Address ID"),
    "street_address": fields.String(required=True, description="Street address"),
    "state": fields.String(required=True, description="State"),
    "postal_code": fields.String(required=True, description="Postal code"),
    "country": fields.String(required=True, description="Country"),
    "user_id": fields.Integer(required=True, description="Associated user ID")
})


@address_ns.route("/")
class AddressList(Resource):
    @address_ns.expect(address_model)
    @address_ns.doc("create_address")
    def post(self):
        try:
            data = address_ns.payload
            response, status = address_logic.create_address_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @address_ns.doc("list_addresses")
    def get(self):
        try:
            response, status = address_logic.list_addresses_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


@address_ns.route("/<int:id>")
@address_ns.param("id", "The address identifier")
class Address(Resource):
    @address_ns.doc("get_address_by_id")
    def get(self, id):
        try:
            response, status = address_logic.get_address_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @address_ns.expect(address_model)
    @address_ns.doc("update_address")
    def put(self, id):
        try:
            data = address_ns.payload
            response, status = address_logic.update_address_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @address_ns.doc("delete_address")
    def delete(self, id):
        try:
            response, status = address_logic.delete_address_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

# ============ cart ============

cart_ns = api.namespace("carts", description="Cart operations")

cart_model = cart_ns.model("Cart", {
    "id": fields.Integer(required=True, description="Cart ID"),
    "user_id": fields.Integer(required=True, description="Associated user ID")
})


@cart_ns.route("/")
class CartList(Resource):
    @cart_ns.expect(cart_model)
    @cart_ns.doc("create_cart")
    def post(self):
        try:
            data = cart_ns.payload
            response, status = cart_logic.create_cart_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_ns.doc("list_carts")
    def get(self):
        try:
            response, status = cart_logic.list_carts_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


@cart_ns.route("/<int:id>")
@cart_ns.param("id", "The cart identifier")
class Cart(Resource):
    @cart_ns.doc("get_cart_by_id")
    def get(self, id):
        try:
            response, status = cart_logic.get_cart_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_ns.expect(cart_model)
    @cart_ns.doc("update_cart")
    def put(self, id):
        try:
            data = cart_ns.payload
            response, status = cart_logic.update_cart_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_ns.doc("delete_cart")
    def delete(self, id):
        try:
            response, status = cart_logic.delete_cart_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400
        
# ============ cart_item ============

cart_item_ns = api.namespace("cart_items", description="Cart item operations")

cart_item_model = cart_item_ns.model("CartItem", {
    "id": fields.Integer(required=True, description="Cart Item ID"),
    "quantity": fields.Integer(required=True, description="Quantity of product"),
    "product_id": fields.Integer(required=True, description="Associated product ID"),
    "cart_id": fields.Integer(required=True, description="Associated cart ID")
})


@cart_item_ns.route("/")
class CartItemList(Resource):
    @cart_item_ns.expect(cart_item_model)
    @cart_item_ns.doc("create_cart_item")
    def post(self):
        try:
            data = cart_item_ns.payload
            response, status = cart_item_logic.create_cart_item_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_item_ns.doc("list_cart_items")
    def get(self):
        try:
            response, status = cart_item_logic.list_cart_items_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


@cart_item_ns.route("/<int:id>")
@cart_item_ns.param("id", "The cart item identifier")
class CartItem(Resource):
    @cart_item_ns.doc("get_cart_item_by_id")
    def get(self, id):
        try:
            response, status = cart_item_logic.get_cart_item_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_item_ns.expect(cart_item_model)
    @cart_item_ns.doc("update_cart_item")
    def put(self, id):
        try:
            data = cart_item_ns.payload
            response, status = cart_item_logic.update_cart_item_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @cart_item_ns.doc("delete_cart_item")
    def delete(self, id):
        try:
            response, status = cart_item_logic.delete_cart_item_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400
        
# ============ payment_method ============

payment_methods_ns = api.namespace("payment_methods", description="Payment method operations")
payment_method_model=payment_methods_ns.model("PaymentMethod",{
    "id":fields.Integer(required=True,description="Payment Method ID"),
    "card_number":fields.String(required=True,description="Card Number"),
    "cvv":fields.Integer(required=True,description="cvv"),
    "expire_date":fields.String(required=True,description="Expire Date"),
    "card_holder_name":fields.String(required=True,description="Card Holder's Name"),
    "user_id":fields.Integer(required=True,description="Associated user ID")
})
@payment_methods_ns.route("/")
class PaymentMethodList(Resource):
    @payment_methods_ns.expect(payment_method_model)
    @payment_methods_ns.doc("create_payment_method")
    def post(self):
        try:
            data = payment_methods_ns.payload
            response,status = payment_method_logic.create_payment_method_logic(**data)
            return response,status

        except Exception as error:
            return {"error": f"{error}"}, 400
    @payment_methods_ns.doc("list_payment_methods")
    def get(self):
        try:
            response,status = payment_method_logic.list_payment_methods_logic()
            return response,status
        
        except Exception as error:
            return {"error": f"{error}"}, 400

@payment_methods_ns.route("/<int:id>")
@payment_methods_ns.param("id", "The payment method identifier")
class PaymentMethod(Resource):
    @payment_methods_ns.doc("get_payment_method_by_id")
    def get(self,id):
        try:
            response,status = payment_method_logic.get_payment_method_by_id_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @payment_methods_ns.expect(payment_method_model)
    @payment_methods_ns.doc("update_payment_method")
    def put(self,id):
        try:
            data = payment_methods_ns.payload
            response,status = payment_method_logic.update_payment_method_logic(id,**data)
            return response,status
        except Exception as error:
            return {"error": f"{error}"}, 400
    
    @payment_methods_ns.doc("delete_payment_method")
    def delete(self,id):
        try:
            response,status = payment_method_logic.delete_payment_method_logic(id)
            return response,status
        except Exception as error:
            return {"error": f"{error}"}, 400
        
# ============ order ============
order_ns = api.namespace("orders", description="Order operations")

order_model = order_ns.model("Order", {
    "id": fields.Integer(required=True, description="Order ID"),
    "created_at": fields.String(required=False, description="Order timestamp"),
    "user_id": fields.Integer(required=True, description="Associated user ID"),
    "payment_method_id": fields.Integer(required=True, description="Associated payment method ID")
})


@order_ns.route("/")
class OrderList(Resource):
    @order_ns.expect(order_model)
    @order_ns.doc("create_order")
    def post(self):
        try:
            data = order_ns.payload
            response, status = order_logic.create_order_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_ns.doc("list_orders")
    def get(self):
        try:
            response, status = order_logic.list_orders_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


@order_ns.route("/<int:id>")
@order_ns.param("id", "The order identifier")
class Order(Resource):
    @order_ns.doc("get_order_by_id")
    def get(self, id):
        try:
            response, status = order_logic.get_order_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_ns.expect(order_model)
    @order_ns.doc("update_order")
    def put(self, id):
        try:
            data = order_ns.payload
            response, status = order_logic.update_order_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_ns.doc("delete_order")
    def delete(self, id):
        try:
            response, status = order_logic.delete_order_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


# ============ order_item ============
order_item_ns = api.namespace("order_items", description="Order item operations")

order_item_model = order_item_ns.model("OrderItem", {
    "id": fields.Integer(required=True, description="Order Item ID"),
    "quantity": fields.Integer(required=True, description="Quantity ordered"),
    "price_at_purchase": fields.Float(required=True, description="Price at time of purchase"),
    "order_id": fields.Integer(required=True, description="Associated Order ID"),
    "product_id": fields.Integer(required=True, description="Associated Product ID")
})

@order_item_ns.route("/")
class OrderItemList(Resource):
    @order_item_ns.expect(order_item_model)
    @order_item_ns.doc("create_order_item")
    def post(self):
        try:
            data = order_item_ns.payload
            response, status = order_item_logic.create_order_item_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_item_ns.doc("list_order_items")
    def get(self):
        try:
            response, status = order_item_logic.list_order_items_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

@order_item_ns.route("/<int:id>")
@order_item_ns.param("id", "The order item identifier")
class OrderItem(Resource):
    @order_item_ns.doc("get_order_item_by_id")
    def get(self, id):
        try:
            response, status = order_item_logic.get_order_item_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_item_ns.expect(order_item_model)
    @order_item_ns.doc("update_order_item")
    def put(self, id):
        try:
            data = order_item_ns.payload
            response, status = order_item_logic.update_order_item_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @order_item_ns.doc("delete_order_item")
    def delete(self, id):
        try:
            response, status = order_item_logic.delete_order_item_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400


# ============ shipping ============

shipping_ns = api.namespace("shipping", description="Shipping operations")

shipping_model = shipping_ns.model("Shipping", {
    "id": fields.Integer(required=True, description="Shipping ID"),
    "tracking_number": fields.String(required=True, description="Tracking number"),
    "shipping_method": fields.String(required=True, description="Shipping method used"),
    "status": fields.String(required=True, description="Current shipping status"),
    "order_id": fields.Integer(required=True, description="Associated Order ID")
})

@shipping_ns.route("/")
class ShippingList(Resource):
    @shipping_ns.expect(shipping_model)
    @shipping_ns.doc("create_shipping")
    def post(self):
        try:
            data = shipping_ns.payload
            response, status = shipping_logic.create_shipping_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @shipping_ns.doc("list_shippings")
    def get(self):
        try:
            response, status = shipping_logic.list_shippings_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

@shipping_ns.route("/<int:id>")
@shipping_ns.param("id", "The shipping identifier")
class Shipping(Resource):
    @shipping_ns.doc("get_shipping_by_id")
    def get(self, id):
        try:
            response, status = shipping_logic.get_shipping_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @shipping_ns.expect(shipping_model)
    @shipping_ns.doc("update_shipping")
    def put(self, id):
        try:
            data = shipping_ns.payload
            response, status = shipping_logic.update_shipping_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @shipping_ns.doc("delete_shipping")
    def delete(self, id):
        try:
            response, status = shipping_logic.delete_shipping_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400
        
# ============ invoice ============

invoice_ns = api.namespace("invoices", description="Invoice operations")

invoice_model = invoice_ns.model("Invoice", {
    "id": fields.Integer(required=True, description="Invoice ID"),
    "total_price": fields.Float(required=True, description="Total price of the order"),
    "payment_status": fields.String(required=True, description="Status of payment"),
    "created_at": fields.String(required=True, description="Invoice creation date"),
    "paid_at": fields.String(required=True, description="Payment date"),
    "order_id": fields.Integer(required=True, description="Associated order ID")
})

@invoice_ns.route("/")
class InvoiceList(Resource):
    @invoice_ns.expect(invoice_model)
    @invoice_ns.doc("create_invoice")
    def post(self):
        try:
            data = invoice_ns.payload
            response, status = invoice_logic.create_invoice_logic(**data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @invoice_ns.doc("list_invoices")
    def get(self):
        try:
            response, status = invoice_logic.list_invoices_logic()
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

@invoice_ns.route("/<int:id>")
@invoice_ns.param("id", "The invoice identifier")
class Invoice(Resource):
    @invoice_ns.doc("get_invoice_by_id")
    def get(self, id):
        try:
            response, status = invoice_logic.get_invoice_by_id_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @invoice_ns.expect(invoice_model)
    @invoice_ns.doc("update_invoice")
    def put(self, id):
        try:
            data = invoice_ns.payload
            response, status = invoice_logic.update_invoice_logic(id, **data)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400

    @invoice_ns.doc("delete_invoice")
    def delete(self, id):
        try:
            response, status = invoice_logic.delete_invoice_logic(id)
            return response, status
        except Exception as error:
            return {"error": f"{error}"}, 400
