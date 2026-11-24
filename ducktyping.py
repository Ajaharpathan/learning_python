
class Animal:
    def sound(self):
        print("Animal shouts")

class Birds:
    def sound(self):
        print("Birds sings") 

class Pets:
    def sound(self):
        print("Pets cry") 

def f1(obj):
    for  i  in obj:
         i.sound()
         print()


lobj=[Animal(), Birds(), Pets()]
f1(lobj) 



# f1(Animal())
# f1(Birds())
# f1(Pets())            


#1.  Using Retrive class

# class Animal:
#     def sound(self):
#         print("Animal shouts")

# class Birds:
#     def sound(self):
#         print("Birds sings") 

# class Pets:
#     def sound(self):
#         print("Pets cry") 

# class Retrieve:
#     def __init__(self, obj):
#         obj.sound()


# Retrieve(Animal())
# Retrieve(Birds())
# Retrieve(Pets())                            