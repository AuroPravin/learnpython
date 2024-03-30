# Polymorphism 
'''
    Polymorphism is a fundamental concept in object-oriented programming (OOP) that refers to the ability of different
    objects to respond to the same message or method invocation in different ways. 
    It allows objects of different classes to be treated as objects of a common superclass, 
    enabling code reuse and flexibility in design.

    there are different shapes in the topic shape, but the area calculation
    starts for particular one based on the user input specified. thats what i understood
        
    
'''



#sample program 1: Find area of the shape

import math

#parent class as shape
class shape:
    def calculation(self):
        pass

#Child class1 as rect
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def calculation(self):
        return self.width*self.height

#Child class2 as circle    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def calculation(self):
        return math.pi*self.radius**2
    

 #user input
shape_type=input("Enter your shape(rectangle/circle) :").lower()

if shape_type=="rectangle":
    width=float(input("Enter the width : "))
    height=float(input("Enter the height : "))
    shaped=rectangle(width,height)
elif shape_type=="circle":
    radius=float(input("enter radius: "))
    shape=circle(radius)
else:
    print("Invalid shape ,(type rectangle or circle only)")


area=shape.calculation()
print(f"The area of {shape_type} is: {area}")




# sample Program 2: animal sound

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Get user input
animal_type = input("Enter animal type (dog/cat): ").lower()

if animal_type == "dog":
    animal = Dog()
elif animal_type == "cat":
    animal = Cat()
else:
    print("Invalid animal type")
    exit()

# Make sound
sound = animal.make_sound()
print(f"The {animal_type} says: {sound}")
