#set Datatype -- mutuable

#1.Dynamic set
#d. dynamic input

# s1=eval(input("Enter set values:"))
# print(s1)
# print(type(s1))


#c. set()
# l1=[10, 20, 30, "python"]
# s=set[l1]
# print(s)
# print(type(s))

# #b. initialise
# s={10, 20, 30, 10, "python", True}
# print(s)
# print(type(s))
# print(s[2])


#a. empty set
# s=set()
# print(s)
# print(type(s))

#add, update 27/10
# l1=[10, 20]
# s={"python", "java"}
# s.update(l1,"DA")
# print(s)

# s1={10, 20, "Python", "java"}
# s1.add(True)
# print(s1) 

#2. built in functions pop(), remove(), discard(), clear()

# s1={10, 20, "python", "java"}
#s1.remove(20)
#s1.discard("pyt")
#s1.clear()
# s1.pop()
# print(s1)

# s1={10, 20, 30}
# #s2=s1 
# s2=s1.copy() #cloning
# print(s1)
# print(s2)
# s1.add(100)
# print(s1)
# print(s2)

#mathmatical 

#a. union
#s1={10, 20, 30, 40, 50}
#s2={40, 50, 80}
#s3=s1.union(s2)
#s3=s1|s2
#print(s3)

#b. intersectin
#s1={10, 20, 30, 40, 50}
#s2={40, 50, 80}
#s3=s1.intersection(s2)
#s3=s1&s2
#print(s3)

#c. difference
#s1={10, 20, 30, 40, 50}
#s2={40, 50, 80}
#s3=s1.difference(s2)
#s3=s1-s1
#print(s3)

#d. symmetric difference
# s1={10, 20, 30, 40, 50}
# s2={40, 50, 80}
# s3=s1.symmetric_difference(s2)
# print(s3)

#e. intersection_update, difference_update
# s1={10, 20, 30, 40, 50}
# s2={40, 50, 80}
# s1.intersection_update(s2)
# s1.difference_update(s2)
# s1.symmetric_difference_update(s2)
# print(s1)

#f. issubset(), issuperset()
# s1={10, 20, 30}
# s2={40, 10, 50, 20, 30}

# print(s1.issubset(s2))
# print(s2.issuperset(s1))

#g. isdisjoint()
# s1={10, 20, 30, 40}
# s2={79, 80}
# print(s1.isdisjoint(s2))

#4. set comprhension

#create a set of sqaure of even numbers from 1 to 20
s={x**2 for x in range(1, 21) if x % 2 == 0}
print(s)
print(type(s))


s={ x*x for x in range(1,11)}
print(s)
print(type(s))

#create a set of unique vowels of a given 