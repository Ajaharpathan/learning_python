# def factorial(x):
#     if x == 1 or x==0:
#         f=1
#     else:
#         f=x*factorial(x-1)
#     return f



# n=int(input("Enter a number:"))
# res=factorial(n)

# print(f"factorial of{n} is {res}")


#sum of 1 to 5 numbers


# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)

# result = sum(5)
# print(result)

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)

# res = sum(5)
# print(res)    



def summ(x):
    if x==5:
        s=5
    else:
        s=x+summ(x+1)
    return s    
summ(6)