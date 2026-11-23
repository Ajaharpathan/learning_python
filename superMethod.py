
#.4. Using super() in multilevel inheritance

class A:
    def m1(self):
         print("A class m1")

class B(A):
    def m1(self):
        print("B class m1") 

class C(B):
    def m1(self):
        A.m1(self)
        # super(B,self).m1() 
        print("c Class m1")               





#3.Accessing in childs static method
# class A:
#     @classmethod
#     def m2(cls):
#         print("parent class - class method")
#
#     @staticmethod
#     def m3():
#         print("parent class static method")
#
# class C(A):
#     @staticmethod
#     def m1():
#         super(C,C).m2()
#         super(C,C).m3()
#
# c=C()
# c.m1()



#2.Accessing properties of parent in childs class method
class Parent():
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        print("Parent instance  method")

    @classmethod
    def m2(cls):
        print("parent class Class Method")

    @staticmethod
    def m3():
        print("parent class Static Method")

class Child(Parent):
    a=80
    def __init__(self):
        self.b=100

    @classmethod
    def clsmthd(cls):
        print("a=",super().a)
        #super().__init__() -error
        #super().m1()--error
        super().m2()
        super().m3()


c1=Child()
c1.clsmthd()




#1. accesssing properties of  parent class using super () in child's constructor
#
# class Parent():
#     a=10
#     def __init__(self):
#         self.b=20

#     def m1(self):
#         print("Parent instance method")



#     @classmethod 
#     def m2(cls):
#         print("Parent class Class Method")

#     @staticmethod
#     def m3():
#         print("parent class Static method")


# class Child(Parent):
#     a = 80
#     def __init__(self):
#         self.b=100
#         super().__init__()
#         print("a=", self.a)
#         print("parent a:", super().a)
#         print("b  :", self.b) #note you cannot use instance variable with super() it gives error so use self
#         super().m1()
#         super().m2()
#         super().m3()

# c=Child()
# c.m1()        