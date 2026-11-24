
class SBI:
    def calculate(self):
        loan = int(input("Enter your loan"))
        years = int(input("Enter Number of Years"))
        rate = int(input("Enter rate of Interest"))

        interest = (loan * rate * years) / 100
        total = loan + interest

        print("SBI Bank")
        print("Loan Amount:", loan)
        print("Number of Years:", years)
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)
        print("----------------")

 
class HDFC:
    def calculate(self):
        loan = 500000
        years = 5
        rate = 9

        interest = (loan * rate * years) / 100
        total = loan + interest

        print("HDFC Bank")
        print("Loan Amount:", loan)
        print("Number of Years:", years)
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)
        print("----------------")


class Axis:
    def calculate(self):
        loan = 500000
        years = 5
        rate = 10

        interest = (loan * rate * years) / 100
        total = loan + interest

        print("Axis Bank")
        print("Loan Amount:", loan)
        print("Number of Years:", years)
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)
        print("----------------")


def Bank(obj):
    obj.calculate()


lobj = [SBI(), HDFC(), Axis()]

for obj in lobj:
    Bank(obj)
       