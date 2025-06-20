from app import crud,services
from app.db import SessionLocal

def create_category_logic(id:int,name:str):
    try:
        with SessionLocal() as db:
            category = crud.create_category(db, id,name)
            # converting sqlalchemy's returning to a dictionary  
            keys =["id","name"]
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Created",201)
            # return dictionary in json format to response
            return dictionary,201

    except Exception as e:
        return {"error": f"{e}"},400
    
def category_list_logic():
    try:
        with SessionLocal() as db:
            categories = crud.list_categories(db)
            return [category.to_dict() for category in categories]
    except Exception as error:
        return {"error": f"{error}"}
    
def get_category_by_id_logic(id:int):
    try:
        with SessionLocal() as db:
            category = crud.get_category_by_id(db,id)
            if not category:
                return {"error": f"category with id {id} not found"}
            return category.to_dict(),200
    except Exception as error:
        return {"error":f"{error}"}
    
def update_category_logic(id:int,data):
    try:
        with SessionLocal() as db:
            category = crud.update_category(db,id,**data)
            if not category:
                return {"error":"id is required"},400
            # converting sqlalchemy's returning method to a dictionary
            keys =["id","name"]
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Updated",200)
            # return dictionary in json format to response
            return dictionary,200
    except Exception as error:
        return {"error":f"{error}"}

def delete_category_logic(id:int):
    try:
        with SessionLocal() as db:
            category = crud.delete_category(db,id)
            if not category:
                return {"error": "Category not found"}, 404
            # converting sqlalchemy's returning to a dictionary       
            keys =["id","name"]
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Deleted",200)
            # return dictionary in json format to response
            return dictionary,200
    except Exception as error:
        return {"error":f"{error}"}