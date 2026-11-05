





#ex 1 .decorators
# def decor2(wish):
#     def inner(name):
#         print("Second decorator")
#         wish(name)
#     return inner

# def decor1(wish):
#     def inner(name):
#         print("first decorator")
#         wish(name)
#     return inner   


# @decor1
# @decor2
# def wish(name):
#     print("hello" +name)

# wish("tom")    





# def decor(div):
#     def inner(n1, n2):
#         if n2==0:
#             print("number cannot be divided by 0")
#         else:
#             div(n1, n2)
#     return inner

# @decor 
# def div(n1, n2):
#     res=n1/n2 
#     print("result:", res)

# div(20, 10)
# div(20, 0)          


# def div(func):
#     def inner(a, b):
#         if b == 0:
#             print("Please select other number")
#         else:
#             return func(a, b)
#     return inner


# @div
# def division(a, b):
#     print("Division:", a / b)


# division(20, 5)
# division(10, 0)
    



#2. wthout annotation calling decorators

# def decor(wish):
#     def inner(name):
#         if name=="jill":
#             print("Not welcome")
#         else:
#             wish(name)
#     return inner

# def wish(name):
#     print("welcome"+name)

# # wish("anna")
# # wish("jill")           

# dfunction=decor(wish) 
#     




# def decor(wish):
#     def inner(name):
#         if name=="jill":
#             print("Not Welcomed jill")
#         else:
#             wish(name)
#     return inner

# @decor
# def wish(name):
#     print("welcome", name)

# wish("tom")
# wish("anna") 
# wish("jill")      
