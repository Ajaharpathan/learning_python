#3. Constructors with parameter in parents and child

class Person:
    def __init__(self, name ,age):
        self.name=name
        self.age=age

    def persondetails(self):
        print("name:", self.name)
        print("age:", self.age)

class Employee(Person):
    def __init__(self,empid, salary, name, age):
        super().__init__(name, age)    
        self.empid=empid
        self.salary=salary

    def employeedetails(self):
        print("empid:", self.empid)
        self.persondetails()
        print("salary:", self.salary)


e1=Employee(101, 99999, "ajahar", 23)
e1.employeedetails()            
        





# class Parent:

#     def __init__(self):
#         self.a=10
#         print("parents constructor")


#     def m2(self):
#         print("parents m2")



# class Child(Parent):
#     def __init__(self):
#         super().__init__()        
#         self.b=20
#         print("child constructor")


#     def m1(self):
#         print("sum of:", self.a+self.b)

# c1=Child
# c1.m1()
# c1.m2()       









# class Parent:
#     a=10
#     def __init__(self):
#         print("Parents constructor")

#     def insmthd(self):
#         print("parents instmthd")


#     @classmethod
#     def clsmthd(cls):
#         print("Parents clsmthd")

#     @staticmethod
#     def stsmthd():
#         print("parents stsmthd")           


# class Child(Parent):
#     pass

# c1=Child()
# print("instance method:", Child.a)
# print("a=", c1.a)
# print("_______")
# c1.insmthd()
# print("___________")
# c1.clsmthd
# Child.clsmthd()
# print("____________")

# c1.stsmthd
# Child.stsmthd()