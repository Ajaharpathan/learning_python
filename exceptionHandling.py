#print ("hello")

#6. Userdefined Exception 
class TooYoungExceptionError(Exception):
    def __init__(self, msg):
        self.msg=msg

age=int(input("Enter your age:")) 
if age<18:
    raise TooYoungExceptionError("Your age should be above 18:")
else:
    print("Registered successfully") 

print("End of application")    
            



#5. Finally Block and exit
# import os
# try:
#     n1=eval(input("Enter n1:"))
#     n2=eval(input("Enter n2:"))
#     n3=n1/n2
#     print("n3",n3) 
   
# except:
#     print("Something went wrong") 
#     #os._exit(1)
# else:
#     print("All is well")    

# finally:
#     print("Executed Finally block")

# print("End of application")           



#4. Single except block with multiple exception

# try:
#     n1=eval(input("Enter n1:"))
#     n2=eval(input("Enter n2:"))
#     n3=n1/n2
#     print(n3)

# except(ZeroDivisionError, TypeError) as msg:
#     print("Error occured", msg)

# except:
#     print(" Something went wrong")    





#3. Parent and child exception class
# try:
#     n1=eval(input("Enter n1:"))
#     n2=eval(input("Enter n2:"))
#     n3=n1/n2
#     print(n3)

# except ArithmeticError:
#     print("some arithmetic error")

# except ZeroDivisionError:
#     print("can't divided by zero ")

# except TypeError:
#     print("to divide a number it shoud be integer") 

# except:
#     print("Something went wrong")        




#2. try with multiple exception block
# try:
#     n1=eval(input("Enter n1:"))
#     n2=eval(input("Enter n2:"))
#     n3=n1/n2
#     print(n3)

# except ZeroDivisionError:
#     print("Number cannot be divided by zero ")

# except TypeError:
#     print("To divide number it should be an integer")

# except:
#     print("Something went wrong")




#1. Handling exceptions
 

# try: 
#     n1=eval(input("Enter n1:"))
#     n2=eval(input("Enter n2:"))
#     n3=n1/n2
#     print(n3)

# except:
#     print("Some error Occured")


# print("End of application")    