from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey
class Base(DeclarativeBase):
    pass

class Company(Base):
    __tablename__ ="company"
    id:Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=True)
    product:Mapped[List["Product"]] = relationship(back_populates="company",cascade="all, delete-orphan")

    def to_dict(self):
        return {"id":self.id,"name":self.name, "products":[{"id":product.id,"name":product.name,"price":product.price,"description":product.description,"stock_quantity":product.stock_quantity,"category_id":product.category_id,"company_id":product.company_id}for product in self.product]if self.product else []}

    def __repr__(self) -> str:
        return (
            f"Company(id={self.id!r}, name={self.name!r})"
        )

class Category(Base):
    __tablename__="category"
    id:Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=True)
    product:Mapped[List["Product"]] = relationship(back_populates="category",cascade="all, delete-orphan")
    def to_dict(self):
        return {"id":self.id,"name":self.name, "products":[{"id":product.id,"name":product.name,"price":product.price,"description":product.description,"stock_quantity":product.stock_quantity,"category_id":product.category_id,"company_id":product.company_id}for product in self.product]if self.product else []}
    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"
    
class Product(Base):
    __tablename__="product"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=True)
    price:Mapped[float]=mapped_column(nullable=True)
    stock_quantity:Mapped[int]=mapped_column(nullable=True)
    description:Mapped[int]=mapped_column(nullable=True)
    company_id:Mapped[int]=mapped_column(ForeignKey("company.id",ondelete="CASCADE"))
    category_id:Mapped[int]=mapped_column(ForeignKey("category.id",ondelete="CASCADE"))
    company:Mapped["Company"]=relationship(back_populates="product")
    category:Mapped["Category"]=relationship(back_populates="product")
    cart_item:Mapped["Cart_Item"]=relationship(back_populates="product")
    order_item:Mapped["Order_Item"]=relationship("Order_Item",back_populates="product", cascade="all, delete",passive_deletes=True)
    def to_dict(self):
        return {
                "id":self.id,
                "name":self.name,
                "price":self.price,
                "stock_quantity":self.stock_quantity,
                "description":self.description,
                "company_id":self.company_id,
                "category_id":self.category_id,
                }
    def __repr__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, price={self.price!r}, stock_quantity={self.stock_quantity!r}, description={self.description!r})"


class User(Base):
    __tablename__="user"
    id:Mapped[int]= mapped_column(primary_key=True)
    full_name:Mapped[str]=mapped_column(nullable=True)
    email:Mapped[str]=mapped_column(nullable=True)
    password:Mapped[str]=mapped_column(nullable=True)
    phone:Mapped[str]=mapped_column(nullable=True)
    address:Mapped[List["Address"]]=relationship(back_populates="user", cascade="all, delete-orphan")
    cart:Mapped["Cart"]=relationship(back_populates="user",cascade="all, delete-orphan")
    order:Mapped["Order"]=relationship(back_populates="user", cascade="all, delete-orphan")
    payment_method:Mapped[List["Payment_Method"]]= relationship(back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id":self.id,
            "full_name":self.full_name,
            "email":self.email,
            "password":self.password,
            "phone":self.phone,
            "address":[{
                "id":address.id,
                "street_address":address.street_address,
                "state":address.state,
                "postal_code":address.postal_code,
                "country":address.country,
                "user_id":address.user_id,
            }for address in self.address] if self.address else [],
            "cart":{
                "id":self.cart.id,
                "user_id":self.cart.user_id
            }if self.cart else None,
            "payment_methods":[{
                "id":pay_method.id,
                "card_number":pay_method.card_number,
                "card_holder_name":pay_method.card_holder_name,
                "cvv":pay_method.cvv,
                "expire_date":pay_method.expire_date,
                "user_id":pay_method.user_id
            }for pay_method in self.payment_method] if self.payment_method else[]
            }

    def __repr__(self):
        return f"User(id={self.id!r}, full_name={self.full_name!r}, email={self.email!r}, password={self.password!r}, phone={self.phone!r})"

