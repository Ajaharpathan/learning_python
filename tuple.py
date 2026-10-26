#a. empty
# t1=()
# print(t1)
# print(type(t1))

# t1=(10, 20, "Python", 10)
# print(t1)
# print(type(t1))

#single values tuple
# t1=(10,)
# print(t1)
# print(type(t1))

# #b. intialise
# t1=10, 20, "python", 10
# print(t1)
# print(type(t1))

# #c. tuple()
# l1=[10, 20, 30, 40]
# print(l1)
# print(type(t1))
# t1=tuple(l1)
# print(t1)
# print(type(t1))

# #d. dynamic input
# data=eval(input("Enter list of data:"))
# print(data)
# print(type(data))

#2. accessing tuple
# t1=(10, 20, "python", "java", True)
# #t1=[1]=100
# print(t1)
# print(t1[-3])

# #3. Mathmatical op + *
# t1=(10, 20, 30)
# t2=(56, 78)
# print(t1+t2)
# print(t1*3)


#5.count()
# t1=(10, 20, 30, 10, 50, 10)
# print(t1.count(10))


# #4.sorted, len, max, min
# t1=(23, 45, 78, 90)
# print(max(t1))


# l1=sorted(t1, reverse=True)
# print(l1)
# print(t1)

#6. tuple packing and unpacking
# a,b,c = 10, 20, 30
# t1=a,b,c #packing
# print(t1)
# print(type(t1))

# x,y,z=t1 #unpacking
# print(x,y,z, sep=',')