students = []
help = []
while (name := input("Enter student or 'q' to quit: ").strip()) != 'q':
    Math = input("Math score : ")
    Science = input("Science score : ")
    if Math.isnumeric() and Science.isnumeric():
        Math = int(Math)
        Science = int(Science)
        x = {"name": name, "math": Math, "science": Science}
        students.append(x)
        if Math < 60 or Science < 60:
            help.append(name)
    else:
        print("Incorrect input")
        continue
print("\nStudent Averages:")
for student in students:
    average = (student["math"] + student["science"])*0.5
    if average % 1 == 0:
        print(student["name"], ":", "%d" % average)
    else:
        print(student["name"], ":", "%.1f" % average)
if students:
    mathmax = max(students, key=lambda x: x["math"])["math"]
    scimax = max(students, key=lambda x: x["science"])["science"]

    top_math_students = [s["name"] for s in students if s["math"] == mathmax]
    top_science_students = [s["name"] for s in students if s["science"] == scimax]

    print("\nTop performer in Math :", " ".join(top_math_students))
    print("Top performer in Science :", " ".join(top_science_students))
else:
    print("\nNo student data entered.")
print("\nStudents need help:", "[" + ", ".join(help) + "]")