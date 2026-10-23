# n=int(input("enter a number:"))
# flag = 0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break

# if flag==1:
#     print("Not prime number")
# else:
#     print("prime number")


# cart=[10, 20, 100, 70, 80]
# for item in cart:
#     if item >500:
#         print("you cannot process further")
#         break
#     print(item)
# else:
#     print("all items processed successfully")


# print("end")

#comparison op 
# s1 = "python"
# s2 = "python is easy"
# print(s1<s2)


# #2.membership op in not in
 
# s1="python is easy"
# print("python" not in s1)


# #1. mathmatical op + *

# s1 = "python"
# s2="java"
# print(s1+s2)
# print(s1*3)

# state1=input("enter state:")
# state=state1.strip()


# if state=="maharashtra":
#     print("capital: Mumbai")
# elif state=="Gujrat":
#     print("capital:gandhi nagar")  
# elif state=="uttarpradesh":
#     print("capital:lucknow")   
# else:
#     print("invalid state")       



#5.find(),index(), rfind(), rindex()
# s="python is easy"
# x=s.index("z")
# print(x)

# x=s.find("s", 9, 14)
# print(x)

# x=s.rfind("y")
# print(x)

# x=s.find("y")
# x=s.find("eas")
# x=s.find("java")
# print(x)

# s="abaabbbaabbabbab"
# for i in range(len(s)):
#     if s[i] == "a":
#         print(i)

# s="abaabbbaabbabbab"
# p=-1
# n=len(s)
# while True:

# s = "abaabbbaabbabbab"

# i = 0

# while i < len(s):
#     if s[i] == "b":
#         print(i)
#     i += 1


# s=input("enter main string:")
# subs= input("enter sub string:")

# p=-1
# n=len(s)
# while true:
#     p=s.find(sub,p+1,n)
#     if p==1:
#         break
#     print("found at position", p)

# s='Ramesh works in fortune cloud Technology'
# subs=int(input("enter sub  string:  "))
# p=-1
# while True:
#     p= s.find(subs, p +1,n)

#     if p == -1:
#         break 
#     print("found at index", p)
        
#6.count()

# s="python is easy to learn"

# x=s.count('a')
# print(x)


#7. Replace()
# s1="python is easy to use"
# s1=s1.replace("python", "java")
# print(s1)


# s = "learing python is very difficult"
# s1 = s.replace("difficult", "easy")
# print(s1)


# s = "ababbabbaababab"
# s1=s.replace("a", "b")
# print(s1)


#8. split()

# s="22-10-2026"
# l1=s.split("-")
# print(l1)


# s="python is easy to learn"
# l1=s.split()
# print(l1)

#9. join()

# l1="python", "is", "easy"
# s1="".join(l1)
# print(s1)

#10. changing casese upper, lower, swapcase, title, capitalize

# s1="python IS eASy"
# #s2=s1.upper()
# #s2=s1.lower()
# #s2=s1.title()
# #s2=s1.swapcase()
# s2=s1.capitalize()
# print(s2)

#11. startswith()   endswith()

# s="  "
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.istitle())
# print(s.isspace())


# s="python is easy to learn"
# print(s.startswith('Py'))
# print(s.endswith('n'))
# print(s.startswith('python'))




# n="Python is easy for learning"
# s1=n.replace("Python", "c++")
# print(s1)

# l1="python", "is", "easy", "learn"
# s1="".join(l1)
# print(s1)



#  LIST --MUTABLE
#create list
#a. empty list
# l1=[]
# print(l1)
# print(type(l1))

#b. Initialize

# l1=[10, 20, "python", 10]
# print(l1)
# print(type(l1))

# #dynamic input
# l1=eval(input("enter list of data:"))
# print(l1)
# print(type(l1))

# #d. list()
# t=(10, 20, 30)
# print(t)
# print(type(t))
# l1=list(t)
# print(l1)
# print(type(l1))

# #e. split()
# s="python is easy"
# l1=s.split()
# print(l1)

# l1=[10, 20, 30, 40, 50]
# #traversing(for or while)
# for i in l1:
#     print(i)

# i = 0
# while i < len(l1):
#     print(l1[i])
#     i += 1    

#a.count()
# l1=[10, 20, 30, 40, 50, 60, 10, 20, 40]
# print(l1.count(10))

# #b.index()
# l1=[10, 20, 30, 40, 50, 60, 10, 20, 40]
# print(l1.index(20))
# print(l1.index(60))

#c.append()
# l1=[10, 20, 30, 40, 50, 60, 10, 20, 40]
# l1.append(80, 90)
# print(l1)


#d.insert()
# l1=[10, 20, 30, 40, 50, 60, 10, 20, 40]
# l1.insert(2, 100)
# l1.insert(-3, 100)
# print(l1)

#e. extend()
# l1=[10, 20, 30, 40,]
# l2=[50, 60]
# l2=4, 5, 6
# l2="java"
# l1.extend(l2)
# print(l1)


# l1=[10, 20, 30]
# l2=[40, 50]

# l1.extend(l2)
# print(l1)

# l1.append(l2)
# print(l1)


# #create a list even number and it divisible by 7
# l1=[]
# for x in range(101):
#     if x%2==0 and x%7==0:
#         l1.append(x)
# print(l1)        

# l1=[]
# for x in range(0,100,2):
#     if x%7==0:
#         l1.append(x)
# print(l1)        

#f. remove(), pop(), pop(index), clear()
# l1=[10, 20, 30, 40, 10, 50, 60]
# #l1.remove(10)
# # l1.remove(55) #value error
# #l1.pop() #
# l1.pop(2) #position index pop only 
# #l1.clear() data delete but list still exist
# #del l1 all the data delete
# print(l1)

# l1=[10, 5, 40, 30, 25]
#l1.reverse()
# l1.sort()
#l1.sort(reverse=True)
# print(l1)

#cloning (using slicing and copy)
# l1=[10, 20, 30]
# l2=l1[:]
# l2=l1.copy()
# print(l1)
# print(l2)
# print("l1 address:", id(l1))
# print("l2 address:", id(l2))
# l1[2]=100
# print(l1)
# print(l2)

#aliasing (=)
l1=[10, 20, 30]
l2=l1
print(l1)
print(l2)
print("l2 address:", id(l2))
print("l2 address:", id(l2))
