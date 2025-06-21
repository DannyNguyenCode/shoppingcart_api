from app import crud, services
from app.db import SessionLocal

def get_user_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            user = crud.get_user_by_id(db, id)
            if not user:
                return {"error": f"User with id {id} not found"}, 404

            return services.generate_response(
                message="User retrieved",
                status=200,
                data=user.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_user_logic(id: int, full_name: str, email: str, password: str, phone: str):
    try:
        with SessionLocal() as db:
            user = crud.create_user(db, id, full_name, email, password, phone)
            if not user:
                return {"error": "User creation failed"}, 500

            return services.generate_response(
                message="User created",
                status=201,
                data=user.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_user_logic(id: int):
    try:
        with SessionLocal() as db:
            print("Error checking ========= userlogic")
            print(id)
            user = crud.delete_user(db, id)
            if not user:
                return {"error": f"User with id {id} not found"}, 404
            print("Error checking ========= userlogic1")
            print(user)
            return services.generate_response(
                message="User deleted",
                status=200,
                data=user
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_users_logic():
    try:
        with SessionLocal() as db:
            users = crud.user_list(db)
            user_dicts = [user.to_dict() for user in users]
            return services.generate_response(
                message="User list retrieved",
                status=200,
                data={"users": user_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def update_user_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            user = crud.update_user(db, id, **kwargs)
            if not user:
                return {"error": f"User with id {id} not found"}, 404

            return services.generate_response(
                message="User updated",
                status=200,
                data=user.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500