#static variable

#6. updating
class Test:
    a=10  #static variable
    def __init__(self):
        self.a=20  #instance variable

    # def m1(self):
    #     del self.a   

t1=Test()
Test.a=100
print(Test.a)              #del Test.a   del t1.a
print("_________________")
t1.a=500
print("Test.a:",Test.a)
print("t1.a:",t1.a)
# t1.m1()


#5.Accessing static variable
# class Test:
#     a =10 #static variable 
#     def __init__(self):
#          Test.a=100
#          print("a in constructor:", Test.a)
#          print("a using self:", self.a)
#          print("_________")

#     def m1(self):
#          print("a in inst method with Test:", Test.a)
#          print("a using self in inst method: ", self.a)
#          print("_____")

#     @classmethod         
#     def m2(cls):
#          print("a in class method using test:", Test.a) 
#          print("a in class method using self:", cls.a)
#          print("________")

#     @staticmethod
#     def m3():
#          print("a in static method with Test:", Test.a)
#          print("______")

# print("a outside clss:",Test.a)
# t1=Test()
# print("a with refvar:",t1.a)
# t1.m1()
# t1.m2()
# t1.m3()         


#4. Declaring static variable
# class Test:
#     a =10 #static variable 
#     def __init__(self):
#          Test.b=20  # instance variable


#     def m1(self):
#          Test.c=30

#     @classmethod
#     def m2(cls):
#               Test.d=40
#               cls.e=50

#     @staticmethod
#     def m3():
#               Test.f=70

# print("a=",Test.a)
# t1=Test()
# print("b=", Test.b)
# t1.m1()
# print("c=", Test.c)
# Test.m2()
# print("d=", Test.d)
# print("e=", Test.e)
# t1.m3()
# print("f=", Test.f)                    


#3.
# class Test:
#     a =10 #static variable can change value save variable
#     def __init__(self):
#          self.b=20 # instance variable

# t1=Test()
# t2=Test()
# print("t1.a=", t1.a)
# print("t2.a=", t2.a)
# Test.a=100
# print("t1.a=", t1.a)
# print("t2.a=", t2.a)
# t2.b=40
# print("t1.a=", t1.a, "t1.b=", t1.b)
# print("t2.a=", t2.a, "t2.b=", t2.b)    
# t1.a=500 # it will not change static variable values it will create new instance variable for t1
# print("t1.a=", t1.a, "t1.b=", t1.b)
# print("t2.a=", t2.a, "t2.b=", t2.b)
# print("__________")
# print("inst var t1:",t1.__dict__)
# print("inst var t2:",t2.__dict__)



#2.
# class Test:
#     a =10
#     def __init__(self):
#         self.b=20 # instance variable


# t1=Test()
# t2=Test()
# print("t1.a=", t1.a)
# print("t2.a=", t2.a)
# Test.a=100
# print("t1.a=", t1.a)
# print("t2.a=", t2.a)
# t2.b=40
# print("t1.a=", t1.a, "t1.b=", t1.b)
# print("t2.a=", t2.a, "t2.b=", t2.b)





# class Test:
#     a = 10 #static variable
#     def __init__(self):
#         self.b=20 # instance variable

# print("a=", Test.a)
# t1=Test()
# print("a using t1:", t1.a)
# print("b=", t1.b)        
