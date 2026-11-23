class D:
    def m1(self):
        pass

class E:
    def m1(self):
        pass

class F:
    def m1(self):
        pass

class B(D,E):
    def m1(self):
        pass

class C(D,F):
    def m1(self):
        pass

class A(B,C):
    def m1(self):
        pass

a1=A()
  
print(A.__mro__)      
   
a1.m1() 







# class A:
#     def m1(self):
#         print("A m1 called")

# class B:
#     def m1(self):
#         print("B m1 called")

# class C:
#     def m1(self):
#         print("C m1 is called") 

# class D:
#     def m1(self):
#         print("D m1 called")

# d1=D()
  
# print(D.__mro__)      
   
# d1.m1()                       