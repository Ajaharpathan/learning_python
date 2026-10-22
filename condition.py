# state=input("enter state:")
# if state=="maharashtra":
#     print("capital: Mumbai")
# elif state=="gujrat":
#     print("capital:Gandhinagar")
# elif state=="uttar pradesh":
#     print("capital:lucknow")
# else:
#     print("invalid state")

# m1=int(input("enter first subjects"))
# m2=int(input("enter second subjects"))
# m3=int(input("enter third subjects"))
# m4=int(input("enter forth subjects"))
# m5=int(input("enter fifth subjects"))

# total= m1 + m2 + m3 + m4 + m5
# percentage= total / 500 * 100

# print("Total Marks:", total)
# print("Percentage is:", percentage,"%")

# if percentage >= 75:
#     print("class obtained:Distinction")
# elif percentage >= 60:
#     print("class obtained: First")
# elif percentage >= 50:
#     print("class obtained: Second")
# elif percentage >=40:
#     print("class obtained : pass")
# else:
#     print("fail")
# l1 = [10, 20, "python"]

# for x in l1:
#         print(x)


# str = "python"
# for x in str:
#         print(x)



# print("Positive Indexing:")
# for x in range(len(str)):
#     print(x, str[x])

# print("Negative Indexing:")
# for x in range(-len(str), 0):
#     print(x, str[x])


# str="python"
# i=0
# l=len(str)
# for x in str:
#     print(x,"positive index:",i, "negative index :", i-1)
#     i=i+1


# for i in range(0, 11):
#     print(i)


# for i in range(0, 21):
#   if i % 2 == 0: 
#      print(i)

# for i in range(10, 0, -1):
#     print(i)


# list =eval(input("enter list:"))
# sum=0
# for i in list:
#     sum = sum+i

# print("Sum of list:", sum)



#while loop
# i=0
# while i<10:
#    print("1 to 10:"i=i+1)


# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print( n * i)

# while True:
#     name = input("Enter your name: ")

#     if name == "Ajahar":
#         print("Your name is entered!")
#         break



n = 236
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print("Reverse number is:", rev)

# n=236, rev = 0
# d = n % 10
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
#     print("reverse =", rev)


# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("loop ended")    


# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")    


# i = 1
# while i  <= 10:
#     print(5*i)
#     i += 1


# n = 1
# while n <= 10:
#         print(3 * n)
#         n += 1

j = 1
while j <= 10:
        print(6 * j)
        j += 1     