class Address(Base):
    __tablename__="address"
    id:Mapped[int]=mapped_column(primary_key=True)
    street_address:Mapped[str]=mapped_column(nullable=True)
    state:Mapped[str]=mapped_column(nullable=True)
    postal_code:Mapped[str]=mapped_column(nullable=True)
    country:Mapped[str]=mapped_column(nullable=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id",ondelete="CASCADE"))
    user:Mapped["User"]=relationship(back_populates="address")

    def to_dict(self):
        return {
            "id":self.id,
            "street_address":self.street_address,
            "state":self.state,
            "postal_code":self.postal_code,
            "country":self.country,
            "user_id":self.user_id,
            "user":self.user.to_dict() if self.user else {},
        }

    def __repr__(self):
        return f"Address(id={self.id!r}, street_address={self.street_address!r}, state={self.state!r}, postal_code={self.postal_code!r}, country={self.country!r})"

class Cart(Base):
    __tablename__="cart"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id",ondelete="CASCADE"))
    user:Mapped["User"]=relationship(back_populates="cart")
    cart_item:Mapped[List["Cart_Item"]]=relationship(back_populates="cart",cascade="all, delete-orphan")
    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "cart_item":[item.to_dict() for item in self.cart_item]if self.cart_item else []
        }
    def __repr__(self):
        return f"Cart(id={self.id!r})"


class Cart_Item(Base):
    __tablename__="cart_item"
    id:Mapped[int]=mapped_column(primary_key=True)
    quantity:Mapped[int]=mapped_column(nullable=True)
    product_id:Mapped[int]=mapped_column(ForeignKey("product.id",ondelete="CASCADE"))
    product:Mapped["Product"]=relationship(back_populates="cart_item")
    cart_id:Mapped[int]=mapped_column(ForeignKey("cart.id",ondelete="CASCADE"))
    cart:Mapped["Cart"]=relationship(back_populates="cart_item")
    def to_dict(self):
        return{
            "id":self.id,
            "quantity":self.quantity,
            "cart_id":self.cart_id,
            "products":self.product.to_dict() if self.product else {}
        }
    def __repr__(self):
        return f"Cart_Item(id={self.id!r}, quantity={self.quantity!r})"

