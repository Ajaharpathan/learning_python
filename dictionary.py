#Dictionary -- Mutable

#write a program to take dictionary from the keyboard and print the sum of value?
# d=eval(input("Enter dictionary: "))
# s=sum(d.values())
# print("sum: ", s)

#write a program to find number of occurrences of each letter present in the given sring? IMP
# word=input("Enter any word:")
# word=input("Enter any word:")
# d={}
# for x in word:
#     d[x]=d.get(x,0)+1
#     for k,v in d.items():
#      print(k, "occured" ,v, "times")

#dictionary comprhension
# d={x:x*x for x in range(1, 6)}
# print(d)
# print(type(d))





#10. update
# d1={1:"python", 2:"java"}
# d2={3:"DA"}
# d1.update(d2)
# print(d1)


 #9. setdefault()
# d1={1:"python", 2:"java"}
# d2={3:"DA"}
# d1.update(d2)
# print(d1)

# d1={1:"python", 2:"java"}
# d1.setdefault(3,"DS")
# d1.setdefault(2,"DA")
# print(d1)

# d=[3]="data science"



#8. copy()
# d1={1:"python", 2:"java"}
# d2=d1
# #d2=d1.copy()
# print(d1)
# print(d2)
# d1[3]="DA"
# print(d1)
# print(d2)




#7. keys, values, items





#6. pop(k), popitem()
# d={1:"python", 2:"java", 'a':"apple"}
# x=d.popitem()
# print(x)

# x=d.pop(2)
# print(x)
# print(d)

# d={1:"python", 2:"java", 'a':"apple"}
# print(d.keys()):
# for k in d.keys():
#     print(k)



#5. get(key), get(key, default)
#d={1:"python", 2:"java", 'a':"apple"}
#x=d.get('a')
#x=d[5] //error
#x=d.get(5) 
#x=d.get(5, "guest")
#print(x)




#4.del key, clear
# d={1:"python", 2:"java", 'a':"apple"}
# print(len(d))
# d.clear()
# print(d)
# del d[2]
# del d
# print(d)

#3. update key
# d={1:"python", 2:"java", 'a':"apple"}
# d[1]="DS"
# print(d)
# d[3]="Net"
# print(d)





#2. accessing
# d={1:"python", 2:"java", 'a':"apple"}
# for k in d:
#     print(k)

# d={1:"python", 2:"java", 'a':"apple"}
# print(d[2])
# d[2]='DA'
# print(d)   

#a. empty dict
# d={}
# print(d)
# print(type(d))

#b. initialise
# d={1:"Python", 2:"java", 3:"Apple"}
# print(d)

# #c. dict()
# d=dict([(1, "python"), (2, "java"), (3, "da")])
# print(d)
# print(type(d))

#1. create dictionary
#e. 
# d={}
# print(d)
# d[1]="python"
# print(d)



#d. dynamic input
# d=eval(input("Enter data:"))
# print(d)
# print(type(d))
#

#write a program to enter name and percentage marks in a dictionay and display information on the screen

# d = {}
# a = {}
# p = {}

# d["name"] = input("Enter your name: ")
# d["percentage"] = float(input("Enter your percentage: "))

# a["name"] = input("Enter your name: ")
# a["percentage"] = float(input("Enter your percentage: "))

# p["name"] = input("Enter your name: ")
# p["percentage"] = float(input("Enter your percentage: "))

# print("Student Information:")
# print("Name:", d["name"])
# print("Percentage:", d["percentage"], "%")


# print("Name:", a["name"])
# print("Percentage:", a["percentage"], "%")

# print("Name:", p["name"])
# print("Percentage:", p["percentage"], "%")


# rec = {}
# n=int(input("Ente number of students:"))
# i=1
# while i <= n:
#     name=input("Enter Student Name:")
#     marks=input("Enter  % of marks of student:")
#     rec[name]=marks
#     i=i+1
#     print(rec)
#     print("name of student\t of marks" )
#     for x in rec:
#         print("\t",x, "\t\t", rec[x])

