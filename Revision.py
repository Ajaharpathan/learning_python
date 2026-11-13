# l=[10, 20, 30]
# l.append("ajhar")
# print(l)
# l.remove(10)
# print(l)
# l.reverse()
# print(l)
# l.append(10)
# print(l)
# l.append(20)
# print(l)
# l.remove(20)
# print(l)

# print("hello world")
# a = 10
# b = 20
# print("Addition of two number is", a+b)
# print("Substraction is two number is", a-b)
# print("Multiplication of two number is:", a*b)
# print("Division of two number is:", a/b)

# a = int(input("Enter your number:"))
# if (a % 2 == 0):
#     print("Number is even ")
# else:
#     print("Number is odd")

# a = 50
# b = 20
# if a > b:
#     print("A is largest")
# else:
#     print("B is largest")    

# for i in range(1, 11):
#     print(i)    

# for a in range(11, 50):
#     print(a)   


# names = ["azhar", "javed","harun", "mosin"]

# for names in names:
#     print(names)

# print( )

# city= ["pune", "mumbai", "latur", "ausa"] 

# for city in city:
#     print(city)


# # for i in range(1, 11):
# #     print(5, "*", i, "=", 5 * i)

# for a in range(1, 11):
#     print(7, "*", a, "=", 7 * a)

# for b in range(1,11):
#     print(9, "*", b , "=", 9 * b)   

# num = 5
# fact = 1

# for i in range(1, num +1):
#     fact = fact * i

# print("Factorial =", fact)    



# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
#     else:
#         pass

# for i in range(10):
#     if i == 8:
#         break
#     print(i)    


#if statment
# age = int(input("Enter your age:"))
# if age>18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")    


#nested if
# age = 15
# owncar = 'true'

# if (age>=18):
#     print("you can drive car")
#     if (owncar == 'true'):
#         print("drive your car")
#     else:
#         print("first purchase your car")
# else:
#     print("You can't drive car")    

# a = float(input("Enter your First Number"))
# b = float(input("Enter your second Number"))

# c =a, b
# d = b
# print("Avg = ", (a+b)/2)

# a = int(input("Enter your first Number:"))
# b = int(input("Enter your second Number:"))

# if a>= b:
#     print('True')
# else:
#     print('False')   

# print(a>=b)    

# str = "hello my name is Ajahar. I'm from Osmanabad"
# print(str)

# first= "Ajahar"
# second = "Pathan"

# fullName = first + " " + second
# print(fullName)
# print(len(str))



#slicing
# print(str[: : -1])

# print(str.endswith("Osmanabad"))
# print(str.capitalize())
# print(str.upper())
# print(str.lower())
# print(str.replace("Osmanabad" ,"Dharashiv"))
# print(str.find("my"))
# print(str.count("name"))

# firstName = str(input("Enter your firstname:  "))
# print(len(firstName))

# name = "$azhar$pathan"
# print(name.count("$"))

# traffic = "Yellow"

# if (traffic == "Red"):
#     print("Stop")
# elif(traffic == "Green"):
#     print("Go")
# else:
#     print("Go Slow")        

# marks = 30

# if(marks>=90):
#     print("Grade A")
# elif(marks>=80):
#       print("Grade B")
# elif(marks>=70):
#       print("Grade c")    
# elif(marks>=50):
#       print("Grade D")

# else:
#      print("Fail")   
# 
#      
# practic question 1
# num = int(input("Enter your Number: "))

# if (num % 2 == 0):

#     print("Number is even")
# else:
#     print("Number is odd")    

# practice question 2

# num1 = int(input("Enter your Number: "))
# num2 = int(input("Enter your Number: "))
# num3 = int(input("Enter your Number: "))

# if(num1>num2 and num1>num3):
#     print("Number 1 is greater")
# elif(num2>num3 and num2>num1):
#     print("Number 2 is greter")    
# else:
#     print("Number 3 is greater")

# a = int(input("Enter your number: "))

# if(a % 7 == 0):
#     print("Number is multiple by 7")
# else:
#     print("Numbe is not multiple by 7")    

# marks = [23.5, 10, 5, 80, 56.6, 90.4]
# print(marks)

# mark = (23, 65, 67)
# print(mark)
# print(type(mark))
# print(type(marks))
# print(marks.append("ajahar"))
# print(marks.sort())
# print(marks.sort(reverse=True))
# print(marks.remove(5))
# print(marks.insert(0, "pathan"))
# print(marks.insert(3, "javed"))
# print(marks)

# tup = (2, 4, 6 , 7, 4, 8)
# print(tup)
# print(type(tup))
# print(tup.index(4))
# print(tup.count(4))

# mov =  []

# mov.append(input("Enter 1st movie:"))
# mov.append( input("Enter 2nd movie:"))
# mov.append(input("Enter 3rd movie:"))

# print(mov)

# list.append(mov1)
# list.append(mov2)
# list.append(mov3)

# print(list)
# print(type(list))

# list1 = [1, 2, 1]

# copy_list = list1.copy()
# copy_list.reverse()

# if(copy_list == list1):
#     print("Palindrone Number")
# else:
#     print("No palindrone")

# grade = ("D", "A", "A", "B", "B" ,"A")
# print(grade.count("A")) 

list1 = ["D", "A", "A", "B", "B" ,"A"]
list1.sort()
print(list1)
