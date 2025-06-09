from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Company

# ============ company ============

def create_company(db:Session, id:int,name:str)->Company:
    company = Company(id=id, name=name)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def list_companies(db:Session):
    return db.execute(select((Company))).scalars()    

def get_company_by_id(db:Session,id:int):
    return db.execute(select((Company)).where(Company.id==id)).scalar()

def update_company(db:Session, id:int,**kwargs):
    company = get_company_by_id(db,id)
    if company:
        for key, value in kwargs.items():
            setattr(company,key,value)
        db.commit()
        db.refresh(company)
    return company

def delete_company(db:Session,id:int):
    company = get_company_by_id(db,id)
    if company:
        db.delete(company)
        db.commit()
    return company

# ============ category ============