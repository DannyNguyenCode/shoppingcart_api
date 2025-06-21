from app import crud, services
from app.db import SessionLocal

def get_payment_method_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            method = crud.get_payment_method_by_id(db, id)
            if not method:
                return {"error": f"Payment method with id {id} not found"}, 404
            return services.generate_response(
                message="Payment method retrieved",
                status=200,
                data=method.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_payment_methods_logic():
    try:
        with SessionLocal() as db:
            methods = crud.list_payment_methods(db)
            method_dicts = [m.to_dict() for m in methods]
            return services.generate_response(
                message="Payment method list retrieved",
                status=200,
                data={"payment_methods": method_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_payment_method_logic(
    id: int,
    card_number: int,
    cvv: int,
    expire_date: str,
    card_holder_name: str,
    user_id: int
):
    try:
        with SessionLocal() as db:
            method = crud.create_payment_method(
                db,
                id=id,
                card_number=card_number,
                cvv=cvv,
                expire_date=expire_date,
                card_holder_name=card_holder_name,
                user_id=user_id
            )
            if not method:
                return {"error": "Payment method creation failed"}, 500
            return services.generate_response(
                message="Payment method created",
                status=201,
                data=method.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_payment_method_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            method = crud.update_payment_method(db, id, **kwargs)
            if not method:
                return {"error": f"Payment method with id {id} not found"}, 404
            return services.generate_response(
                message="Payment method updated",
                status=200,
                data=method.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_payment_method_logic(id: int):
    try:
        with SessionLocal() as db:
            method = crud.delete_payment_method(db, id)
            if not method:
                return {"error": f"Payment method with id {id} not found"}, 404
            return services.generate_response(
                message="Payment method deleted",
                status=200,
                data=method
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
