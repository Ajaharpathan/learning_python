#lambda

#square of a number using lambda

# s=lambda x:x*x
# print("Square of number:", s(4))


# n=lambda n:n*(n+1)
# res=n(5)
# print("Sum of number:", n(5))


# s=lambda x,y:x+y
# print("addition :", s(10, 20))

# s=lambda a, b: s if a<b else b  
# print("Min =", s(20, 5))

#b. using lambda
# l1=[10, 9, 8, 13, 18, 20]
# res=list(filter(lambda x:x%2==0, l1))
# print(res)

#without lambda function
# def isEven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# l1=[10, 2, 5, 8, 18]
# res=list(filter(isEven, l1))
# print(res)    

# inp_list=['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']

# res=list(filter(lambda x:x!='t', inp_list))
# print(res)

# list1=[5, 10, 20, 30, 40, 'a', 'x', 50]
# list2=[10, 20, 'a']

# res=list(filter(lambda x: x not in list2, list1)) 

# print(res)


#map()
# def double(x):
#     return 2*x
# l1=[1, 2, 4, 3]

# res=list(map(double,l1))
# print(res)

#using lambda
# l1=[1, 2, 4, 3]
# res=list(map(lambda x:2*x, l1))
# print(res)

# l1=[1, 2, 4, 3]
# l2=[10, 20, 30, 40]

# res=list(map(lambda x,y:x*y, l1, l2))
# print(res)


#reduce()
# from functools import *
# l1=[10, 20, 30, 40]
# res=reduce(lambda x, y:x+y, l1)
# print(res)


#product of all numbers from 1 to 10
# from functools import *
# seq = range(1,11)
# res=reduce(lambda x, y: x * y, seq)
# print(res)





