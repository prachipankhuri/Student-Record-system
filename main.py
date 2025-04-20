from student import Student

def add_student():
    print("\n[Add Student]")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    grade = input("Enter Grade: ")

    student = Student(roll, name, marks, grade)

    with open("records.txt", "a") as f:
        f.write(student.to_line())

    print("Student added successfully!")

def view_students():
    print("\n[All Students]")
    try:
        with open("records.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No records found.")
            else:
                for line in lines:
                    student = Student.from_line(line)
                    print(f"Roll: {student.roll}, Name: {student.name}, Marks: {student.marks}, Grade: {student.grade}")
    except FileNotFoundError:
        print("No records file found.")

def search_student():
    print("\n[Search Student]")
    roll = input("Enter Roll Number to search: ")
    found = False

    try:
        with open("records.txt", "r") as f:
            for line in f:
                student = Student.from_line(line)
                if student.roll == roll:
                    print(f"Found: Roll: {student.roll}, Name: {student.name}, Marks: {student.marks}, Grade: {student.grade}")
                    found = True
                    break
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No records file found.")

def update_student():
    print("\n[Update Student]")
    roll = input("Enter Roll Number to update: ")
    updated = False
    new_data = []

    try:
        with open("records.txt", "r") as f:
            for line in f:
                student = Student.from_line(line)
                if student.roll == roll:
                    print("Enter new details:")
                    student.name = input("New Name: ")
                    student.marks = input("New Marks: ")
                    student.grade = input("New Grade: ")
                    updated = True
                new_data.append(student.to_line())

        if updated:
            with open("records.txt", "w") as f:
                f.writelines(new_data)
            print("Student updated successfully!")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("No records file found.")

def delete_student():
    print("\n[Delete Student]")
    roll = input("Enter Roll Number to delete: ")
    deleted = False
    new_data = []

    try:
        with open("records.txt", "r") as f:
            for line in f:
                student = Student.from_line(line)
                if student.roll != roll:
                    new_data.append(student.to_line())
                else:
                    deleted = True

        if deleted:
            with open("records.txt", "w") as f:
                f.writelines(new_data)
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("No records file found.")

def main_menu():
    while True:
        print("\n===== Student Record System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
