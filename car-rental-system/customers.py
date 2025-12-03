import json

def list_customers():
    try:
        with open("data/customers.json", "r") as f:
            customers = json.load(f)
            for c in customers:
                print(f"{c['id']}: {c['name']}")
    except FileNotFoundError:
        print("No customer data found.")
