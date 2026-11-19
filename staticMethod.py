class Outer:
    def __init__(self):
        print("Outer class constructor")


    class Inner:
        def __init__(self):
            print("Inner class constructor") 

        def m1(self):
            print("Inner class Instmethod m1") 

    def m2(self):
        print("Outer class instmethod m2")              



#outer().m2()
Outer().Inner().m1()

# o1=Outer()
# o1.m2()
# inn=o1.Inner()
# inn.m1()



# class Test:
#     def __init__(self):
#       self.y=100

#     def mthd(cls):
#        print(cls)


# Test.mthd("Hello") 

# t1=Test()
# t1.mthd()
    





#static Method

# class Test:
#     x=200
#     def __init__(self):
#         self.u=100


#     @staticmethod
#     def stsmthd(a,b):
#         print("addition:", a+b)


# t1=Test()
# t1.stsmthd(10, 20)
# Test.stsmthd(40, 40)            