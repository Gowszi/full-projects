import json
from cars import load_cars, save_cars
from customers import load_customers

RENTAL_FILE = "data/rentals.json"

def load_rentals():
    try:
        with open(RENTAL_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_rentals(rentals):
    with open(RENTAL_FILE, "w") as f:
        json.dump(rentals, f, indent=4)

def list_rentals():
    rentals = load_rentals()
    if not rentals:
        print("No rentals found.")
        return
    for r in rentals:
        print(f"{r['id']}: Customer {r['customer_id']} rented Car {r['car_id']}")

def rent_car():
    cars = load_cars()
    customers = load_customers()
    rentals = load_rentals()

    print("Available Cars:")
    available_cars = [c for c in cars if not c.get("rented")]
    if not available_cars:
        print("No cars available.")
        return
    for car in available_cars:
        print(f"{car['id']}: {car['make']} {car['model']}")

    car_id = int(input("Enter Car ID to rent: "))
    customer_id = int(input("Enter Customer ID: "))

    car = next((c for c in cars if c["id"] == car_id and not c.get("rented")), None)
    customer = next((c for c in customers if c["id"] == customer_id), None)

    if not car:
        print("Invalid or already rented car.")
        return
    if not customer:
        print("Invalid customer.")
        return

    car["rented"] = True
    rental_id = max([r["id"] for r in rentals], default=0) + 1
    rentals.append({"id": rental_id, "customer_id": customer_id, "car_id": car_id})

    save_cars(cars)
    save_rentals(rentals)
    print("Car rented successfully!")

def return_car():
    rentals = load_rentals()
    cars = load_cars()

    print("Current Rentals:")
    for r in rentals:
        print(f"{r['id']}: Customer {r['customer_id']} rented Car {r['car_id']}")

    rental_id = int(input("Enter Rental ID to return: "))
    rental = next((r for r in rentals if r["id"] == rental_id), None)

    if not rental:
        print("Invalid rental ID.")
        return

    car = next((c for c in cars if c["id"] == rental["car_id"]), None)
    if car:
        car["rented"] = False

    rentals = [r for r in rentals if r["id"] != rental_id]

    from cars import save_cars
    save_cars(cars)
    save_rentals(rentals)
    print("Car returned successfully!")
