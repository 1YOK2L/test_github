import random

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduce(self):
        print(f"Hello! My name is {self.firstname} {self.lastname}.")

class Student(Person):
    def __init__(self, firstname, lastname, grade=None):
        super().__init__(firstname, lastname)
        self.grade = grade
        self.score = None

    def introduce(self):
        super().introduce()
        print("Current grade:", self.grade)
        if self.score is not None:
            print("Test score:", self.score)
            print("Grade:", self.get_grade())

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

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
        print("Student list:", self.studentlist)

    def random_score(self):
        for student in self.studentlist:
            score = random.randint(0, 100)
            student.score = score
            print(f"{student.firstname} {student.lastname} got a score of {score}.")

    def list_test_grade(self):
        print("\nTest grades:")
        for student in self.studentlist:
            print(f"{student.firstname} {student.lastname} ({student.score}): {student.get_grade()}")

    def class_room_grade_summary(self):
        grade_summary = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

        for student in self.studentlist:
            grade = student.get_grade()
            grade_summary[grade] += 1

        print("\nClassroom grade summary:")
        for grade, count in grade_summary.items():
            print(f"{grade}: {count}")

p = Person("John", "Smith")
p.introduce()

s1 = Student("Alice", "Johnson")
s2 = Student("Bob", "Miller")

s1.introduce()
s2.introduce()

t = Teacher("Mr.", "Anderson")
t.assign_students()

t.random_score()

t.list_test_grade()

t.class_room_grade_summary()