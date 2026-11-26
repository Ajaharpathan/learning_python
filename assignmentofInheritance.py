class Bank:
    def __init__(self):
        self.loan = 500000
        self.years = 5

    def display(self):
        print("Loan Amount:", self.loan)
        print("Number of Years:", self.years)


class SBI(Bank):
    def calculate(self):
        rate = 8
        interest = (self.loan * rate * self.years) / 100
        total = self.loan + interest

        print("_________")
        print("SBI Bank")
        self.display()
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)


class HDFC(Bank):
    def calculate(self):
        rate = 9
        interest = (self.loan * rate * self.years) / 100
        total = self.loan + interest

        print("_______")
        print("HDFC Bank")
        self.display()
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)


class Axis(Bank):
    def calculate(self):
        rate = 10
        interest = (self.loan * rate * self.years) / 100
        total = self.loan + interest

        print("________")
        print("Axis Bank")
        self.display()
        print("Rate of Interest:", rate, "%")
        print("Interest:", interest)
        print("Total Amount:", total)


s = SBI()
h = HDFC()
a = Axis()

s.calculate()
h.calculate()
a.calculate()