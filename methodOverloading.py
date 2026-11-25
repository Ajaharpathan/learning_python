#2. using variable length argument
class Test:
    def summ(self, *n):
      print(n)
      total = 0
      for x  in n:
         total+=x
      print("sum=", total)   





t1=Test()
t1.summ()
t1.summ(10, 20)
t1.summ(10, 20, 30)






#1. Method overloading using default arguments


# class Test:
#     def summ(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             res = a+b+c 
#             print("Addition:", res)

#         elif a!=None and b!=None:
#             res=a+b
#             print("Addition ", res)

#         else:
#             print("Please provide atleat 2 numbers")

# t1=Test()
# t1.summ(10, 20, 30)
# t1.summ(10, 20)
# t1.summ("Python", "java")                    