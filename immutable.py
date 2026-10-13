#immutable

'''
n1= 10
n2 = 20
print("n1=", n1)
print("address of n1", id(n1))
print("n2=", n2)
print("address of n2", id(n2))

n3= 10
print("n3=", n3)
print("address of n3", id(n3))
print("*******************")

n4=40
print("n4=", n4)
print("address of n4", id(n4))
'''


'''
s1="python"
s2 = "python"
print("s1=", s1)
print("address of s1", id(s1))
print("s2=", s2)
print("address of s2", id(s2))
'''
'''
f1= 10.23
f2 = 10.23
print("f1=", f1)
print("address of f1", id(f1))
print("f2=", f2)
print("address of f2", id(f2))
'''

'''
x=[10, 20, 30]
print(x)
print("datatypes=", type(x))
b=bytes(x)
print("b=", b)
print("datatype=", type(b))
#print(b[1])
#b[1]=100
'''


'''
x1=[10, 20, "python", 2.5]
x2=[10, 20, "python", 2.5]
print("x1"=x1)
print("datatypes=", type(x1))
'''
'''
x=[10, 20, 30]
print(x)
print("datatypes=", type(x))
ba=bytearray(x)
print("ba", ba)
print("dataypes=", type(ba))
ba[1]= 100
print(ba[1])
'''
'''
#list
l1=[]
print("l1", 11)
print("datatypes of l1", type(l1))
'''

'''
l1=[10, 20, "pthon", True, 20, "Python", "java", "da"]
#print("l1 =", l1)
#print("datatype of l1", type(l1))
#print(l1[3])
print(l1[-4])
print(l1[10])
#print(l1[:10])
#print(l1[2:10:-1])
#print(l1[-6:-2:-1])
#print(l1)
'''

#tuple --- immutable
t=10,
print(t)
print(type (t))

'''
t=10,20,"python", True
print(t)
print(type(t))
print(t[2])
print(t[:4])
#t[0]=100
'''

'''
t=()
print(t)
print(type (t))
'''


'''
#range

#c.r1=range(0, 20, 2)
print(type(r1))
for x in r1:
    print(x)
'''

'''    
#b.range (n1, n2)
r1=range(10, 20)
print(type(r1))
for x in r1:
    print(x)
'''


#c.range(x)
r1=range(20)
print(r1)
print(type(r1))
for x in r1:
    print(x)
    












