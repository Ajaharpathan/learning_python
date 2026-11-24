#3. Operator overloading with different objects

class Employee:
    def __init__(self, name, salperday):
        self.name=name
        self.salperday= salperday



class Timesheet:
    def __init__(self, name, noofdays):
        self.name=name
        self.noofdays=noofdays


    def __mul__(self, other):
        return self.noofdays * other.salperday




e1=Employee("ajahar", 9000)
t1=Timesheet("Pathan", 30)
#print("total salary:",e1*t1)
print("total salary:",t1*e1)










#2. Operator overloading with adding 3 objects

# class Book:
#     def __init__(self, pages):
#         self.pages=pages


#     def __add__(self, other):
#         print("self=", self.pages)
#         print("other=",other.pages)
#         s=self.pages+other.pages
#         return Book(s)

#     def __str__(self):
#         return str(self.pages)



# b1=Book(20)
# b2=Book(30)
# b3=Book(50)
# b4=b1+b2+b3
# print(b4)    





#1. 
# class Book:
#     def __init__(self, pages):
#         self.pages=pages

#     def __add__(self, other):
#         print("self=", self.pages)
#         print("other=", other.pages)
#         s=self.pages+other.pages
#         return s


# b1=Book(20)
# b2=Book(30)
# b3=b1+b2
# print("total pages of b1 and b2:", b3)        