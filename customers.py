import json

CUSTOMER_FILE = "data/customers.json"

def load_customers():
    try:
        with open(CUSTOMER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_customers(customers):
    with open(CUSTOMER_FILE, "w") as f:
        json.dump(customers, f, indent=4)

def list_customers():
    customers = load_customers()
    if not customers:
        print("No customers found.")
        return
    for c in customers:
        print(f"{c['id']}: {c['name']}")

def add_customer():
    customers = load_customers()
    customer_id = max([c["id"] for c in customers], default=0) + 1
    name = input("Customer Name: ")
    customers.append({"id": customer_id, "name": name})
    save_customers(customers)
    print("Customer added successfully!")
