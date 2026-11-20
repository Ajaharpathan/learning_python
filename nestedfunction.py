class Test:
    def m1(self):
        def calc(n1, n2):
            print("addition:", n1+n2)
            print("substraction:",n1-n2)
            print("multiplication:", n1*n2)
            print("************")

        calc(10, 20)
        calc(2, 3)    
        calc(20, 10)
        return calc


t1=Test()
# t1.m1()  
x = t1.m1()      