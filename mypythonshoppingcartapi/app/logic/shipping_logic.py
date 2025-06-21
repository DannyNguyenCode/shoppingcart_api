from app import crud, services
from app.db import SessionLocal

def get_shipping_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            shipping = crud.get_shipping_by_id(db, id)
            if not shipping:
                return {"error": f"Shipping with id {id} not found"}, 404

            return services.generate_response(
                message="Shipping retrieved",
                status=200,
                data=shipping.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_shippings_logic():
    try:
        with SessionLocal() as db:
            shippings = crud.list_shippings(db)
            shipping_dicts = [s.to_dict() for s in shippings]
            return services.generate_response(
                message="Shipping list retrieved",
                status=200,
                data={"shippings": shipping_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_shipping_logic(id: int, tracking_number: str, shipping_method: str, status: str, order_id: int):
    try:
        with SessionLocal() as db:
            shipping = crud.create_shipping(
                db,
                id=id,
                tracking_number=tracking_number,
                shipping_method=shipping_method,
                status=status,
                order_id=order_id
            )
            if not shipping:
                return {"error": "Shipping creation failed"}, 500

            return services.generate_response(
                message="Shipping created",
                status=201,
                data=shipping.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_shipping_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            shipping = crud.update_shipping(db, id, **kwargs)
            if not shipping:
                return {"error": f"Shipping with id {id} not found"}, 404

            return services.generate_response(
                message="Shipping updated",
                status=200,
                data=shipping.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_shipping_logic(id: int):
    try:
        with SessionLocal() as db:
            shipping = crud.delete_shipping(db, id)
            if not shipping:
                return {"error": f"Shipping with id {id} not found"}, 404

            return services.generate_response(
                message="Shipping deleted",
                status=200,
                data=shipping
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
