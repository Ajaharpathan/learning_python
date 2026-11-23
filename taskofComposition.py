class Car:
    model=4
    def __init__(self):
        self.color="red"


class Employee:
    def __init__(self,eid, name, sal):
        self.eid=eid
        self.name=name
        self.sal=sal
        self.c=Car()


    def show(self):
        print("eid:", self.eid)
        print("name:", self.name)
        print("sal:", self.sal)
        print("model:", self.c.model)
        print("color:", self.c.color)
        

e=Employee(101, "ajahar", 25000)
e.show()                   
