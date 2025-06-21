from app import crud, services
from app.db import SessionLocal

def get_cart_item_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            item = crud.get_cart_item_by_id(db, id)
            if not item:
                return {"error": f"CartItem with id {id} not found"}, 404

            return services.generate_response(
                message="Cart item retrieved",
                status=200,
                data=item.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_cart_items_logic():
    try:
        with SessionLocal() as db:
            items = crud.list_cart_items(db)
            item_dicts = [item.to_dict() for item in items]
            return services.generate_response(
                message="Cart item list retrieved",
                status=200,
                data={"cart_items": item_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_cart_item_logic(id: int, quantity: int, cart_id: int, product_id: int):
    try:
        with SessionLocal() as db:
            item = crud.create_cart_item(db, id=id, quantity=quantity, cart_id=cart_id, product_id=product_id)
            if not item:
                return {"error": "Cart item creation failed"}, 500

            return services.generate_response(
                message="Cart item created",
                status=201,
                data=item.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_cart_item_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            item = crud.update_cart_item(db, id, **kwargs)
            if not item:
                return {"error": f"Cart item with id {id} not found"}, 404

            return services.generate_response(
                message="Cart item updated",
                status=200,
                data=item.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_cart_item_logic(id: int):
    try:
        with SessionLocal() as db:
            item = crud.delete_cart_item(db, id)
            if not item:
                return {"error": f"Cart item with id {id} not found"}, 404

            return services.generate_response(
                message="Cart item deleted",
                status=200,
                data=item
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
