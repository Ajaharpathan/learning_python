#4. Multiple Inheritance

class Parent1:
    def m1(self):
        print("parent1 m1 method")

class Parent2:
    def m2(self):
        print("Parent2 m2 method")

class Child(Parent1, Parent2):
    def m3(self):
        print("Child m3 method") 


c1=Child()
c1.m1()
c1.m2()
c1.m3()                  


#3. Heirchical 

# class Parent:
#     def m1(self):
#         print("parent m1 method")

# class Child1(Parent):
#     def m2(self):
#         print("child m2 method")


# class Child2(Parent):
#     def m3(self):
#         print("child m3 method") 

# c1=Child1()
# c1.m2()
# c1.m1()                       
# print("__________")
# c2=Child2()
# c2.m1()
# c2.m3()



#2, Multilevel Inheritance
"""
  A
  |
  B
  |
  C


"""

# class Gparent:
#     def m1(self):
#         print("gparent m1")

# class Parent(Gparent):
#     def m2(self):
#         print("parent m2")

# class Child(Parent):
#     def m3(self):
#         print("child m3")          


# c1=Child()
# c1.m1()
# c1.m2()
# c1.m3()        


#single inheritance
#   A
#   |
#   B 