
#4..accessing private member outside the class

class Parent:
    __a=10
    def __init__(self):
        self.__b=20

    def show(self):
        print("a=",Parent.__a)
        print("b=",self.__b)

p1=Parent()
p1.show()
print("a outside class:",p1._Parent__a)

#3.Protected
# class Parent:
#     _a=10
#     def __init__(self):
#         self._b=20
#
#     def show(self):
#         print("a=",Parent._a)
#         print("b=",self._b)
#
# class Child(Parent):
#     def display(self):
#         print("a=",Child._a)
#         print("b=",self._b)
#
# c1=Child()
# c1.display()
#
# print("------------------------------")
#
# p1=Parent()
# p1.show()
#
# print("-----------------------")
# print("c1._a:",c1._a)
# print("c1._b:",c1._b)

#2.Private

# class Parent:
#     __a=10
#     def __init__(self):
#         self.__b=20
#
#     def show(self):
#         print("a=",Parent.__a)
#         print("b=",self.__b)
#
# class Child(Parent):
#     def display(self):
#         print("a=",Child.__a)
#         print("b=",self.__b)
#
# c1=Child()
# c1.display()
# print(c1.__a)


# p1=Parent()
# p1.show()