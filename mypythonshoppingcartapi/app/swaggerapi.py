from flask import Blueprint,jsonify
from flask_restx import Api, Resource,fields
from app.logic import company_logic

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