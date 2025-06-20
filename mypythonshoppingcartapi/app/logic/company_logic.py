
from app import crud,services
from app.db import SessionLocal


def create_company_logic(id:int,name:str):
    try:
        with SessionLocal() as db:       
            company = crud.create_company(db, id, name)
            # converting sqlalchemy's returning to a dictionary
            keys =["id","name"]
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Created",201)
            # return dictionary in json format to response
            return dictionary

    except Exception as error:
        return {"error": f"{error}"},400

def list_companies_logic():
    try:
        with SessionLocal() as db:
            companies=crud.list_companies(db)
            return [company.to_dict() for company in companies]
    except Exception as error:
        return {"error": f"{error}"}
    
def get_company_by_id_logic(id:int):
    try:
        with SessionLocal() as db:
            company = crud.get_company_by_id(db,id)
            if not company:
                return {"error": f"Company id={id} not found"}, 400
            return company.to_dict(),200
    except Exception as error:
        return {"error": f"{error}"},400

def update_company_logic(id:int,data):
    try:
        with SessionLocal() as db:
     
            company = crud.update_company(db,id,**data)
            if not company:
                return {"error":"id is required"},400
            # converting sqlalchemy's returning to a dictionary
            keys =["id","name"]
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Updated",200)
             # return dictionary in json format to response
            return dictionary
    except Exception as error:
        return {"error":f"{error}"}
    
def delete_company_logic(id:int):
    try:
        with SessionLocal() as db:
            company = crud.delete_company(db,id)
            if not company:
                return {"error":"id is required"},400
            # converting sqlalchemy's returning to a dictionary
            keys =["id","name"]
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Deleted",200)
             # return dictionary in json format to response
            return dictionary
    except Exception as error:
        return {"error":f"{error}"}