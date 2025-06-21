
from app import crud,services
from app.db import SessionLocal


def get_company_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            company = crud.get_company_by_id(db, id)
            if not company:
                return {"error": f"Company with id {id} not found"}, 404

            return services.generate_response(
                message="Company retrieved",
                status=200,
                data=company.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400


def create_company_logic(id: int, name: str):
    try:
        with SessionLocal() as db:
            company = crud.create_company(db, id=id, name=name)
            if not company:
                return {"error": "Company creation failed"}, 500

            return services.generate_response(
                message="Company created",
                status=201,
                data=company.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500


def delete_company_logic(id: int):
    try:
        with SessionLocal() as db:
            company = crud.delete_company(db, id)
            if not company:
                return {"error": f"Company with id {id} not found"}, 404

            return services.generate_response(
                message="Company deleted",
                status=200,
                data=company
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
    
def list_companies_logic():
    try:
        with SessionLocal() as db:
            companies = crud.list_companies(db)
            company_dicts = [company.to_dict() for company in companies]
            return services.generate_response(
                message="Company list retrieved",
                status=200,
                data={"companies": company_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
    
def update_company_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            company = crud.update_company(db, id, **kwargs)
            if not company:
                return {"error": f"Company with id {id} not found"}, 404

            return services.generate_response(
                message="Company updated",
                status=200,
                data=company.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500