from sqlalchemy.orm import Session
from sqlalchemy import select,update,insert,delete
from app.models import Company,Category,Product,User,Address,Cart

# ============ company ============

def create_company(db:Session, id:int,name:str)->Company:
    company = db.execute(insert(Company)
                         .values(id=id,name=name)
                         .returning(Company.id,Company.name)).fetchall()
    db.commit()
    return company


def list_companies(db:Session):
    return db.execute(select(Company)).scalars()    

def get_company_by_id(db:Session,id:int):
    return db.execute(select((Company)).where(Company.id==id)).scalar()

def update_company(db:Session, id:int,**kwargs):
    company = db.execute(update(Company)
                         .where(Company.id == id)
                         .values(kwargs)
                         .returning(Company.id,Company.name)).fetchall()
    db.commit()
    return company

def delete_company(db:Session,id:int):
    company = db.execute(delete(Company)
                         .where(Company.id==id)
                         .returning(Company.id,Company.name)).fetchall()
    db.commit()
    return company

# ============ category ============


def create_category(db:Session, id:int,name:str)->Category:
    category = db.execute(insert(Category)
                          .values(id=id,name=name)
                          .returning(Category.id,Category.name)).fetchall()
    db.commit()
    return category


def list_categories(db:Session):
    categories = db.execute(select(Category)).scalars()

    return categories

def get_category_by_id(db:Session,id:int):
    category = db.execute(select(Category).where(Category.id==id)).scalar()
    return category

def update_category(db:Session,id:int,**kwargs):
    category = db.execute(update(Category)
                          .where(Category.id==id)
                          .values(kwargs)
                          .returning(Category.id,Category.name)).fetchall()
    db.commit()
    return category

def delete_category(db:Session,id:int):
    category = db.execute(delete(Category)
                          .where(Category.id==id)
                          .returning(Category.id,Category.name)).fetchall()
    db.commit()
    return category

# ============ product ============


def create_product(db:Session, id:int, name:str,price:float,description:str,category_id:int,stock_quantity:int,company_id:int) ->Product:
    product = db.execute(insert(Product)
                         .values(id=id, name=name,price=price,description=description,category_id=category_id,stock_quantity=stock_quantity,company_id=company_id)
                         .returning(Product.name,Product.price,Product.description,Product.category_id,Product.stock_quantity,Product.company_id)).fetchall()
    db.commit()
    return product

def product_list(db:Session):
    products = db.execute(select(Product)).scalars()
    return products

def get_product_by_id(db:Session,id:int):
    products = db.execute(select(Product).where(Product.id == id)).scalar()
    return products

def update_product(db:Session,id:int,**kwargs):
    product = db.execute(update(Product)
                         .where(Product.id == id)
                         .values(kwargs)
                         .returning(Product.name,Product.price,Product.description,Product.category_id,Product.stock_quantity,Product.company_id)).fetchall()
    db.commit()
    return product


def delete_product(db:Session,id:int):
    product = db.execute(delete(Product)
                         .where(Product.id == id)
                         .returning(Product.name,Product.price,Product.description,Product.category_id,Product.stock_quantity,Product.company_id)).fetchall()
    db.commit()
    return product
        
# ============ user ============

def create_user(db:Session,id:int,full_name:str,email:str,password:str,phone:str)->User:
    user = db.execute(insert(User)
                      .values(id=id,full_name=full_name,email=email,password=password,phone=phone)
                      .returning(User.id,User.full_name,User.email,User.password,User.phone)).fetchall()
    db.commit()
    return user

def user_list(db:Session):
    return db.execute(select(User)).scalars()

def get_user_by_id(db:Session,id:int):
    return db.execute(select(User).where(User.id == id)).scalar()

def update_user(db:Session,id:int,**kwargs):
    user = db.execute(update(User)
                      .where(User.id == id)
                      .values(kwargs)
                      .returning(User.id,User.full_name,User.email,User.password,User.phone)).fetchall()
    db.commit()
    return user

def delete_user(db:Session,id:int):
    user = db.execute(delete(User)
                      .where(User.id == id)
                      .returning(User.id,User.full_name,User.email,User.password,User.phone)).fetchall()
    db.commit()
    return user

# ============ address ============

def create_address(db:Session,id:int,street_address:str,state:str,postal_code:str,country:str,user_id:int)->Address:
    user = db.execute(insert(Address)
                      .values(id=id,street_address=street_address,state=state,postal_code=postal_code,country=country,user_id=user_id)
                      .returning(Address.id,Address.street_address,Address.state,Address.postal_code,Address.country,Address.user_id)).fetchall()
    db.commit()
    return user

def address_list(db:Session):
    return db.execute(select(Address)).scalars()

def get_address_by_id(db:Session,id:int):
    return db.execute(select(Address).where(Address.id == id)).scalar()

def update_address(db:Session,id:int,**kwargs):
    address = db.execute(update(Address)
                         .where(Address.id == id)
                         .values(kwargs)
                         .returning(Address.id,Address.street_address,Address.state,Address.postal_code,Address.country,Address.user_id)).fetchall()
    db.commit()
    return address

def delete_address(db:Session,id:int):
    address = db.execute(delete(Address)
                         .where(Address.id == id)
                         .returning(Address.id,Address.street_address,Address.state,Address.postal_code,Address.country,Address.user_id)).fetchall()
    db.commit()
    return address
                    
# ============ cart ============
def create_cart(db:Session,id:int,user_id:int)->Cart:
    cart = db.execute(insert(Cart)
                      .values(id=id,user_id=user_id)
                      .returning(Cart.id,Cart.user_id)).fetchall()
    db.commit()
    return cart

def cart_list(db:Session):
    cart = db.execute(select(Cart)).scalars()
    return cart
def get_cart_by_id(db:Session,id:int):
    cart = db.execute(select(Cart).where(Cart.id==id)).scalar()
    return cart
def update_cart(db:Session,id:int,**kwargs):
    cart = db.execute(update(Cart)
                      .where(Cart.id == id)
                      .values(kwargs)
                      .returning(Cart.id,Cart.user_id)).fetchall()
    db.commit()
    return cart
def delete_cart(db:Session,id:int):
    cart = db.execute(delete(Cart)
                      .where(Cart.id == id)
                      .returning(Cart.id,Cart.user_id)).fetchall()
    db.commit()
    return cart