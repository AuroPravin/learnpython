# Types of methods available in python 
# UNDERSTANDING PROGRAM EXAMPLE



# Example 1: 

'''

class students:
    def __init__(self,name1,name2,name3):
        self.name1=name1
        self.name2=name2
        self.name3=name3
    def list(self):
        print(self.name1, self.name2, self.name3)
    @classmethod
    def school(cls):
        return cls.school

secA=students("Ambi","babu","chan")
secB=students("keerthi","lav","meen")

secA.list()
print(students.school)

'''

# Example 2: 

'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        print(f"The car has been driven for {distance} miles.")

    def honk(self):
        print("Beep beep!")

    @staticmethod
    def about():
        print("This is a car. It can drive and honk.")

    @classmethod
    def from_string(cls, car_string):
        brand, model, year = car_string.split('-')
        return cls(brand, model, int(year))


#Creating car object
my_car = Car("Toyota", "Camry", 2020)

#Drive the car
my_car.drive(100)

#Honk
my_car.honk()

#information about the car
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Mileage: {my_car.mileage}")

#Static method 
Car.about()

#Class method 
new_car = Car.from_string("Ford-Focus-2018")
print(f"New car: {new_car.brand} {new_car.model} {new_car.year}")

'''


 