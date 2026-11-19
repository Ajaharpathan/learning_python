
class Student:

    def __init__(self, rno, name, marks1, marks2, marks3, marks4, marks5):
        self.rno = rno
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4
        self.marks5 = marks5
        

    def markstotal(self):
        total = self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5
        return total

    def percentage(self):
        percentage = self.markstotal() / 5
        return percentage

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B "
        elif percentage >= 60:
            return "C "
        elif percentage >= 40:
            return "D "
        else:
            return "Fail"

    def show(self):
        print("Student Rno:", self.rno)
        print("Student Name:", self.name)
        print("Total Marks:", self.markstotal())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


s1 = Student( 101, "Azhar", 45, 40, 30, 40, 59)


s1.show()
