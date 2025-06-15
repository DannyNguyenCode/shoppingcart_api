from flask import Flask, request, jsonify
from app.db import SessionLocal, engine
from sqlalchemy.exc import IntegrityError
from app import crud, models,services

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# ============ company ============

@app.route("/companies/create",methods=["POST"])
def create_company():
    try:
        with SessionLocal() as db:
            data = request.get_json()
            company = crud.create_company(db, data.get("id"), data.get("name"))
            # converting sqlalchemy's returning to a dictionary
            keys =['id','name']
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Created",201)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),201
    except IntegrityError as integrityError:
        error_msg = str(integrityError.orig).lower()
        if "unique constraint" in error_msg or "duplicate key value" in error_msg:
            return jsonify({"error": f"id={data.get("id")} already exists"}), 409
        elif "not-null constraint" in error_msg:
            return jsonify({"error": "id is a required field"}), 400
        else:
            return jsonify({"error": f"{error_msg}"}),400
    except Exception as e:
        return jsonify({"error": f"{e}"}),400


@app.route("/companies", methods=["GET"])
def list_companies():
    try:
        with SessionLocal() as db:
            companies=crud.list_companies(db)
            return jsonify([company.to_dict() for company in companies]),200
    except Exception as error:
        return jsonify({"Error": f"{error}"}) 

@app.route("/companies/<int:id>",methods=["GET"])
def get_company_by_id(id):
    try:
        with SessionLocal() as db:
            company = crud.get_company_by_id(db,id)
            if not company:
                return jsonify({"error": "Company not found"}), 404
            return jsonify(company.to_dict()),200
    except Exception as error:
        return jsonify({"error":f"{error}"})

@app.route("/companies/<int:id>/update", methods=["PUT"])
def update_company(id):
    try:
        with SessionLocal() as db:
            data=request.get_json()
            company = crud.update_company(db,id,**data)
            if not company:
                return jsonify({"error":"id is required"}),400
            # converting sqlalchemy's returning to a dictionary
            keys =['id','name']
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Updated",200)
             # return dictionary in json format to response
            return jsonify(
                dictionary
            ),200
    except Exception as error:
        return jsonify({"error":f"{error}"})


@app.route("/companies/<int:id>/delete",methods=["DELETE"])
def delete_company(id):
    try:
        with SessionLocal() as db:
            company = crud.delete_company(db,id)
            if not company:
                return jsonify({"error": "Company not found"}), 404
            # converting sqlalchemy's returning to a dictionary
            keys =['id','name']
            values = company[0]
            dictionary = services.generate_response(keys, values,"Company Deleted",200)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),200
    except Exception as error:
         return jsonify({"error":f"{error}"})


# ============ category ============


@app.route("/categories/create",methods=["POST"])
def create_category():
    try:
        with SessionLocal() as db:
            data = request.get_json()
            category = crud.create_category(db, data.get("id"), data.get("name"))
            # converting sqlalchemy's returning to a dictionary  
            keys =['id','name']
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Created",201)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),201

    except IntegrityError as integrityError:
        error_msg = str(integrityError.orig).lower()
        if "unique constraint" in error_msg or "duplicate key value" in error_msg:
            return jsonify({"error": f"id={data.get("id")} already exists"}), 409
        elif "not-null constraint" in error_msg:
            return jsonify({"error": "id is a required field"}), 400
        else:
            return jsonify({"error": f"{error_msg}"}),400
    except Exception as e:
        return jsonify({"error": f"{e}"}),400

    
@app.route("/categories",methods=["GET"])
def list_categories():
    try:
        with SessionLocal() as db:
            categories = crud.list_categories(db)
            return jsonify([category.to_dict() for category in categories]),200
    except Exception as error:
        return jsonify({"error":f"{error}"})

@app.route("/categories/<int:id>",methods=["GET"])
def get_category_by_id(id):
    try:
        with SessionLocal() as db:
            category = crud.get_category_by_id(db,id)
            if not category:
                return jsonify({"error": f"category with id {id} not found"})
            return jsonify({
                "id":category.id,
                "name":category.name,
                "products":[
                    {
                        "id":product.id,
                        "name":product.name,
                        "price":product.price,
                        "description":product.description,
                        "stock_quantity":product.stock_quantity,
                        "category_id":product.category_id,
                        "company_id":product.company_id
                        }for product in category.product]
            }),200
    except Exception as error:
        return jsonify({"error":f"{error}"})

