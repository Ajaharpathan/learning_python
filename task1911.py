# Display number of objects
class Test:
    count = 0

    def __init__(self):
       
        Test.count += 1

    @classmethod
    def countobj(cls):
        print("no of object", Test.count)    

   


t1=Test()
t2=Test()
Test.countobj()
t3=Test()
t4=Test()
Test.countobj()