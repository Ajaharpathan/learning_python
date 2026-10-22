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

s="  "
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.istitle())
print(s.isspace())


s="python is easy to learn"
print(s.startswith('Py'))
print(s.endswith('n'))
