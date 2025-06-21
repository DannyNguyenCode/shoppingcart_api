from app import crud, services
from app.db import SessionLocal

def get_cart_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            cart = crud.get_cart_by_id(db, id)
            if not cart:
                return {"error": f"Cart with id {id} not found"}, 404

            return services.generate_response(
                message="Cart retrieved",
                status=200,
                data=cart.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_carts_logic():
    try:
        with SessionLocal() as db:
            carts = crud.list_carts(db)
            cart_dicts = [cart.to_dict() for cart in carts]
            return services.generate_response(
                message="Cart list retrieved",
                status=200,
                data={"carts": cart_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_cart_logic(id: int, user_id: int):
    try:
        with SessionLocal() as db:
            cart = crud.create_cart(db, id=id, user_id=user_id)
            if not cart:
                return {"error": "Cart creation failed"}, 500

            return services.generate_response(
                message="Cart created",
                status=201,
                data=cart.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_cart_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            cart = crud.update_cart(db, id, **kwargs)
            if not cart:
                return {"error": f"Cart with id {id} not found"}, 404

            return services.generate_response(
                message="Cart updated",
                status=200,
                data=cart.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_cart_logic(id: int):
    try:
        with SessionLocal() as db:
            cart = crud.delete_cart(db, id)
            if not cart:
                return {"error": f"Cart with id {id} not found"}, 404

            return services.generate_response(
                message="Cart deleted",
                status=200,
                data=cart
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400