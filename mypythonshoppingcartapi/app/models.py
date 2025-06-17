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
    def get_keys(self):
        return["id","name"]
    def to_dict(self):
        return {"id":self.id,"name":self.name, "products":[{"id":product.id,"name":product.name,"price":product.price,"description":product.description,"stock_quantity":product.stock_quantity,"category_id":product.category_id,"company_id":product.company_id}for product in self.product]}

    def __repr__(self) -> str:
        return (
            f"Company(id={self.id!r}, name={self.name!r})"
        )

class Category(Base):
    __tablename__="category"
    id:Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=True)
    product:Mapped[List["Product"]] = relationship(back_populates="category",cascade="all, delete-orphan")
    def get_keys(self):
        return["id","name"]
    def to_dict(self):
        return {"id":self.id,"name":self.name, "products":[{"id":product.id,"name":product.name,"price":product.price,"description":product.description,"stock_quantity":product.stock_quantity,"category_id":product.category_id,"company_id":product.company_id}for product in self.product]}
    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r})"
    
class Product(Base):
    __tablename__="product"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=True)
    price:Mapped[float]=mapped_column(nullable=True)
    stock_quantity:Mapped[int]=mapped_column(nullable=True)
    description:Mapped[int]=mapped_column(nullable=True)
    company_id:Mapped[int]=mapped_column(ForeignKey("company.id"))
    category_id:Mapped[int]=mapped_column(ForeignKey("category.id"))
    company:Mapped["Company"]=relationship(back_populates="product")
    category:Mapped["Category"]=relationship(back_populates="product")
    cart_item:Mapped["Cart_Item"]=relationship(back_populates="product")
    def get_keys(self):
        return["name","price","description","category_id","stock_quantity","company_id","company","category"]
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
    def get_keys(self):
        return["id","full_name","email","password","phone"]
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
            }for address in self.address],
            "cart":{
                "id":self.cart.id,
                "user_id":self.cart.user_id
            },
            "payment_methods":[{
                "id":pay_method.id,
                "card_number":pay_method.card_number,
                "card_holder_name":pay_method.card_holder_name,
                "cvv":pay_method.cvv,
                "expire_date":pay_method.expire_date,
                "user_id":pay_method.user_id
            }for pay_method in self.payment_method]
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
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"))
    user:Mapped["User"]=relationship(back_populates="address")
    def get_keys(self):
        return["id","street_address","state","postal_code","country","user_id"]
    def to_dict(self):
        return {
            "id":self.id,
            "street_address":self.street_address,
            "state":self.state,
            "postal_code":self.postal_code,
            "country":self.country,
            "user_id":self.user_id,
            "user":self.user.to_dict(),
        }

    def __repr__(self):
        return f"Address(id={self.id!r}, street_address={self.street_address!r}, state={self.state!r}, postal_code={self.postal_code!r}, country={self.country!r})"

class Cart(Base):
    __tablename__="cart"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"))
    user:Mapped["User"]=relationship(back_populates="cart")
    cart_item:Mapped[List["Cart_Item"]]=relationship(back_populates="cart",cascade="all, delete-orphan")
    def get_keys(self):
        return["id","user_id"]
    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "cart_item":[item.to_dict() for item in self.cart_item]
        }
    def __repr__(self):
        return f"Cart(id={self.id!r})"


class Cart_Item(Base):
    __tablename__="cart_item"
    id:Mapped[int]=mapped_column(primary_key=True)
    quantity:Mapped[int]=mapped_column(nullable=True)
    product_id:Mapped[int]=mapped_column(ForeignKey("product.id"))
    product:Mapped["Product"]=relationship(back_populates="cart_item")
    cart_id:Mapped[int]=mapped_column(ForeignKey("cart.id"))
    cart:Mapped["Cart"]=relationship(back_populates="cart_item")
    def get_keys(self):
        return["id","quantity","product_id","cart_id"]
    def to_dict(self):
        return{
            "id":self.id,
            "quantity":self.quantity,
            "cart_id":self.cart_id,
            "products":self.product.to_dict()
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
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"))
    user:Mapped["User"]= relationship(back_populates="payment_method")
    order:Mapped["Order"]=relationship(back_populates="payment_method")
    def get_keys(self):
        return["id","card_number","cvv","expire_date","card_holder_name","user_id"]
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
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"))
    user:Mapped["User"]=relationship(back_populates="order")
    payment_method_id:Mapped[int]= mapped_column(ForeignKey("payment_method.id"))
    payment_method:Mapped["Payment_Method"]=relationship(back_populates="order")

    def __repr__(self):
        return f"Order(id={self.id!r}, created_at={self.created_at!r})"
    
class Order_Item(Base):
    __tablename__="order_item"
    id:Mapped[int]=mapped_column(primary_key=True)

