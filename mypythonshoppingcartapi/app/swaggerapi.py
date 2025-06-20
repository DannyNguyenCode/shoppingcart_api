from flask import Blueprint,jsonify
from flask_restx import Api, Resource,fields
from app.logic import company_logic,category_logic,product_logic

swaggerapp = Blueprint("swagger", __name__)
api = Api(swaggerapp, version="1.0", title="Shopping Cart API", description="API with Swagger UI")


company_namespace = api.namespace("companies", description="Company operations")
company_model = api.model("Company", {
    "id": fields.Integer(required=True, description="Company ID"),
    "name": fields.String(required=False, description="Company name")
})

@company_namespace.route("/")
class CompanyList(Resource):
    @company_namespace.expect(company_model)
    @company_namespace.doc("create_company")

    def post(self):
        try:
            data = api.payload
            company =company_logic.create_company_logic(data.get("id"),data.get("name"))
            return company
        except Exception as error:
            return {"error": f"{error}"},400
        
    @company_namespace.doc("list_companies")
    def get(self):
        try:
            companies = company_logic.list_companies_logic()
            return companies
        except Exception as error:
            return {"error": f"{error}"},400
    

@company_namespace.route("/<int:id>")
@company_namespace.param('id', 'The company identifier')
class Company(Resource):
    @company_namespace.doc("get_company_by_id")
    def get(self,id):
        try:
            company = company_logic.get_company_by_id_logic(id)
            return company
        except Exception as error:
            return {"error": f"{error}"},400
    @company_namespace.expect(company_model)
    @company_namespace.doc("update_company")
    def put(self,id):
        try:
            data = api.payload
            company = company_logic.update_company_logic(id,data)
            return company
        except Exception as error:
            return {"error": f"{error}"},400
    
    @company_namespace.doc("delete_company")
    def delete(self,id):
        try:
            company = company_logic.delete_company_logic(id)
            return company
        except Exception as error:
            return {"error": f"{error}"},400


category_namespace = api.namespace("categories", description="Category operations")
category_model = api.model("Category", {
    "id": fields.Integer(required=True, description="Category ID"),
    "name": fields.String(required=False, description="Category name")
})

@category_namespace.route("/")
class CategoryList(Resource):
    @category_namespace.expect(category_model)
    @category_namespace.doc("create_category")
    def post(self):
        try:
            data = api.payload
            category =category_logic.create_category_logic(data.get("id"),data.get("name"))
            return category
        except Exception as error:
            return {"error": f"{error}"},400
        
    @category_namespace.doc("list_categories")
    def get(self):
        try:
            categories = category_logic.category_list_logic()
            return categories
        except Exception as error:
            return {"error": f"{error}"},400
        

@category_namespace.route("/<int:id>")
@category_namespace.param('id', 'The category identifier')
class Category(Resource):
    @category_namespace.doc("get_category_by_id")
    def get(self,id):
        try:
            category = category_logic.get_category_by_id_logic(id)
            return category
        except Exception as error:
            return {"error": f"{error}"},400
        
    @category_namespace.expect(category_model)
    @category_namespace.doc("update_category")
    def put(self,id):
        try:
            data = api.payload
            category = category_logic.update_category_logic(id,data)
            return category
        except Exception as error:
            return {"error": f"{error}"},400
    
    @category_namespace.doc("delete_category")
    def delete(self,id):
        try:
            category = category_logic.delete_category_logic(id)
            return category
        except Exception as error:
            return {"error": f"{error}"},400