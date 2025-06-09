from flask import Flask, request, jsonify
from app.db import SessionLocal, engine
from app import crud, models

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# ============ company ============

@app.route("/companies/create",methods=["POST"])
def create_company():
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

@app.route("/companies", methods=["GET"])
def list_companies():
    with SessionLocal() as db:
        companies=crud.list_companies(db)
        return jsonify([{
            "id": company.id,
            "name": company.name
        } for company in companies]),200 

@app.route("/companies/<int:id>",methods=["GET"])
def get_company_by_id(id):
    with SessionLocal() as db:
        company = crud.get_company_by_id(db,id)
        if not company:
            return jsonify({"error": "Company not found"}), 404
        return jsonify({
            "id":company.id,
            "name":company.name
        }),200



@app.route("/companies/<int:id>/update", methods=["PUT"])
def update_company(id):
    data=request.get_json()
    with SessionLocal() as db:
        company = crud.update_company(db,id,**data)
        if not company:
            return jsonify({"error":"id is required"}),400
        return jsonify({
            "id":company.id,
            "name":company.name
        }),204

@app.route("/companies/<int:id>/delete",methods=["DELETE"])
def delete_company(id):
    with SessionLocal() as db:
        company = crud.delete_company(db,id)
        if not company:
            return jsonify({"error": "Company not found"}), 404
        return jsonify({"message": "Company deleted"}),200 


# ============ category ============

@app.route("/categories/create",methods=["POST"])
def create_category():
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
    
@app.route("/categories",methods=["GET"])
def list_categories():
    with SessionLocal() as db:
        categories = crud.list_categories(db)
        return jsonify([{
                "id": category.id,
                "name": category.name
            } for category in categories]),200

@app.route("/categories/<int:id>",methods=["GET"])
def get_category_by_id(id):
    with SessionLocal() as db:
        category = crud.get_category_by_id(db,id)
        if not category:
            return jsonify({f"Error: category with id {id} not found"})
        return jsonify({
            "id":category.id,
            "name":category.name
        }),200

@app.route("/categories/<int:id>/update",methods=["PUT"])
def update_category(id):
    data=request.get_json()
    with SessionLocal() as db:
        category = crud.update_category(db,id,**data)
        if not category:
            return jsonify({f"Error: category with id {id} not found"}),400
        return jsonify({
            "id":category.id,
            "name":category.name
        }),204

@app.route("/categories/<int:id>/delete", methods=["DELETE"])
def delete_category(id):
    with SessionLocal() as db:
        category = crud.delete_category(db,id)
        if not category:
            return jsonify({f"Error: category with id {id} not found"}),400
        return jsonify({
            "message": "Category deleted"
        }),200