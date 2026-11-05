#generator
 #userdefined generator

def countdown(num):
    print("start countdown")
    while(num>0):
        yield num
        num=num-1

values=countdown(5)
for x in values:
    print(x)


# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'

# g=mygen()
# print(g)
# print(type(g))
# print(next(g))    
# print(next(g))
# print(next(g))








# l1=(i*i for i in range(1, 100000))
# print(l1)
# print(type(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))

# l1=(i*i for i in range(1, 10000))
# print(l1)
# print(type(l1))
# for i in l1:
#     print(i)



#3. chaining of decorator


#ex. 2 decorator

# def decor1(num):
#     def inner():
#         n=num()
#         return n*n
#     return inner

# def decor2(num):
#     def inner():
#         n=num()
#         return n+n
#     return inner


# @decor1
# @decor1
# def num():
#     return 10

# print(num())