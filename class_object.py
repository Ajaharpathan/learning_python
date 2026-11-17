# class Student:
#     def accept(self, rno,name):
#         self.rno=rno
#         self.name=name

#     def show(self):
#         print("rollno", self.rno)
#         print("name:", self.name)


# s1=Student()
# print("s1", s1)

# s1.accept(101, "tom")
# s1.show()

# print("__________")
# s2=Student()

# class Employee():
#     def accept(self, id, name, salary):
#      self.id=id
#      self.name=name 
#      self.salary=salary

#     def show(self):
#        self.id
#        self.name
#        self.salary
#        print("id", self.id)
#        print("name", self.name)
#        print("salary", self.salary)



# s1=Employee()
# s1.accept(1, "ajahar", 89000)
# s1.show()


#constructor

# class Student:
#     def __init__(self):
#         print("this is constructor")
#         self.rno=int(input("Enter rno:"))
#         self.rname=(input("Enter name:"))
#         print()

#     def show(self):
#         print("Roll No:", self.rno)
#         print("Name:", self.name)

# s1=Student()
# s2=Student()
# print("***********")
# s1.show()
# print()
# s2.show()         

# class Student():
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("Self Name", self.name)
#         print("Self Age:", self.age)

# s1=Student(1, "ajahar")
# s1.show()             




#in python not support method overloading
# class Student:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age

#     def __init__(self):
#         self.name="ajahr"
#         self.age=32

#     def show(self):
#         print(self.name)
#         print(self.age)

# s1=Student()
# s1.show                


class Calc:
    def __init__(self, no1, no2):
        self.no1=no1
        self.no2=no2

    def add(self):
        print("Addition of two number is:", self.no1 + self.no2)

    def sub(self):
        print("Substaction of two number is:", self.no1 - self.no2)

    def mul(self):
            print("Substaction of two number is:", self.no1 * self.no2)

    def div(self):
            print("Substaction of two number is:", self.no1 / self.no2)                


s1=Calc(10, 20)
s1.add()
s1.sub()
s1.mul()
s1.div()
