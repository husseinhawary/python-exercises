# property decorator
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def display(self):
        return self.name + " got grade " + self.grade

    @staticmethod
    def hello():
        print("Hello Hussein")


stu = Student("Hussein", "95")
print(stu.name)
print(stu.grade)
print(stu.display)
Student.hello()
stu.hello()