@app.route("/categories/<int:id>/update",methods=["PUT"])
def update_category(id):
    try:
        data=request.get_json()
        with SessionLocal() as db:
            category = crud.update_category(db,id,**data)
            if not category:
                return jsonify({"error":"id is required"}),400
            # converting sqlalchemy's returning method to a dictionary
            keys =['id','name']
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Updated",200)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),200
    except Exception as error:
        return jsonify({"error":f"{error}"})

@app.route("/categories/<int:id>/delete", methods=["DELETE"])
def delete_category(id):
    try:
        with SessionLocal() as db:
            category = crud.delete_category(db,id)
            if not category:
                return jsonify({"error": "Category not found"}), 404
            # converting sqlalchemy's returning to a dictionary       
            keys =['id','name']
            values = category[0]
            dictionary = services.generate_response(keys, values,"Category Deleted",200)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),200
    except Exception as error:
        return jsonify({"error":f"{error}"})
    

# ============ product ============

@app.route("/products/create",methods=["POST"])
def create_product():
    try:
        with SessionLocal() as db :
            data = request.get_json()

            # first check relationship category exists
            category = crud.get_category_by_id(db,data.get("category_id"))
            if not category:
                return jsonify({"error": f"category with id {data.get("category_id")} not found"}),400
            
            # second check relationship company exists
            company = crud.get_company_by_id(db,data.get("company_id"))
            if not company:
                return jsonify({"error": f"company with id {data.get("company_id")} not found"}),400
            
            # third if all pass, create product and commit to database
            product = crud.create_product(db,data.get("id"),data.get("name"),data.get("price"),data.get("description"),data.get("category_id"),data.get("stock_quantity"),data.get("company_id"))
            
            # converting sqlalchemy's returning to a dictionary
            keys =["name","price","description","category_id","stock_quantity","company_id","company","category"]
            values = product[0]
            dictionary = services.generate_response(keys, values,"Product Created",201)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),201
    except IntegrityError as integrityError:
        error_msg = str(integrityError.orig).lower()
        if "unique constraint" in error_msg or "duplicate key value" in error_msg:
            return jsonify({"error": f"User with id={data.get("id")} already exists"}), 409
        elif "not-null constraint" in error_msg:
            return jsonify({"error": "id is a required field"}), 400
        else:
            return jsonify({"error": f"{error_msg}"}),400
    except Exception as error:
        return jsonify({"error":f"{error}"})

@app.route("/products",methods=["GET"])
def product_list():
    try:
        with SessionLocal() as db:
            products = crud.product_list(db)
            return jsonify([product.to_dict() for product in products]),200
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400
    
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    try:
        with SessionLocal() as db:
            product = crud.get_product_by_id(db,id)
            if not product:
                return jsonify({"error":f"product id={id} not found"})
            return jsonify(product.to_dict()),200
    except Exception as error:
        return jsonify({"Error":f"{error}"}),400


@app.route("/products/<int:id>/update",methods=["PUT"])
def update_product(id):
    try:
        with SessionLocal() as db :
            data = request.get_json()
            product = crud.update_product(db,id,**data)
            if not product:
                return jsonify({"error":"id is required"}),400
            # converting sqlalchemy's returning to a dictionary     
            keys =["name","price","description","category_id","stock_quantity","company_id"]
            values = product[0]
            dictionary = services.generate_response(keys, values,"Product Updated",200)
            # return dictionary in json format to response
            return jsonify(
                dictionary
            ),200
                 
    except Exception as error:
        return jsonify({"error":f"{error}"}),400

@app.route("/products/<int:id>/delete",methods=["DELETE"])
def delete_product(id):
    try:
        with SessionLocal() as db:
            product = crud.delete_product(db,id)
            if not product:
                return jsonify({"error":"product not found"}),400 
            keys =["name","price","description","category_id","stock_quantity","company_id"]
            values = product[0]
            dictionary = services.generate_response(keys, values,"Product Deleted",200)
            return jsonify(
                dictionary
            ),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    

# ============ user ============
    
