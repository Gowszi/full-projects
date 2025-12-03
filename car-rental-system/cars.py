import json

def list_cars():
    try:
        with open("data/cars.json", "r") as f:
            cars = json.load(f)
            for car in cars:
                print(f"{car['id']}: {car['make']} {car['model']} ({car['year']})")
    except FileNotFoundError:
        print("No car data found.")
