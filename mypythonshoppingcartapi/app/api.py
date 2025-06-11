from flask import Flask, request, jsonify
from app.db import SessionLocal, engine
from sqlalchemy.exc import IntegrityError
from app import crud, models

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# ============ company ============

@app.route("/companies/create",methods=["POST"])
def create_company():
    try:
        data = request.get_json()
        id=data.get("id")
        if not id:
            return jsonify({"error": "id is required"}),400
        name=data.get("name")
        with SessionLocal() as db:
            company = crud.create_company(db, id, name)
            return jsonify({
                "id":company.id,
                "name":company.name
            }),201
    except IntegrityError:
        return jsonify({"Error": f"id={id} already exists in database"}),400
    except Exception as e:
        return jsonify({"Error": f"{e}"})

@app.route("/companies", methods=["GET"])
def list_companies():
    try:
        with SessionLocal() as db:
            companies=crud.list_companies(db)
            return jsonify([{
                "id": company.id,
                "name": company.name
            } for company in companies]),200
    except Exception as error:
        return jsonify({"Error": f"{error}"}) 

@app.route("/companies/<int:id>",methods=["GET"])
def get_company_by_id(id):
    try:
        with SessionLocal() as db:
            company = crud.get_company_by_id(db,id)
            if not company:
                return jsonify({"error": "Company not found"}), 404
            return jsonify({
                "id":company.id,
                "name":company.name
            }),200
    except Exception as error:
        return jsonify({"Error":f"{error}"})



@app.route("/companies/<int:id>/update", methods=["PUT"])
def update_company(id):
    try:
        data=request.get_json()
        with SessionLocal() as db:
            company = crud.update_company(db,id,**data)
            if not company:
                return jsonify({"error":"id is required"}),400
            return jsonify({
                "id":company.id,
                "name":company.name
            }),204
    except Exception as error:
        return jsonify({"Error":f"{error}"})

@app.route("/companies/<int:id>/delete",methods=["DELETE"])
def delete_company(id):
    try:
        with SessionLocal() as db:
            company = crud.delete_company(db,id)
            if not company:
                return jsonify({"error": "Company not found"}), 404
            return jsonify({"message": "Company deleted"}),200
    except Exception as error:
         return jsonify({"Error":f"{error}"})


# ============ category ============

@app.route("/categories/create",methods=["POST"])
def create_category():
    try:
        data=request.get_json()
        id = data.get("id")
        if not id:
            return jsonify({"error": "id is required"}),400
        name = data.get("name")
        with SessionLocal() as db:
            category = crud.create_category(db,id,name)
            return jsonify({
                "id":category.id,
                "name":category.name
            }),201
    except IntegrityError:
        return jsonify({"Error": f"id={id} already exists in database"}),400
    except Exception as error:
        return jsonify({"Error":f"{error}"})
    
@app.route("/categories",methods=["GET"])
def list_categories():
    try:
        with SessionLocal() as db:
            categories = crud.list_categories(db)
            return jsonify([{
                    "id": category.id,
                    "name": category.name
                } for category in categories]),200
    except Exception as error:
        return jsonify({"Error":f"{error}"})

@app.route("/categories/<int:id>",methods=["GET"])
def get_category_by_id(id):
    try:
        with SessionLocal() as db:
            category = crud.get_category_by_id(db,id)
            if not category:
                return jsonify({"Error": f"category with id {id} not found"})
            return jsonify({
                "id":category.id,
                "name":category.name
            }),200
    except Exception as error:
        return jsonify({"Error":f"{error}"})

@app.route("/categories/<int:id>/update",methods=["PUT"])
def update_category(id):
    try:
        data=request.get_json()
        with SessionLocal() as db:
            category = crud.update_category(db,id,**data)
            if not category:
                return jsonify({"Error": f"category with id {id} not found"}),400
            return jsonify({
                "id":category.id,
                "name":category.name
            }),204
    except Exception as error:
        return jsonify({"Error":f"{error}"})

@app.route("/categories/<int:id>/delete", methods=["DELETE"])
def delete_category(id):
    try:
        with SessionLocal() as db:
            category = crud.delete_category(db,id)
            if not category:
                return jsonify({"Error": f"category with id {id} not found"}),400
            return jsonify({
                "message": "Category deleted"
            }),200
    except Exception as error:
        return jsonify({"Error":f"{error}"})
    

# ============ product ============

@app.route("/products/create",methods=["POST"])
def create_product():
    try:
        with SessionLocal() as db :
            data = request.get_json()
            # first check relationship category exists
            category = crud.get_category_by_id(db,data.get("category_id"))
            if not category:
                return jsonify({"Error": f"category with id {data.get("category_id")} not found"}),400
            # second check relationship company exists
            company = crud.get_company_by_id(db,data.get("company_id"))
            if not company:
                return jsonify({"Error": f"company with id {data.get("company_id")} not found"}),400
            # third if all pass, create product and commit to database
            product = crud.create_product(
                db,
                id=data.get("id"),
                name=data.get("name"),
                price=data.get("price"),
                description=data.get("description"),
                category_id=data.get("category_id"),
                stock_quantity=data.get("stock_quantity"),
                company_id=data.get("company_id"))
            return jsonify({
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "description":product.description,
                "category_id":product.category_id,
                "stock_quantity":product.stock_quantity,
                "company_id":product.company_id
            }),201
    except IntegrityError:
        return jsonify({"Error": f"id={id} already exists in database"}),400
    except Exception as error:
        return jsonify({"Error":f"{error}"})

@app.route("/products",methods=["GET"])
def product_list():
    try:
        with SessionLocal() as db:
            products = crud.product_list(db)
            return jsonify([{
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "description":product.description,
                "category_id":product.category_id,
                "stock_quantity":product.stock_quantity,
                "company_id":product.company_id
            } for product in products]),200
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400
    
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    try:
        with SessionLocal() as db:
            product = crud.get_product_by_id(db,id)
            if not product:
                return jsonify({"Error":f"producy id={id} not found"})
            return jsonify({
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "description":product.description,
                "category_id":product.category_id,
                "stock_quantity":product.stock_quantity,
                "company_id":product.company_id
            }),200
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400

@app.route("/products/<int:id>/update",methods=["PUT"])
def update_product(id):
    try:
        data = request.get_json()
        with SessionLocal() as db:
            product = crud.update_product(db,id,**data)
            if not product:
                return jsonify({"Error":"Product with id={id} not found"}),400
            return jsonify({
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "description":product.description,
                "category_id":product.category_id,
                "stock_quantity":product.stock_quantity,
                "company_id":product.company_id
            }),204           
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400
    
@app.route("/products/<int:id>/delete",methods=["DELETE"])
def delete_product(id):
    try:
        with SessionLocal() as db:
            product = crud.delete_product(db,id)
            if not product:
                return jsonify({"Error": f"product with id {id} not found"}),400
            return jsonify({
                "message": "Product deleted"
            }),200
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400
    
