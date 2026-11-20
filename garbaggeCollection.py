import gc

#5.List of objects
class Test:
    def __init__(self,name):
        print("Objects initialized")
        self.name=name

    def __del__(self):
        print("Performing clean up activities")

    def m1(self):
        print("Name=",self.name)
        print()


t=[Test("Tom"),Test("Jack"),Test("Jill")]
for obj in t:
    obj.m1()


#4.count reference variable

# import sys
# class Test:
#     def __init__(self):
#         print("Objects initialized")
#
#     def __del__(self):
#         print("Performing clean up activities")
#
# t1=Test()
# t2=t1
# t3=t2
# print("Reference variable count:",sys.getrefcount(t1))
# del t2
# print("Reference variable count:",sys.getrefcount(t1))

#3.

# import time
# class Test:
#     def __init__(self):
#         print("Objects initialized")
#
#     def __del__(self):
#         print("Performing clean up activities")
#
#
# t1=Test()
# t1=None
# print(t1)

# del t1
# print(t1)

        

#2.
#import time
# class Test:
#     def __init__(self):
#         print("Ojbects Initiailzed")

#     def __del__(self):
#         print("Peforming clean up activities")

# t1=Test()
# t2=t1
# t3=t2
# print("3 objects created")
# del t1
# time.sleep(3)
# print("ojbect not destroyed")
# del t2
# time.sleep(3)
# print("Object not destroyed")
# del t3
# time.sleep(3)
# print("object destroyed")
# print("End of application")





#1.
# import time

# class Test:
#     def __init__(self):
#         print("Ojbects Initiailzed")

#     def __del__(self):
#         print("Peforming clean up activities")



# t1=Test()
# t2=Test()
# time.sleep(5)
# print("work done with t1")
# time.sleep(2)
# t1=None
# time.sleep(5)
# t2=None
# print("end of Statement")



#print(gc.isenabled())
#gc.disable()
#print(gc.isenabled())
# gc.enable()
# print((gc.isenabled))