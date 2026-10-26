#4. Relational  + *
# l1=[10, 20, 30]
# l2=[40, 50]
# print(l1+l2)
# print(l1*3)

#5. Relational op
# l1=["python", "java", "c++", "java"]
# l2=["python", "da"]
# print(l1<l2)

#6. Special op
# l1=["python", "java", "c++", "java"]
# print("python" not in l1) #Membership Op

# l1=[10, 20, 30]
# l2=[10, 20,30]
# print(l1==l2)
# print(l1 is l2) #Identity Operator

#7. Nested list
# l1=[10, 20, ["python", "java"]]
# print(l1[2][1])

#List comprehension
#a.
# l1=[x for x in range(1, 11)]
# print(l1)

#even numbers
# l1=[x for x in range(1, 11) if x % 2==0]
# print(l1)

#square of list
# l1=[1, 2, 3, 4]
# l1=[x*x for x in l1]
# print(l1)

# l1 = [10, 20, 30, 40]
# l2 = [30, 40, 50, 60]
# num3=


s = "The quick brown fox jumps over a lazy dog"
s2=s.split()
print(s2)
l1=[ [x, len(x)] for x in s2]
print(l1)