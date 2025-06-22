from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request
from app.schemas import CompanySchema,CompanyUpdateSchema,CategorySchema, CategoryUpdateSchema, ProductSchema,ProductUpdateSchema,UserSchema,UserUpdateSchema, AddressSchema,AddressUpdateSchema, CartSchema,CartUpdateSchema,CartItemSchema,CartItemUpdateSchema,PaymentMethodSchema, PaymentMethodUpdateSchema,OrderSchema,OrderUpdateSchema,OrderItemSchema,OrderItemUpdateSchema,ShippingSchema,ShippingUpdateSchema, InvoiceSchema,InvoiceUpdateSchema

from app.logic import company_logic, category_logic,product_logic,user_logic,address_logic,cart_logic,cart_item_logic,payment_method_logic,order_logic,order_item_logic,shipping_logic,invoice_logic

# ============ companies ============

company_blp = Blueprint("companies", __name__, url_prefix="/api/companies", description="Company operations")

@company_blp.route("/")
class CompanyList(MethodView):
    @company_blp.doc(description="List all comapnies")
    def get(self):
        response, status = company_logic.list_companies_logic()
        return response, status
    
    @company_blp.doc(description="Create a company")
    @company_blp.arguments(CompanySchema)
    def post(self,data):
        response, status = company_logic.create_company_logic(**data)
        return response, status

@company_blp.route("/<int:id>")
class CompanyResource(MethodView):
    @company_blp.doc(description="Get a company by id")
    def get(self, id):
        response, status = company_logic.get_company_by_id_logic(id)
        return response, status
    
    @company_blp.doc(description="Update a company")
    @company_blp.arguments(CompanyUpdateSchema)
    def put(self, data,id):
        response, status = company_logic.update_company_logic(id, **data)
        return response, status
    @company_blp.doc(description="Delete a company")
    def delete(self, id):
        response, status = company_logic.delete_company_logic(id)
        return response, status

# ============ categories ============

category_blp = Blueprint("categories", __name__, url_prefix="/api/categories", description="Category operations")

@category_blp.route("/")
class CategoryList(MethodView):
    @category_blp.doc(description="List all categories")
    def get(self):
        response, status = category_logic.list_categories_logic()
        return response, status

    @category_blp.doc(description="Create a category")
    @category_blp.arguments(CategorySchema)
    def post(self, data):
        response, status = category_logic.create_category_logic(**data)
        return response, status

@category_blp.route("/<int:id>")
class CategoryResource(MethodView):
    @category_blp.doc(description="Get a category by id")
    def get(self, id):
        response, status = category_logic.get_category_by_id_logic(id)
        return response, status

    @category_blp.doc(description="Update a category")
    @category_blp.arguments(CategoryUpdateSchema)
    def put(self, data, id):
        response, status = category_logic.update_category_logic(id, **data)
        return response, status

    @category_blp.doc(description="Delete a category")
    def delete(self, id):
        response, status = category_logic.delete_category_logic(id)
        return response, status
        

# ============ product ============

product_blp = Blueprint("products", __name__, url_prefix="/api/products", description="Product operations")

@product_blp.route("/")
class ProductList(MethodView):
    @product_blp.doc(description="List all products")
    def get(self):
        response, status = product_logic.list_products_logic()
        return response, status

    @product_blp.doc(description="Create a product")
    @product_blp.arguments(ProductSchema)
    def post(self, data):
        response, status = product_logic.create_product_logic(**data)
        return response, status

@product_blp.route("/<int:id>")
class ProductResource(MethodView):
    @product_blp.doc(description="Get a product by id")
    def get(self, id):
        response, status = product_logic.get_product_by_id_logic(id)
        return response, status

    @product_blp.doc(description="Update a product")
    @product_blp.arguments(ProductUpdateSchema)
    def put(self, data, id):
        response, status = product_logic.update_product_logic(id, **data)
        return response, status

    @product_blp.doc(description="Delete a product")
    def delete(self, id):
        response, status = product_logic.delete_product_logic(id)
        return response, status
# ============ user ============
user_blp = Blueprint("users", __name__, url_prefix="/api/users", description="User operations")

@user_blp.route("/")
class UserList(MethodView):
    @user_blp.doc(description="List all users")
    def get(self):
        response, status = user_logic.list_users_logic()
        return response, status

    @user_blp.doc(description="Create a user")
    @user_blp.arguments(UserSchema)
    def post(self, data):
        response, status = user_logic.create_user_logic(**data)
        return response, status

@user_blp.route("/<int:id>")
class UserResource(MethodView):
    @user_blp.doc(description="Get a user by id")
    def get(self, id):
        response, status = user_logic.get_user_by_id_logic(id)
        return response, status

    @user_blp.doc(description="Update a user")
    @user_blp.arguments(UserUpdateSchema)
    def put(self, data, id):
        response, status = user_logic.update_user_logic(id, **data)
        return response, status

    @user_blp.doc(description="Delete a user")
    def delete(self, id):
        response, status = user_logic.delete_user_logic(id)
        return response, status
