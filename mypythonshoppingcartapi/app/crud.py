from sqlalchemy.orm import Session
from sqlalchemy import select,update,insert,delete
from app.models import Company,Category,Product,User,Address,Cart,Cart_Item,Payment_Method,Order,Order_Item,Shipping,Invoice

# ============ company ============

def get_company_by_id(db: Session, id: int) -> Company | None:
    stmt = select(Company).where(Company.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_companies(db: Session) -> list[Company]:
    stmt = select(Company)
    return db.execute(stmt).scalars().all()

def create_company(db: Session, id: int, name: str) -> Company | None:
    stmt = (
        insert(Company)
        .values(id=id, name=name)
        .returning(Company)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_company(db: Session, id: int, **kwargs) -> Company | None:
    stmt = (
        update(Company)
        .where(Company.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Company)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_company(db: Session, id: int) -> dict | None:
    stmt = select(Company).where(Company.id == id)
    company = db.execute(stmt).scalar_one_or_none()
    if not company:
        return None
    company_data = company.to_dict()
    db.delete(company)
    db.commit()
    return company_data

# ============ category ============


def list_categories(db: Session) -> list[Category]:
    stmt = select(Category)
    return db.execute(stmt).scalars().all()

def get_category_by_id(db: Session, id: int) -> Category | None:
    stmt = select(Category).where(Category.id == id)
    return db.execute(stmt).scalar_one_or_none()

def create_category(db: Session, id: int, name: str) -> Category | None:
    stmt = (
        insert(Category)
        .values(id=id, name=name)
        .returning(Category)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_category(db: Session, id: int, **kwargs) -> Category | None:
    stmt = (update(Category)
            .where(Category.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
            .returning(Category))
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_category(db: Session, id: int) -> dict | None:
    stmt = select(Category).where(Category.id == id)
    category = db.execute(stmt).scalar_one_or_none()
    if not category:
        return None
    category_data = category.to_dict()
    db.delete(category)
    db.commit()
    return category_data

# ============ product ============


def create_product(db: Session,id: int,name: str,price: float,description: str,category_id: int,stock_quantity: int,company_id: int) -> Product | None:
    stmt = (insert(Product)
            .values(id=id,name=name, price=price, description=description, category_id=category_id, stock_quantity=stock_quantity, company_id=company_id)
            .returning(Product))

    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def product_list(db: Session) -> list[Product]:
    stmt = select(Product)
    return db.execute(stmt).scalars().all()

def get_product_by_id(db: Session, id: int) -> dict | None:
    stmt = select(Product).where(Product.id == id)
    return db.execute(stmt).scalar_one_or_none()

def update_product(db:Session,id:int,**kwargs)->Product|None:
    stmt = (update(Product)
            .where(Product.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
            .returning(Product))
    
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result


def delete_product(db: Session, id: int) -> dict | None:
    stmt = select(Product).where(Product.id == id)
    product = db.execute(stmt).scalar_one_or_none()
    
    if not product:
        return None
    
    product_data = product.to_dict()
    db.delete(product)
    db.commit()
    return product_data
        
# ============ user ============

def create_user(db: Session, id: int, full_name: str, email: str, password: str, phone: str) -> User | None:
    stmt = (
        insert(User)
        .values(id=id, full_name=full_name, email=email, password=password, phone=phone)
        .returning(User)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def user_list(db: Session) -> list[User]:
    stmt = select(User)
    return db.execute(stmt).scalars().all()

def get_user_by_id(db: Session, id: int) -> User | None:
    stmt = select(User).where(User.id == id)
    return db.execute(stmt).scalar_one_or_none()

def update_user(db: Session, id: int, **kwargs) -> User | None:
    stmt = (
        update(User)
        .where(User.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(User)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_user(db: Session, id: int):
    stmt = select(User).where(User.id == id)
    user = db.execute(stmt).scalar_one_or_none()
    if not user:
        return None
    user_data = user.to_dict()
    db.delete(user)
    db.commit()
    return user_data

# ============ address ============

def get_address_by_id(db: Session, id: int) -> Address | None:
    stmt = select(Address).where(Address.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_addresses(db: Session) -> list[Address]:
    stmt = select(Address)
    return db.execute(stmt).scalars().all()

def create_address(db: Session, id: int, street_address: str, state: str, postal_code: str, country: str, user_id: int) -> Address | None:
    stmt = (
        insert(Address)
        .values(id=id, street_address=street_address, state=state, postal_code=postal_code, country=country, user_id=user_id)
        .returning(Address)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_address(db: Session, id: int, **kwargs) -> Address | None:
    stmt = (
        update(Address)
        .where(Address.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Address)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_address(db: Session, id: int) -> dict | None:
    stmt = select(Address).where(Address.id == id)
    address = db.execute(stmt).scalar_one_or_none()
    if not address:
        return None
    address_data = address.to_dict()
    db.delete(address)
    db.commit()
    return address_data
                    
# ============ cart ============

def get_cart_by_id(db: Session, id: int) -> Cart | None:
    stmt = select(Cart).where(Cart.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_carts(db: Session) -> list[Cart]:
    stmt = select(Cart)
    return db.execute(stmt).scalars().all()

def create_cart(db: Session, id: int, user_id: int) -> Cart | None:
    stmt = (
        insert(Cart)
        .values(id=id, user_id=user_id)
        .returning(Cart)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    if result is None:
        result = db.execute(select(Cart).where(Cart.id == id)).scalar_one_or_none()
    return result

def update_cart(db: Session, id: int, **kwargs) -> Cart | None:
    stmt = (
        update(Cart)
        .where(Cart.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Cart)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_cart(db: Session, id: int) -> dict | None:
    stmt = select(Cart).where(Cart.id == id)
    cart = db.execute(stmt).scalar_one_or_none()
    if not cart:
        return None
    cart_data = cart.to_dict()
    db.delete(cart)
    db.commit()
    return cart_data

# ============ cart_item ============

def get_cart_item_by_id(db: Session, id: int) -> Cart_Item | None:
    stmt = select(Cart_Item).where(Cart_Item.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_cart_items(db: Session) -> list[Cart_Item]:
    stmt = select(Cart_Item)
    return db.execute(stmt).scalars().all()

def create_cart_item(db: Session, id: int, quantity: int, cart_id: int, product_id: int) -> Cart_Item | None:
    stmt = (
        insert(Cart_Item)
        .values(id=id, quantity=quantity, cart_id=cart_id, product_id=product_id)
        .returning(Cart_Item)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    if result is None:
        result = db.execute(select(Cart_Item).where(Cart_Item.id == id)).scalar_one_or_none()
    return result

def update_cart_item(db: Session, id: int, **kwargs) -> Cart_Item | None:
    stmt = (
        update(Cart_Item)
        .where(Cart_Item.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Cart_Item)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_cart_item(db: Session, id: int) -> dict | None:
    stmt = select(Cart_Item).where(Cart_Item.id == id)
    item = db.execute(stmt).scalar_one_or_none()
    if not item:
        return None
    item_data = item.to_dict()
    db.delete(item)
    db.commit()
    return item_data

# ============ payment_method ============

def get_payment_method_by_id(db: Session, id: int) -> Payment_Method | None:
    stmt = select(Payment_Method).where(Payment_Method.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_payment_methods(db: Session) -> list[Payment_Method]:
    stmt = select(Payment_Method)
    return db.execute(stmt).scalars().all()

def create_payment_method(
    db: Session,
    id: int,
    card_number: int,
    cvv: int,
    expire_date: str,
    card_holder_name: str,
    user_id: int
) -> Payment_Method | None:
    stmt = (
        insert(Payment_Method)
        .values(
            id=id,
            card_number=card_number,
            cvv=cvv,
            expire_date=expire_date,
            card_holder_name=card_holder_name,
            user_id=user_id
        )
        .returning(Payment_Method)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_payment_method(db: Session, id: int, **kwargs) -> Payment_Method | None:
    stmt = (
        update(Payment_Method)
        .where(Payment_Method.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Payment_Method)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_payment_method(db: Session, id: int) -> dict | None:
    stmt = select(Payment_Method).where(Payment_Method.id == id)
    payment_method = db.execute(stmt).scalar_one_or_none()
    if not payment_method:
        return None
    data = payment_method.to_dict()
    db.delete(payment_method)
    db.commit()
    return data


# ============ order ============

def get_order_by_id(db: Session, id: int) -> Order | None:
    stmt = select(Order).where(Order.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_orders(db: Session) -> list[Order]:
    stmt = select(Order)
    return db.execute(stmt).scalars().all()

def create_order(
    db: Session,
    id: int,
    created_at: str,
    user_id: int,
    payment_method_id: int
) -> Order | None:
    stmt = (
        insert(Order)
        .values(
            id=id,
            created_at=created_at,
            user_id=user_id,
            payment_method_id=payment_method_id
        )
        .returning(Order)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_order(db: Session, id: int, **kwargs) -> Order | None:
    stmt = (
        update(Order)
        .where(Order.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Order)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_order(db: Session, id: int) -> dict | None:
    stmt = select(Order).where(Order.id == id)
    order = db.execute(stmt).scalar_one_or_none()
    if not order:
        return None
    data = order.to_dict()
    db.delete(order)
    db.commit()
    return data

# ============ order_item ============

def get_order_item_by_id(db: Session, id: int) -> Order_Item | None:
    stmt = select(Order_Item).where(Order_Item.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_order_items(db: Session) -> list[Order_Item]:
    stmt = select(Order_Item)
    return db.execute(stmt).scalars().all()

def create_order_item(
    db: Session,
    id: int,
    quantity: int,
    price_at_purchase: float,
    order_id: int,
    product_id: int
) -> Order_Item | None:
    stmt = (
        insert(Order_Item)
        .values(
            id=id,
            quantity=quantity,
            price_at_purchase=price_at_purchase,
            order_id=order_id,
            product_id=product_id
        )
        .returning(Order_Item)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_order_item(db: Session, id: int, **kwargs) -> Order_Item | None:
    stmt = (
        update(Order_Item)
        .where(Order_Item.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Order_Item)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_order_item(db: Session, id: int) -> dict | None:
    stmt = select(Order_Item).where(Order_Item.id == id)
    item = db.execute(stmt).scalar_one_or_none()
    if not item:
        return None
    data = item.to_dict()
    db.delete(item)
    db.commit()
    return data

# ============ shipping ============

def get_shipping_by_id(db: Session, id: int) -> Shipping | None:
    stmt = select(Shipping).where(Shipping.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_shippings(db: Session) -> list[Shipping]:
    stmt = select(Shipping)
    return db.execute(stmt).scalars().all()

def create_shipping(
    db: Session,
    id: int,
    tracking_number: str,
    shipping_method: str,
    status: str,
    order_id: int
) -> Shipping | None:
    stmt = (
        insert(Shipping)
        .values(
            id=id,
            tracking_number=tracking_number,
            shipping_method=shipping_method,
            status=status,
            order_id=order_id
        )
        .returning(Shipping)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_shipping(db: Session, id: int, **kwargs) -> Shipping | None:
    stmt = (
        update(Shipping)
        .where(Shipping.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Shipping)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_shipping(db: Session, id: int) -> dict | None:
    stmt = select(Shipping).where(Shipping.id == id)
    shipping = db.execute(stmt).scalar_one_or_none()
    if not shipping:
        return None
    data = shipping.to_dict()
    db.delete(shipping)
    db.commit()
    return data

# ============ invoice ============

def get_invoice_by_id(db: Session, id: int) -> Invoice | None:
    stmt = select(Invoice).where(Invoice.id == id)
    return db.execute(stmt).scalar_one_or_none()

def list_invoices(db: Session) -> list[Invoice]:
    stmt = select(Invoice)
    return db.execute(stmt).scalars().all()

def create_invoice(
    db: Session,
    id: int,
    total_price: float,
    payment_status: str,
    created_at: str,
    paid_at: str,
    order_id: int
) -> Invoice | None:
    stmt = (
        insert(Invoice)
        .values(
            id=id,
            total_price=total_price,
            payment_status=payment_status,
            created_at=created_at,
            paid_at=paid_at,
            order_id=order_id
        )
        .returning(Invoice)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def update_invoice(db: Session, id: int, **kwargs) -> Invoice | None:
    stmt = (
        update(Invoice)
        .where(Invoice.id == id)
        .values(**kwargs)
        .execution_options(synchronize_session="fetch")
        .returning(Invoice)
    )
    result = db.execute(stmt).scalars().first()
    db.commit()
    return result

def delete_invoice(db: Session, id: int) -> dict | None:
    stmt = select(Invoice).where(Invoice.id == id)
    invoice = db.execute(stmt).scalar_one_or_none()
    if not invoice:
        return None
    data = invoice.to_dict()
    db.delete(invoice)
    db.commit()
    return data
    