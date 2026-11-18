#Instance variable
#4. delete instance
class Test:
    def __int__(self):
        self.a=10

    def m1(self):
        del self.a


t1=Test()
t2=Test()
print("inst var t1:", t1.__dict__)
print("inst var t2:", t2.__dict__)
#t1.m1()
print("inist var t1:", t1.__dict__)
# print("inst var t2:", t2.__dict__)


#3. Updates instrance variable
# class Test:
#     def __int__(self):
#         self.a=10

#     def m1(self):
#         self.a=100

# t1=Test()
# t2=Test()
# print("inst var t1:", t1.__dict__) 
# print("ins var t2:", t2.__dict__)

# t1.m1()
# t2.m1()

# print("inst var t1:", t1.__dict__)
# print("inst var t2:", t2.__dict__)
# t2.a=5555
# print("inst var t1:", t1.__dict__)
# print("ins var t2:", t2.__dict__)


#2. Accessing instance variable

# class Test:
#     def __int__(self):
#         self.a=10
#         print("a in constrctor:", self.a)
#     def m1(self):
#         print("a in method:", self.a)


# t1=Test()
# t1.m1()
# print("A outside class: ", t1.a),            



#1. Declaring instance variable

#b. outside the class using reference variable

# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#         self.b=20 


#     def add(self):
#         print("sum", self.a+self.b) 

# t1=Test()
# t1.m1()
# print("t1 inst var:", t1.__dict__)
# t1.add()
# print("___")        
# t2=Test()
# t2.m1()
# print("t2 inst var:", t2.__dict__)
# t1.c=100 # declaring with t1

# print("t1 inst var:", t1.__dict__)
# print("t2 inst var:", t2.__dict__)

# t2.y=200 # declaring with t2
# print("t1 inst var:", t1.__dict__)
# print("t2 inst var:", t2.__dict__)




#a, inside constructor and inside instance method

# class Test:
#     def __init__(self):
#         self.a=10

#     def m1(self):
#         self.b=20 


#     def add(self):
#         print("sum", self.a+self.b) 

# t1=Test()
# print("inst var:", t1.__dict__)
# t1.m1()
# print("inst var:", t1.__dict__)
# t1.add()

# print("___________")

# t2=Test()
# print("inst var:", t2.__dict__)
# t2.m1()
# print("inst var:", t2.__dict__)
# t2.add()