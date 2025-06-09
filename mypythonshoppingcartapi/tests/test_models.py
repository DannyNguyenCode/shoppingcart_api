import json
from app.models import Car

def test_car_model_instantiation():
    car = Car(
        car_VIN="VIN123",
        car_make="Toyota",
        car_model="Camry",
        car_year=2020,
        id=1
    )
    assert car.car_VIN == "VIN123"
    assert car.car_make == "Toyota"
    assert car.car_model == "Camry"
    assert car.car_year == 2020
    assert car.id == 1

def test_car_repr_returns_valid_json():
    car = Car(
        car_VIN="VIN456",
        car_make="Honda",
        car_model="Accord",
        car_year=2019,
        id=2
    )
    repr_str = repr(car)
    data = json.loads(repr_str)
    assert data["car_VIN"] == "VIN456"
    assert data["car_make"] == "Honda"
    assert data["car_model"] == "Accord"
    assert data["car_year"] == 2019
    assert data["id"] == 2
