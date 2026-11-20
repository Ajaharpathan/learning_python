class Person():
    def __init__(self, name, dd,mm, yyyy):
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)

        def display(self):
            print("Hai:", self.name)
            self.dob.dob()


        class Dob():
            def __init__(self, dd, mm, yyyy):
                self.dd=dd
                self.mm=mm
                self.yyyy=yyyy

            def dob(self):
                print("Your birth day is on {}/{}/{}".format(self.dd,self.mm,self.yyyy))

p=Person("ajahar", 25, "may", 2003)
p.display()        