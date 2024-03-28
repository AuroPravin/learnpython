class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop
    def show(self):
        print(self.name, self.roll)

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=2

        def show(self):
            print(self.brand,self.name, self.roll)
            self.lap.show()



s1=student("jak",20)
s2=student("bet",24)

lap1=student.laptop
lap2=student.laptop

s1.show()