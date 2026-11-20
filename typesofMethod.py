class Calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        print("sum=", self.a+self.b)    
        self.sub()

    def sub(sefl):
        print("sub=", sefl.a-sefl.b)


c1=Calculator(20, 10)
c1.add()
print()            



