from app import crud, services
from app.db import SessionLocal

def get_address_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            address = crud.get_address_by_id(db, id)
            if not address:
                return {"error": f"Address with id {id} not found"}, 404

            return services.generate_response(
                message="Address retrieved",
                status=200,
                data=address.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_address_logic(id: int, street_address: str, state: str, postal_code: str, country: str, user_id: int):
    try:
        with SessionLocal() as db:
            address = crud.create_address(db, id, street_address, state, postal_code, country, user_id)
            if not address:
                return {"error": "Address creation failed"}, 500

            return services.generate_response(
                message="Address created",
                status=201,
                data=address.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_address_logic(id: int):
    try:
        with SessionLocal() as db:
            address = crud.delete_address(db, id)
            if not address:
                return {"error": f"Address with id {id} not found"}, 404

            return services.generate_response(
                message="Address deleted",
                status=200,
                data=address
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_addresses_logic():
    try:
        with SessionLocal() as db:
            addresses = crud.list_addresses(db)
            address_dicts = [addr.to_dict() for addr in addresses]
            return services.generate_response(
                message="Address list retrieved",
                status=200,
                data={"addresses": address_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def update_address_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            address = crud.update_address(db, id, **kwargs)
            if not address:
                return {"error": f"Address with id {id} not found"}, 404

            return services.generate_response(
                message="Address updated",
                status=200,
                data=address.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500