# ============ address ============
address_blp = Blueprint("addresses", __name__, url_prefix="/api/addresses", description="Address operations")

@address_blp.route("/")
class AddressList(MethodView):
    @address_blp.doc(description="List all addresses")
    def get(self):
        response, status = address_logic.list_addresses_logic()
        return response, status

    @address_blp.doc(description="Create an address")
    @address_blp.arguments(AddressSchema)
    def post(self, data):
        response, status = address_logic.create_address_logic(**data)
        return response, status

@address_blp.route("/<int:id>")
class AddressResource(MethodView):
    @address_blp.doc(description="Get an address by id")
    def get(self, id):
        response, status = address_logic.get_address_by_id_logic(id)
        return response, status

    @address_blp.doc(description="Update an address")
    @address_blp.arguments(AddressUpdateSchema)
    def put(self, data, id):
        response, status = address_logic.update_address_logic(id, **data)
        return response, status

    @address_blp.doc(description="Delete an address")
    def delete(self, id):
        response, status = address_logic.delete_address_logic(id)
        return response, status
# ============ cart ============

cart_blp = Blueprint("carts", __name__, url_prefix="/api/carts", description="Cart operations")

@cart_blp.route("/")
class CartList(MethodView):
    @cart_blp.doc(description="List all carts")
    def get(self):
        response, status = cart_logic.list_carts_logic()
        return response, status

    @cart_blp.doc(description="Create a cart")
    @cart_blp.arguments(CartSchema)
    def post(self, data):
        response, status = cart_logic.create_cart_logic(**data)
        return response, status

@cart_blp.route("/<int:id>")
class CartResource(MethodView):
    @cart_blp.doc(description="Get a cart by id")
    def get(self, id):
        response, status = cart_logic.get_cart_by_id_logic(id)
        return response, status

    @cart_blp.doc(description="Update a cart")
    @cart_blp.arguments(CartUpdateSchema)
    def put(self, data, id):
        response, status = cart_logic.update_cart_logic(id, **data)
        return response, status

    @cart_blp.doc(description="Delete a cart")
    def delete(self, id):
        response, status = cart_logic.delete_cart_logic(id)
        return response, status
# ============ cart_item ============

cart_item_blp = Blueprint("cart_items", __name__, url_prefix="/api/cart_items", description="Cart Item operations")

@cart_item_blp.route("/")
class CartItemList(MethodView):
    @cart_item_blp.doc(description="List all cart items")
    def get(self):
        response, status = cart_item_logic.list_cart_items_logic()
        return response, status

    @cart_item_blp.doc(description="Create a cart item")
    @cart_item_blp.arguments(CartItemSchema)
    def post(self, data):
        response, status = cart_item_logic.create_cart_item_logic(**data)
        return response, status

@cart_item_blp.route("/<int:id>")
class CartItemResource(MethodView):
    @cart_item_blp.doc(description="Get a cart item by id")
    def get(self, id):
        response, status = cart_item_logic.get_cart_item_by_id_logic(id)
        return response, status

    @cart_item_blp.doc(description="Update a cart item")
    @cart_item_blp.arguments(CartItemUpdateSchema)
    def put(self, data, id):
        response, status = cart_item_logic.update_cart_item_logic(id, **data)
        return response, status

    @cart_item_blp.doc(description="Delete a cart item")
    def delete(self, id):
        response, status = cart_item_logic.delete_cart_item_logic(id)
        return response, status
# ============ payment_method ============

payment_method_blp = Blueprint("payment_methods", __name__, url_prefix="/api/payment_methods", description="Payment Method operations")

@payment_method_blp.route("/")
class PaymentMethodList(MethodView):
    @payment_method_blp.doc(description="List all payment methods")
    def get(self):
        response, status = payment_method_logic.list_payment_methods_logic()
        return response, status

    @payment_method_blp.doc(description="Create a payment method")
    @payment_method_blp.arguments(PaymentMethodSchema)
    def post(self, data):
        response, status = payment_method_logic.create_payment_method_logic(**data)
        return response, status

@payment_method_blp.route("/<int:id>")
class PaymentMethodResource(MethodView):
    @payment_method_blp.doc(description="Get a payment method by id")
    def get(self, id):
        response, status = payment_method_logic.get_payment_method_by_id_logic(id)
        return response, status

    @payment_method_blp.doc(description="Update a payment method")
    @payment_method_blp.arguments(PaymentMethodUpdateSchema)
    def put(self, data, id):
        response, status = payment_method_logic.update_payment_method_logic(id, **data)
        return response, status

    @payment_method_blp.doc(description="Delete a payment method")
    def delete(self, id):
        response, status = payment_method_logic.delete_payment_method_logic(id)
        return response, status
