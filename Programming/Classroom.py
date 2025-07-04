class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"Hello! My name is {self.firstname} {self.lastname}.")

class Student(Person):
    def __init__(self, firstname, lastname, grade):
        super().__init__(firstname, lastname)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print("Current grade:", self.grade)

class Teacher(Person):
    studentlist = []

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def assign_students(self):
        while True:
            name = input("Enter a student name (or '-' to stop): ")
            if name == "-":
                break
            self.studentlist.append(name)
        print(self.studentlist)

    def introduce(self):
        super().introduce()
        print("Students:", ", ".join(self.studentlist))

p = Person("John", "Smith")
p.introduce()

s = Student("Alice", "Johnson", "A")
s.introduce()

t = Teacher("Mr.", "Anderson")
t.studentlist = ["Tom", "Jerry"]
t.introduce()
t.assign_students()