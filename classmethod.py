class Test:
    def __init__(self):
        self.a=10



    def m1(self):
        print("self", self)
        print("a=", self.a)
        print("_________")



    @classmethod
    def clsmetd(cls):
        print("cls:", cls)
        Test.x=100
        cls.y=200

Test.clsmetd()
t1=Test()
t1.m1() 
t1.clsmetd()               