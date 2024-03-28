class computer:
    def __init__(self,cpu,ram):
        self.cpu="JAk"
        self.ram="8"
    def compare(self,other):
        if self.ram==other.ram:
            return True
        else:
            return False
    
c1=computer("jak","16")
c1.ram=8
c2=computer("sam","32")

if c1.compare(c2):
    print("Both are same")
else:
    print("not same here")

print(c1.cpu)
print(c2.cpu)