@app.route("/users/create",methods=["POST"])
def create_user():
    try:
        with SessionLocal() as db:
            data = request.get_json()
            user = crud.create_user(db,data.get("id"),data.get("full_name"),data.get("email"),data.get("password"),data.get("phone"))    
            keys =['id','full_name',"email","password","phone"]
            values = user[0]
            dictionary = services.generate_response(keys, values,"User Created",201)

            return jsonify(
                dictionary
            ),201
    except IntegrityError as integrityError:
        error_msg = str(integrityError.orig).lower()
        if "unique constraint" in error_msg or "duplicate key value" in error_msg:
            return jsonify({"error": f"User with id={data.get("id")} already exists"}), 409
        elif "not-null constraint" in error_msg:
            return jsonify({"error": f"id is a required field {error_msg}"}), 400
        else:
            return jsonify({"error": f"{error_msg}"}),400
    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
@app.route("/users",methods=["GET"])
def users_list():
    try:
        with SessionLocal() as db:
            users = crud.user_list(db)
            return jsonify([user.to_dict() for user in users]),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
@app.route("/users/<int:id>",methods=["GET"])
def get_user_by_id(id):
    try:
        with SessionLocal() as db:
            user = crud.get_user_by_id(db,id)
            if not user:
                return jsonify({"error":f"user id={id} not found"})
            return jsonify(user.to_dict()),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400

@app.route("/users/<int:id>/update",methods=["PUT"])
def update_user(id):
    try:
        with SessionLocal() as db:
            data = request.get_json()
            user = crud.update_user(db,id,**data)
            if not user:
                return jsonify({"error":f"id is required"})
            keys=["id","full_name","email","password","phone"]
            values = user[0]
            dictionary = services.generate_response(keys,values,"User Updated",200)
            return jsonify(dictionary),200

    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
@app.route("/users/<int:id>/delete",methods=["DELETE"])
def delete_user(id):
    try:
        with SessionLocal() as db:
            user = crud.delete_user(db,id)
            if not user:
                return jsonify({"error":f"User not found"})
            keys=["id","full_name","email","password","phone"]
            values = user[0]
            dictionary = services.generate_response(keys,values,"User Deleted",200)
            return jsonify(dictionary),200

    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
# ============ address ============

@app.route("/addresses/create",methods=["POST"])
def create_address():
    try: 
        with SessionLocal() as db:
            data = request.get_json()
            address = crud.create_address(db,data.get("id"),data.get("street_address"),data.get("state"),data.get("postal_code"),data.get("country"),data.get("user_id"))
            keys = ["id","street_address","state","postal_code","country","user_id"]
            values = address[0]
            dictionary = services.generate_response(keys,values,"Address Created",200)
            return jsonify(dictionary),200
    except IntegrityError as integrityError:
        error_msg = str(integrityError.orig).lower()
        if "unique constraint" in error_msg or "duplicate key value" in error_msg:
            return jsonify({"error": f"User with id={data.get("id")} already exists"}), 409
        elif "not-null constraint" in error_msg:
            return jsonify({"error": f"id is a required field {error_msg}"}), 400
        else:
            return jsonify({"error": f"{error_msg}"}),400
    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
@app.route("/addresses",methods=["GET"])
def address_list():
    try:
        with SessionLocal() as db:
            addresses = crud.address_list(db)
            return jsonify([address.to_dict() for address in addresses]),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400

@app.route("/addresses/<int:id>",methods=["GET"])
def get_address_by_id(id):
    try:
        with SessionLocal() as db:
            address = crud.get_address_by_id(db,id)
            if not address:
                return jsonify({"error":f"address id={id} not found"})
            return jsonify(address.to_dict()),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400
    
@app.route("/addresses/<int:id>/update",methods=["PUT"])
def update_address(id):
    try:
        with SessionLocal() as db:
            data = request.get_json()
            address = crud.update_address(db,id,**data)
            if not address:
                return jsonify({"error":f"id is required"}),400
            keys = ["id","street_address","state","postal_code","country","user_id"]
            values = address[0]
            dictionary = services.generate_response(keys,values,"Address Updated",200)
            return jsonify(dictionary),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400

@app.route("/addresses/<int:id>/delete",methods=["DELETE"])
def delete_address(id):
    try:
        with SessionLocal() as db:
            address = crud.delete_address(db,id)
            if not address:
                jsonify({"error":"id is required"}),400
            keys = ["id","street_address","state","postal_code","country","user_id"]
            values = address[0]
            dictionary=services.generate_response(keys,values,"Address Deleted",200)
            return jsonify(dictionary),200
    except Exception as error:
        return jsonify({"error":f"{error}"}),400

