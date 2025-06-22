from app.db import SessionLocal
from app import crud, services

def create_product_logic(id: int, name: str, price: float, description: str, category_id: int, stock_quantity: int, company_id: int):
    try:
        with SessionLocal() as db:
            category = crud.get_category_by_id(db, category_id)
            if not category:
                return {"error": f"Category with id {category_id} not found"}, 404

            company = crud.get_company_by_id(db, company_id)
            if not company:
                return {"error": f"Company with id {company_id} not found"}, 404

            product = crud.create_product(db, id, name, price, description, category_id, stock_quantity, company_id)
            return services.generate_response(
                message="Product created",
                status=201,
                data=product.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 400


def list_products_logic():
    try:
        with SessionLocal() as db:
            products = crud.product_list(db)
            product_dicts = [product.to_dict() for product in products]
            return services.generate_response(
                message="Product list retrieved",
                status=200,
                data={"products": product_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400


def get_product_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            product = crud.get_product_by_id(db, id)
            if not product:
                return {"error": f"Product with id {id} not found"}, 404

            return services.generate_response(
                message="Product retrieved",
                status=200,
                data=product.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400


def update_product_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            product = crud.update_product(db, id, **kwargs)
            if not product:
                return {"error": f"Product with id {id} not found"}, 404

            return services.generate_response(
                message="Product updated",
                status=200,
                data=product.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400


def delete_product_logic(id: int):
    try:
        with SessionLocal() as db:
            product = crud.delete_product(db, id)
            if not product:
                return {"error": f"Product with id {id} not found"}, 404

            return services.generate_response(
                message="Product deleted",
                status=200,
                data=product
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
