from cars import list_cars, add_car
from customers import list_customers, add_customer
from rentals import list_rentals, rent_car, return_car

def main():
    while True:
        print("\n--- Car Rental System ---")
        print("1. List Cars")
        print("2. List Customers")
        print("3. List Rentals")
        print("4. Add Customer")
        print("5. Rent Car")
        print("6. Return Car")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_cars()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            list_rentals()
        elif choice == "4":
            add_customer()
        elif choice == "5":
            rent_car()
        elif choice == "6":
            return_car()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
