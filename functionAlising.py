#nested function
def outer():
    print("start of outer")
    def inner():
        print("I'm in inner function")
    print("End of outer function")
    return inner

inn=outer() #inn=inner
inn()    

 




# def outer():
#     print("start of outer")
#     def Inner():
#         print("I'm  in inner function")
#         Inner()
#         print("end of inner function")
# outer()  



#function alising

# def f1(name):
#     print("hello", name)


# f1("azhar")
# wish=f1 #function alising
# print("address of f1:", id(f1))
# print("address of wish:", id(wish))
# f1("anna")
# wish("jack")
