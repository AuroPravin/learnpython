class Car:
    def __init__(self, make, model, year, mileage, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available

class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year and car.available:
                car.available = False
                return car
        return None

    def return_car(self, make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year and not car.available:
                car.available = True
                return car
        return None

    def display_available_cars(self):
        print("Available Cars:")
        for car in self.cars:
            if car.available:
                print(f"{car.make} {car.model} ({car.year}) - Mileage: {car.mileage}")

#user input:
car_rental_system = CarRentalSystem()

while True:
    print("\n1. Add Car")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Display Available Cars")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        year = input("Enter the year of the car: ")
        mileage = input("Enter the mileage of the car: ")
        car = Car(make, model, year, mileage)
        car_rental_system.add_car(car)
        print("Car added successfully!")

    elif choice == "2":
        make = input("Enter the make of the car to rent: ")
        model = input("Enter the model of the car to rent: ")
        year = input("Enter the year of the car to rent: ")
        rented_car = car_rental_system.rent_car(make, model, year)
        if rented_car:
            print(f"Car {rented_car.make} {rented_car.model} ({rented_car.year}) rented successfully!")
        else:
            print("Car not available for rent.")

    elif choice == "3":
        make = input("Enter the make of the car to return: ")
        model = input("Enter the model of the car to return: ")
        year = input("Enter the year of the car to return: ")
        returned_car = car_rental_system.return_car(make, model, year)
        if returned_car:
            print(f"Car {returned_car.make} {returned_car.model} ({returned_car.year}) returned successfully!")
        else:
            print("Car not found or already returned.")

    elif choice == "4":
        car_rental_system.display_available_cars()
        
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