class Payment_Method(Base):
    __tablename__="payment_method"
    id:Mapped[int]=mapped_column(primary_key=True)
    card_number:Mapped[int]=mapped_column(nullable=True)
    cvv:Mapped[int] =mapped_column(nullable=True)
    expire_date:Mapped[str]=mapped_column(nullable=True)
    card_holder_name:Mapped[str]=mapped_column(nullable=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id",ondelete="CASCADE"))
    user:Mapped["User"]= relationship(back_populates="payment_method")
    order:Mapped["Order"]=relationship(back_populates="payment_method",cascade="all, delete-orphan")
    def to_dict(self):
        return{
            "id":self.id,
            "card_number":self.card_number,
            "card_holder_name":self.card_holder_name,
            "cvv":self.cvv,
            "expire_date":self.expire_date,
            "user_id":self.user_id
        }
    def __repr__(self):
        return f"Payment_Method(id={self.id!r}, card_number={self.card_number!r}, cvv={self.cvv!r}, expire_date={self.expire_date!r}, card_holder_name={self.card_holder_name!r})"


class Order(Base):
    __tablename__ = "order"
    id:Mapped[int]=mapped_column(primary_key=True)
    created_at:Mapped[str]=mapped_column(nullable=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id",ondelete="CASCADE"))
    user:Mapped["User"]=relationship(back_populates="order")
    payment_method_id:Mapped[int]= mapped_column(ForeignKey("payment_method.id", ondelete="CASCADE"))
    payment_method:Mapped["Payment_Method"]=relationship(back_populates="order")
    order_item:Mapped[List["Order_Item"]]=relationship(back_populates="order",cascade="all, delete-orphan")
    shipping:Mapped["Shipping"]=relationship(back_populates="order", cascade="all, delete-orphan",uselist=False)
    invoice:Mapped["Invoice"]=relationship(back_populates="order")

    def to_dict(self):
        return{
        "id":self.id,
        "created_at":self.created_at,
        "user_id":self.user_id,
        "user":{
            "full_name":self.user.full_name,
            "email":self.user.email,
            "phone":self.user.phone,
        }if self.user else None,
        "payment_method_id":self.payment_method_id,
        "payment_method":self.payment_method.to_dict() if self.payment_method else {},
        "order_item":[item.to_dict() for item in self.order_item]if self.order_item else [],
        "shipping":self.shipping.to_dict() if self.shipping else {}
        }
    def __repr__(self):
        return f"Order(id={self.id!r}, created_at={self.created_at!r}, user_id={self.user_id!r}, payment_method_id={self.payment_method_id!r})"
    
class Order_Item(Base):
    __tablename__="order_item"
    id:Mapped[int]=mapped_column(primary_key=True)
    quantity:Mapped[int]=mapped_column(nullable=True)
    price_at_purchase:Mapped[float]=mapped_column(nullable=True)
    order_id:Mapped[int]=mapped_column(ForeignKey("order.id"))
    order:Mapped["Order"]=relationship(back_populates="order_item")
    product_id:Mapped[int]=mapped_column(ForeignKey("product.id", ondelete="CASCADE"))
    product:Mapped["Product"]=relationship("Product",back_populates="order_item")
    def to_dict(self):
        return {
            "id":self.id,
            "quantity":self.quantity,
            "price_at_purchase":self.price_at_purchase,
            "order_id":self.order_id,
            "product_id":self.product_id,
            "product":self.product.to_dict()
        }
    def __repr__(self):
        return f"Order_Item(id={self.id!r}, quantity={self.quantity!r}, price_at_purchase={self.price_at_purchase!r}, order_id={self.order_id!r}, product_id={self.product_id!r})"
    
class Shipping(Base):
    __tablename__="shipping"
    id:Mapped[int]=mapped_column(primary_key=True)
    tracking_number:Mapped[str]=mapped_column(nullable=True)
    shipping_method:Mapped[str]=mapped_column(nullable=True)
    status:Mapped[str]=mapped_column(nullable=True)
    order_id:Mapped[int]=mapped_column(ForeignKey("order.id"))
    order:Mapped["Order"]=relationship(back_populates="shipping")
    def to_dict(self):
        return{
            "id":self.id,
            "tracking_number":self.tracking_number,
            "shipping_method":self.shipping_method,
            "status":self.status,
            "order_id":self.order_id
        }
    def __repr__(self):
        return f"Shipping(id={self.id!r}, tracking_number={self.tracking_number!r}, shipping_method={self.shipping_method!r}, status={self.status!r}, order_id={self.order_id!r})"
    
class Invoice(Base):
    __tablename__="invoice"
    id:Mapped[int]=mapped_column(primary_key=True)
    total_price:Mapped[float]=mapped_column(nullable=True)
    payment_status:Mapped[str]=mapped_column(nullable=True)
    created_at:Mapped[str]=mapped_column(nullable=True)
    paid_at:Mapped[str]=mapped_column(nullable=True)
    order_id:Mapped[int]=mapped_column(ForeignKey("order.id"))
    order:Mapped["Order"]=relationship(back_populates='invoice')
    
    def to_dict(self):
        return{
            "id":self.id,
            "total_price":self.total_price,
            "payment_status":self.payment_status,
            "created_at":self.created_at,
            "paid_at":self.paid_at,
            "order_id":self.order_id,
            "order":self.order.to_dict() if self.order else {}
        }
    def __repr__(self):
        return f"Invoice(id={self.id!r}, total_price={self.total_price!r}, payment_status={self.payment_status!r}, created_at={self.created_at!r}, paid_at={self.paid_at!r}, order_id={self.order_id!r})"
