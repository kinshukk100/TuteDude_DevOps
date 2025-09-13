student_grades = {}

def add_student(name, grade):
    if name in student_grades:
        print(f"{name} already exists with grade {student_grades[name]}.")
    else:
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}.")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found.")

def print_all_students():
    if not student_grades:
        print("No student records available.")
    else:
        print("\nStudent Grades:\n")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}\n")

while True:
    print("\nOptions:")
    print("1 : Add student")
    print("2 : Update student grade")
    print("3 : Print all student grades")
    print("4 : Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student name to update: ")
        grade = input("Enter new grade: ")
        update_student(name, grade)
    elif choice == '3':
        print_all_students()
    elif choice == '4':
        print("Exit.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
