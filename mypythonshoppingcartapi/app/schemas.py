from marshmallow import Schema, fields

class CompanySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class CompanyUpdateSchema(Schema):
    name = fields.Str()

class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class CategoryUpdateSchema(Schema):
    name = fields.Str()

class ProductSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str(required=True)
    category_id = fields.Int(required=True)
    stock_quantity = fields.Int(required=True)
    company_id = fields.Int(required=True)

class ProductUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    description = fields.Str()
    category_id = fields.Int()
    stock_quantity = fields.Int()
    company_id = fields.Int()


class UserSchema(Schema):

    id=fields.Int(required=True)
    full_name=fields.Str(required=True)
    email=fields.Str(required=True)
    password=fields.Str(required=True)
    phone=fields.Str(required=True)

class UserUpdateSchema(Schema):
    full_name=fields.Str()
    email=fields.Str()
    password=fields.Str()
    phone=fields.Str()

class AddressSchema(Schema):
    id =fields.Int(required=True)
    street_address=fields.Str(required=True)
    state=fields.Str(required=True)
    postal_code=fields.Str(required=True)
    country=fields.Str(required=True)
    user_id = fields.Int(required=True)

class AddressUpdateSchema(Schema):
    street_address=fields.Str()
    state=fields.Str()
    postal_code=fields.Str()
    country=fields.Str()
    user_id = fields.Int()


class CartSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)


class CartUpdateSchema(Schema):
    user_id = fields.Int()


class CartItemSchema(Schema):
    id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    cart_id = fields.Int(required=True)

class CartItemUpdateSchema(Schema):
    product_id = fields.Int()
    quantity = fields.Int()
    cart_id = fields.Int()


class PaymentMethodSchema(Schema):
    id=fields.Int(required=True)
    card_number=fields.Str(required=True)
    cvv=fields.Int(required=True)
    expire_date=fields.Str(required=True)
    card_holder_name=fields.Str(required=True)
    user_id=fields.Int(required=True)

class PaymentMethodUpdateSchema(Schema):
    card_number=fields.Str()
    cvv=fields.Int()
    expire_date=fields.Str()
    card_holder_name=fields.Str()
    user_id=fields.Int()

class OrderSchema(Schema):
    id=fields.Int(required=True)
    created_at=fields.Str(required=True)
    user_id=fields.Int(required=True)
    payment_method_id=fields.Int(required=True)

class OrderUpdateSchema(Schema):
    created_at=fields.Str()
    user_id=fields.Int()
    payment_method_id=fields.Int()

class OrderItemSchema(Schema):
    id=fields.Int(required=True)
    quantity=fields.Int(required=True)
    price_at_purchase=fields.Float(required=True)
    order_id=fields.Int(required=True)
    product_id=fields.Int(required=True)

class OrderItemUpdateSchema(Schema):
    quantity=fields.Int()
    price_at_purchase=fields.Float()
    order_id=fields.Int()
    product_id=fields.Int()


class ShippingSchema(Schema):
    id=fields.Str(required=True)
    tracking_number=fields.Str(required=True)
    shipping_method=fields.Str(required=True)
    status=fields.Str(required=True)
    order_id=fields.Int(required=True)

class ShippingUpdateSchema(Schema):
    tracking_number=fields.Str()
    shipping_method=fields.Str()
    status=fields.Str()
    order_id=fields.Int()

class InvoiceSchema(Schema):

    id=fields.Int(required=True)
    total_price=fields.Float(required=True)
    payment_status=fields.Str(required=True)
    created_at=fields.Str(required=True)
    paid_at=fields.Str(required=True)
    order_id=fields.Int(required=True)

class InvoiceUpdateSchema(Schema):
    total_price=fields.Float()
    payment_status=fields.Str()
    created_at=fields.Str()
    paid_at=fields.Str()
    order_id=fields.Int()
