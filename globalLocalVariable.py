#.global and local variable

#4.both accessing local and global
a=100 #global
def f1():
    a=10
    print(a)
    print("global a=", globals()['a'])

f1()






#3. declaring global variable in function

# def f1():
#     global a
#     a=100
#     print(a)

# def f2():
#     print(a)    


# f1()
# f2()    

#2. local var preference than global 
a=100 #global
def f1():
    a=10  #local variable
    print(a)

f1()    






#1.global
# a=10
# def f1():
#     # a=10  local 
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()        