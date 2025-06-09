import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app import crud

TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(TEST_DATABASE_URL, echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_car(db_session):
    car = crud.create_car(db_session, car_vin="VIN123", car_make="Toyota", car_model="Corolla", car_year=2021, id=1)
    assert car.car_VIN == "VIN123"
    assert car.car_make == "Toyota"
    assert car.car_model == "Corolla"
    assert car.car_year == 2021
    assert car.id == 1

def test_get_car(db_session):
    crud.create_car(db_session, car_vin="VIN123")
    car = crud.get_car(db_session, "VIN123")
    assert car is not None
    assert car.car_VIN == "VIN123"

def test_update_car(db_session):
    crud.create_car(db_session, car_vin="VIN123", car_make="Honda")
    updated_car = crud.update_car(db_session, "VIN123", car_make="Toyota", car_year=2022)
    assert updated_car.car_make == "Toyota"
    assert updated_car.car_year == 2022

def test_delete_car(db_session):
    crud.create_car(db_session, car_vin="VIN123")
    success = crud.delete_car(db_session, "VIN123")
    assert success is True
    car = crud.get_car(db_session, "VIN123")
    assert car is None

def test_list_cars(db_session):
    crud.create_car(db_session, car_vin="VIN1")
    crud.create_car(db_session, car_vin="VIN2")
    cars = crud.list_cars(db_session)
    assert len(cars) == 2
    vins = {car.car_VIN for car in cars}
    assert vins == {"VIN1", "VIN2"}
