from app import crud,services
from app.db import SessionLocal

def get_category_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            category = crud.get_category_by_id(db, id)
            if not category:
                return {"error": f"Category with id {id} not found"}, 404

            return services.generate_response(
                message="Category retrieved",
                status=200,
                data=category.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400


def create_category_logic(id: int, name: str):
    try:
        with SessionLocal() as db:
            category = crud.create_category(db, id=id, name=name)
            if not category:
                return {"error": "Category creation failed"}, 500

            return services.generate_response(
                message="Category created",
                status=201,
                data=category.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500


def delete_category_logic(id: int):
    try:
        with SessionLocal() as db:
            category = crud.delete_category(db, id)
            if not category:
                return {"error": f"Category with id {id} not found"}, 404

            return services.generate_response(
                message="Category deleted",
                status=200,
                data=category
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
    
def list_categories_logic():
    try:
        with SessionLocal() as db:
            categories = crud.list_categories(db)
            category_dicts = [category.to_dict() for category in categories]
            return services.generate_response(
                message="Category list retrieved",
                status=200,
                data={"categories": category_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
    

def update_category_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            category = crud.update_category(db, id, **kwargs)
            if not category:
                return {"error": f"Category with id {id} not found"}, 404

            return services.generate_response(
                message="Category updated",
                status=200,
                data=category.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500