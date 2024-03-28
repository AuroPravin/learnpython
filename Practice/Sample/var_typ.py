#Types of variable (Understanding program)

class cars:
    wheel=4   #Variable decalred outside is class var

    def __init__(self):
        self.mil=10   #var inside here is instance var
        self.car="BMW"

c1=cars()
c2=cars()
c2.car="Benz"

cars.wheel=5 #here class var get change, it reflect everywhere

print(c1.mil, c1.car, c1.wheel)
print(c1.mil, c2.car, c1.wheel)