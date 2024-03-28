#INHERITANCE CONCEPT (UNDERSRTANDING CODE)

#understanding code:

'''

class mobile:
    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")

class Tmobile(mobile):
    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

class Kmobile(Kmobile):
    def feature5(self):
        print("Feature5 is working")

    def feature6(self):
        print("Feature6 is working")

samsung=mobile()

samsung.feature1()
samsung.feature2()
'''

#Single inheritance Example 1:

'''
#Super class/Parent class
class animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        pass

#Child class
class dog(animal):
    def sound(self):
        return "Bark: lol, lol"
    
class cat(animal):
    def sound(self):
        return "meow, meow"
    
#Getting animal details   
animal_type=input("enter animal type (dog/cat): ").lower()
animal_name=input("enter animal name: ")

if animal_type=="dog":
    animal=dog(animal_name)
elif animal_type=="cat":
    animal=cat(animal_name)
else:
    print("Invalid input")

#final Output    
print(f"{animal.name} says {animal.sound()}")

'''
# multiple inheritance 

class ddevice:
    def __init__(self,brand,name):
        self.brand=brand
        self.name=name

    def desc(self):
        return f"{self.brand}{self.name}"
    
class phone(ddevice):
    def call(self):
        return f"making a call using {self.desc()}"

class tablet(ddevice):
    def notes(self):
        return f"u can take notes with {self.desc()}"    


class student:
    def study(self):
        return "studying"
    
class emp:
    def work(self):
        return "work"
    

Sphone=phone("mi","note 4")
Tablet=tablet("Samsu","oneplus")
Student=student()
Emp=emp()


print(Sphone.call())
print(Tablet.notes())
print(Student.study())
print(Emp.work())


# Multilevel Inheritance Example

class vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def info(self):
        return f"make:{self.make},model:{self.model}"
    
class car(vehicle):
    def __init__(self, make, model,doors):
        super().__init__(make, model)
        self.doors=doors

    def drive(self):
        return "Driving car"

class motorbike(vehicle):
    def __init__(self, make, model,engine):
        super().__init__(make, model)
        self.engine=engine

    def ride(self):
        return "Riding Motorcycle"

class ecar(car):
    def __init__(self, make, model,doors,range):
        super().__init__(make, model,doors)
        self.range=range

    def charge(self):
        return "charge e car"
    

vehicle_type=input("Enter vehicle type (car/motorbike/ecar) : ").lower()
make=input("Enter vehicle make :")
model=input("Enter the vehicle mode: ")

if vehicle_type=="car":
    doors=int(input("Enter no. of doors :"))
    vehicle=car(make,model,doors)
elif vehicle_type=="motorbike":
    engine=input("Enter the engine :")
    vehicle=motorbike(make, model, engine)
else:
    print("Invalid Vehicle type")

print(vehicle.info())

if isinstance(vehicle,car):
    print(vehicle.drive())
elif isinstance(vehicle,motorbike):
    print(vehicle.ride())
elif isinstance(vehicle,ecar):
    print(vehicle.charge())

   