
#relational operators


#chaining 
# 10<20  true
# 10<20<30  true
# 10<20<30<40  true
# 10<20<30<40>50   false


# s1 = "python is easy"
# s2  = "python"
# print(s1>s2)


#for boolean behavior
# a,b = 10, 5
# c= not(a<b)
# print(c)

# a,b = 10, 5
# c=a<b and b<50
# print(c)

# a,b = 10, 5
# c=a<b or b<50
# print(c)

#for non-boolean behavior

# a="python"
# b=""
# c= a and b
# print(c)

# a=0
# b=5
# c= a or b
# print(c)

#bitwise operator & | ^ ~ << >>

# a = 10
# print(a<<2)
#print(a>>2)

# print(~4)
# print(~101)
# print(~false)

# a,b = 100, 20
# print("a is max") if a>b else print("b is max")

# a,b = 100, 30
# max=a if a>b else b
# print("max=", max)


# a = 19
# print("eligible for voting") if a>=b else print("not eligible")

# a  = 7
# print("Even Number") if a % 2 == 0 else print("Odd Number") 

# a,b,c = 15, 20, 100
# print("a is max") if a>b and a>c else (print ("b is max")if b>c else print("c is max"))

#1. identity operator IS and IS NOT address comparision
# n1=[10, 20, 30]
# n2=[10, 20, 30]
# n1=10
# n2=20
# print("id of n1", id(n1))
# print("id of n2", id(n2))
# print(n1 is n2)
# print(n1 is not n2)

#2. membership operator IN and NOT IN

l1=[10,30,"python"]
print("java" not in l1)


s1="python"
s2 = "0"
print("s2 is s1")
print("s2 not is s1")