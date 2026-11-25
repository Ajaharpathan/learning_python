
#3. Abstract class with no abstract method 

# from abc import *
# class Parent(ABC):
#     def show(self):
#         print("parent show method")

# class Child(Parent):
#     pass


# c1=Child()
# c1.show()

#note 1. if an abstract class doesn't have any abstract method still you can create object of that class
# print("creating object of abstract parent class and calling show method")
# p1=Parent()
# p1.show() 



#2. Abstract class with abstract method
# from abc import *
# class Parent(ABC):
#     def show(self):
#         print("parent show method")

#     @abstractmethod
#     def m1(self):
#         pass

# class Child(Parent):
#     def display(self):
#         print("Child display method")

 
#     def m1(self):
#         print("m1 method of child class")


# c1=Child()
# c1.m1()   

#note1:  If an abstract class has atleast method you cannot create object of that class

#p1=Parent()   -------error----


#note2: If child class will not implment abstract method of parent class you will not be able to 
# create object of child class


#1. abstract method

# from abc import *

# class Parent:
#     def show(self):
#         print("parent show method")

#     @abstractmethod
#     def m1(self):
#         pass

# class Child(Parent):
#     def m1(self):
#         print("m1 method of child class")        


# c1=Child()
# c1.m1()
# c1.show()        