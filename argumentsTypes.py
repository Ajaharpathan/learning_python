#Types of Arguments
#5.keyword variable length argument
def show(**kwargs):
    print(kwargs)

show(name="azhar")
show(age=23)
show(sal=7989899)
show(add="Osmanambad")
show(course="Python Fullstack")



#4. variable lenght arguments
# def summ(*n, name):
#     total = 0
#     for x in n:
#         total+=x
#         print("name:",name)
#         print("total:", total)

# summ(10, 20, 30, name="azhar")        






# def sum(*n):
#     total = 0
#     for i in n:
#         total = total + i
#     print(total)

# sum()
# sum(10)
# sum(10, 20)
# sum(10, 20, 30)    



#3. default argument
# def person(name="pathan", age=23):
#     print(f"{name} is of age {age} years old.")

# person("azhar", 20)
#person()    dafault arguments

#2 keyword arguments

# def person(name, age, sal):
#     print(f"my {name} is of age {age} years old and earning sal of {sal}.")

# person("ajahar", sal=20000, age=23) 


#1.positinal argument

# def person(name, age):
#     print(f "my {name} is of age {age} years old.")

# person("Azhar", 23)