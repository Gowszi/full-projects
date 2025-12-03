import json

CAR_FILE = "data/cars.json"

def load_cars():
    try:
        with open(CAR_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_cars(cars):
    with open(CAR_FILE, "w") as f:
        json.dump(cars, f, indent=4)

def list_cars():
    cars = load_cars()
    if not cars:
        print("No cars found.")
        return
    for car in cars:
        status = "Available" if not car.get("rented") else "Rented"
        print(f"{car['id']}: {car['make']} {car['model']} ({car['year']}) - {status}")

def add_car():
    cars = load_cars()
    car_id = max([c["id"] for c in cars], default=0) + 1
    make = input("Car Make: ")
    model = input("Car Model: ")
    year = input("Car Year: ")
    cars.append({"id": car_id, "make": make, "model": model, "year": year, "rented": False})
    save_cars(cars)
    print("Car added successfully!")
