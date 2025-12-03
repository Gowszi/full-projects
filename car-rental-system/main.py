from cars import list_cars
from customers import list_customers
from rentals import list_rentals

def main():
    print("Welcome to Car Rental System\n")
    print("Available cars:")
    list_cars()
    print("\nCustomers:")
    list_customers()
    print("\nRental records:")
    list_rentals()

if __name__ == "__main__":
    main()
