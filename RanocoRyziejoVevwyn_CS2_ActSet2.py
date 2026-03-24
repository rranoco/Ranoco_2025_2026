students = []

for i in range(3):
    Name = input("Enter Name: ")
    Age = input("Enter Age: ")
    Grade = input("Enter Grade: ")

    student_dictionary = {
   "name" : Name,
   "age" : Age,
   "grade" : Grade
    }

    students.append(student_dictionary)

print("\nClass Directory:\n")

for student in students:

    print("Name:", student["name"], "│ Age:", student["age"], "│ Grade:", student["grade"])
