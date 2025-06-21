from app import crud, services
from app.db import SessionLocal

def get_order_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            order = crud.get_order_by_id(db, id)
            if not order:
                return {"error": f"Order with id {id} not found"}, 404
            return services.generate_response(
                message="Order retrieved",
                status=200,
                data=order.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_orders_logic():
    try:
        with SessionLocal() as db:
            orders = crud.list_orders(db)
            order_dicts = [order.to_dict() for order in orders]
            return services.generate_response(
                message="Order list retrieved",
                status=200,
                data={"orders": order_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_order_logic(id: int, created_at: str, user_id: int, payment_method_id: int):
    try:
        with SessionLocal() as db:
            order = crud.create_order(db, id=id, created_at=created_at, user_id=user_id, payment_method_id=payment_method_id)
            if not order:
                return {"error": "Order creation failed"}, 500
            return services.generate_response(
                message="Order created",
                status=201,
                data=order.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_order_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            order = crud.update_order(db, id, **kwargs)
            if not order:
                return {"error": f"Order with id {id} not found"}, 404
            return services.generate_response(
                message="Order updated",
                status=200,
                data=order.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_order_logic(id: int):
    try:
        with SessionLocal() as db:
            order = crud.delete_order(db, id)
            if not order:
                return {"error": f"Order with id {id} not found"}, 404
            return services.generate_response(
                message="Order deleted",
                status=200,
                data=order
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
