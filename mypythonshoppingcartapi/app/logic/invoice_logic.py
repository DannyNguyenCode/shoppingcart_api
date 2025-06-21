# app/logic/invoice_logic.py

from app import crud, services
from app.db import SessionLocal

def get_invoice_by_id_logic(id: int):
    try:
        with SessionLocal() as db:
            invoice = crud.get_invoice_by_id(db, id)
            if not invoice:
                return {"error": f"Invoice with id {id} not found"}, 404
            return services.generate_response(
                message="Invoice retrieved",
                status=200,
                data=invoice.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def list_invoices_logic():
    try:
        with SessionLocal() as db:
            invoices = crud.list_invoices(db)
            invoice_dicts = [invoice.to_dict() for invoice in invoices]
            return services.generate_response(
                message="Invoice list retrieved",
                status=200,
                data={"invoices": invoice_dicts}
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400

def create_invoice_logic(id: int, total_price: float, payment_status: str, created_at: str, paid_at: str, order_id: int):
    try:
        with SessionLocal() as db:
            invoice = crud.create_invoice(db, id, total_price, payment_status, created_at, paid_at, order_id)
            if not invoice:
                return {"error": "Invoice creation failed"}, 500
            return services.generate_response(
                message="Invoice created",
                status=201,
                data=invoice.to_dict()
            ), 201
    except Exception as error:
        return {"error": f"{error}"}, 500

def update_invoice_logic(id: int, **kwargs):
    try:
        with SessionLocal() as db:
            invoice = crud.update_invoice(db, id, **kwargs)
            if not invoice:
                return {"error": f"Invoice with id {id} not found"}, 404
            return services.generate_response(
                message="Invoice updated",
                status=200,
                data=invoice.to_dict()
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 500

def delete_invoice_logic(id: int):
    try:
        with SessionLocal() as db:
            invoice = crud.delete_invoice(db, id)
            if not invoice:
                return {"error": f"Invoice with id {id} not found"}, 404
            return services.generate_response(
                message="Invoice deleted",
                status=200,
                data=invoice
            ), 200
    except Exception as error:
        return {"error": f"{error}"}, 400
