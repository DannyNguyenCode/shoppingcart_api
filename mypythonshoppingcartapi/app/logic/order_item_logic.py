from app import crud, services
from app.db import SessionLocal

def get_order_item_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            item = crud.get_order_item_by_id(db, id)
            if not item:
                return {"error": f"Order item with id {id} not found"}, 404

            return services.generate_response(
                message="Order item retrieved",
                status=200,
                data=item.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_order_items_logic():
    try:
        with SessionLocal() as db:
            items = crud.list_order_items(db)
            item_dicts = [item.to_dict() for item in items]
            return services.generate_response(
                message="Order item list retrieved",
                status=200,
                data={"order_items": item_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_order_item_logic(id: int, quantity: int, price_at_purchase: float, order_id: int, product_id: int):
    try:
        with SessionLocal() as db:
            item = crud.create_order_item(
                db,
                id=id,
                quantity=quantity,
                price_at_purchase=price_at_purchase,
                order_id=order_id,
                product_id=product_id
            )
            if not item:
                return {"error": "Order item creation failed"}, 500

            return services.generate_response(
                message="Order item created",
                status=201,
                data=item.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_order_item_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            item = crud.update_order_item(db, id, **kwargs)
            if not item:
                return {"error": f"Order item with id {id} not found"}, 404

            return services.generate_response(
                message="Order item updated",
                status=200,
                data=item.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_order_item_logic(id: int):
    try:
        with SessionLocal() as db:
            item = crud.delete_order_item(db, id)
            if not item:
                return {"error": f"Order item with id {id} not found"}, 404

            return services.generate_response(
                message="Order item deleted",
                status=200,
                data=item
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
