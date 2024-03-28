 # Class & Object :
#========================

#Example 1:

'''
class computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1=computer()
com2=computer()

com1.config()
com2.config()

'''

#Example 2: __init__ or Constructor

'''

class robot:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def introduce(self):
        print("hello, i am "+self.name+" and i am in " +self.color+" color")
 
#object creation for robot
name=input("Enter the name for ur robot: ")
color=input("Enter the color: ")

r1=robot(name,color)

#printing the information for robot
print("my name is: "+r1.name+"\nmy color is: "+r1.color)
r1.introduce()

'''

#Example 3: 

'''
class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print("Hello, I am " + self.name + " and I am in " + self.color + " color")

# Create the first robot object
name1 = input("Enter the name for your first robot: ")
color1 = input("Enter the color: ")
r1 = Robot(name1, color1)

# Print information about the first robot
print("Information about the first robot:")
print("My name is: "+ r1.name+"\nMy color is: " + r1.color)
r1.introduce()

# Create the second robot object
name2 = input("Enter the name for your second robot: ")
color2 = input("Enter the color: ")
r2 = Robot(name2, color2)

# Print information about the second robot
print("\nInformation about the second robot:")
print("My name is: " + r2.name+"\nMy color is: " + r2.color)
r2.introduce()

'''

# Example 3 in shorter way using function concept:

class robot:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def intro(self):
        print(f"Hello, i am {self.name}\nand i'm in {self.color}")
    
#Creating robot
def create_robo():
    return robot(input("Enter the name: "),input("Enter the color: "))

#info about the robot
def intro_robo(ro):
    print(f"my name is: {ro.name}\nmy color is: {ro.color}")
    ro.intro()

#declaring the object 1:
robot1=create_robo()
print("Information")
intro_robo(robot1)
