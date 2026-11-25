#Overriding Example


class Parent:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def m1(self):
        sum=(self.a+self.b+self.c)
        print(sum)

class Child(Parent):
    def m1(self):
            mul=(self.a*self.b*self.c)
            print(mul)

c=Child()
c.m1()