# ============ order ============
order_blp = Blueprint("orders", __name__, url_prefix="/api/orders", description="Order operations")

@order_blp.route("/")
class OrderList(MethodView):
    @order_blp.doc(description="List all orders")
    def get(self):
        response, status = order_logic.list_orders_logic()
        return response, status

    @order_blp.doc(description="Create an order")
    @order_blp.arguments(OrderSchema)
    def post(self, data):
        response, status = order_logic.create_order_logic(**data)
        return response, status

@order_blp.route("/<int:id>")
class OrderResource(MethodView):
    @order_blp.doc(description="Get an order by id")
    def get(self, id):
        response, status = order_logic.get_order_by_id_logic(id)
        return response, status

    @order_blp.doc(description="Update an order")
    @order_blp.arguments(OrderUpdateSchema)
    def put(self, data, id):
        response, status = order_logic.update_order_logic(id, **data)
        return response, status

    @order_blp.doc(description="Delete an order")
    def delete(self, id):
        response, status = order_logic.delete_order_logic(id)
        return response, status
# ============ order_item ============
order_item_blp = Blueprint("order_items", __name__, url_prefix="/api/order_items", description="Order Item operations")

@order_item_blp.route("/")
class OrderItemList(MethodView):
    @order_item_blp.doc(description="List all order items")
    def get(self):
        response, status = order_item_logic.list_order_items_logic()
        return response, status

    @order_item_blp.doc(description="Create an order item")
    @order_item_blp.arguments(OrderItemSchema)
    def post(self, data):
        response, status = order_item_logic.create_order_item_logic(**data)
        return response, status

@order_item_blp.route("/<int:id>")
class OrderItemResource(MethodView):
    @order_item_blp.doc(description="Get an order item by id")
    def get(self, id):
        response, status = order_item_logic.get_order_item_by_id_logic(id)
        return response, status

    @order_item_blp.doc(description="Update an order item")
    @order_item_blp.arguments(OrderItemUpdateSchema)
    def put(self, data, id):
        response, status = order_item_logic.update_order_item_logic(id, **data)
        return response, status

    @order_item_blp.doc(description="Delete an order item")
    def delete(self, id):
        response, status = order_item_logic.delete_order_item_logic(id)
        return response, status
# ============ shipping ============
shipping_blp = Blueprint("shipping", __name__, url_prefix="/api/shipping", description="Shipping operations")

@shipping_blp.route("/")
class ShippingList(MethodView):
    @shipping_blp.doc(description="List all shipping entries")
    def get(self):
        response, status = shipping_logic.list_shippings_logic()
        return response, status

    @shipping_blp.doc(description="Create a shipping entry")
    @shipping_blp.arguments(ShippingSchema)
    def post(self, data):
        response, status = shipping_logic.create_shipping_logic(**data)
        return response, status

@shipping_blp.route("/<int:id>")
class ShippingResource(MethodView):
    @shipping_blp.doc(description="Get a shipping entry by id")
    def get(self, id):
        response, status = shipping_logic.get_shipping_by_id_logic(id)
        return response, status

    @shipping_blp.doc(description="Update a shipping entry")
    @shipping_blp.arguments(ShippingUpdateSchema)
    def put(self, data, id):
        response, status = shipping_logic.update_shipping_logic(id, **data)
        return response, status

    @shipping_blp.doc(description="Delete a shipping entry")
    def delete(self, id):
        response, status = shipping_logic.delete_shipping_logic(id)
        return response, status

# ============ invoice ============
invoice_blp = Blueprint("invoices", __name__, url_prefix="/api/invoices", description="Invoice operations")

@invoice_blp.route("/")
class InvoiceList(MethodView):
    @invoice_blp.doc(description="List all invoices")
    def get(self):
        response, status = invoice_logic.list_invoices_logic()
        return response, status

    @invoice_blp.doc(description="Create an invoice")
    @invoice_blp.arguments(InvoiceSchema)
    def post(self, data):
        response, status = invoice_logic.create_invoice_logic(**data)
        return response, status

@invoice_blp.route("/<int:id>")
class InvoiceResource(MethodView):
    @invoice_blp.doc(description="Get an invoice by id")
    def get(self, id):
        response, status = invoice_logic.get_invoice_by_id_logic(id)
        return response, status

    @invoice_blp.doc(description="Update an invoice")
    @invoice_blp.arguments(InvoiceUpdateSchema)
    def put(self, data, id):
        response, status = invoice_logic.update_invoice_logic(id, **data)
        return response, status

    @invoice_blp.doc(description="Delete an invoice")
    def delete(self, id):
        response, status = invoice_logic.delete_invoice_logic(id)
        return response, status