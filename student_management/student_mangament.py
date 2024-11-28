import json

# Define the Students class
class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def display(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects
        }

# Add a new student
def add_student(list_students):
    id = int(input("Enter your ID: \n"))
    name = input("Enter your name: \n")
    age = int(input("Enter your age: \n"))
    grade = input("Enter your grade: \n")
    subjects = input("Enter your subjects (comma-separated): \n").split(',')

    # Create an instance of the Students class
    student = Student(id, name, age, grade, [subject.strip() for subject in subjects])
    list_students.append(student)
    print("Student added successfully!\n")

# Update a student
def update_student(list_students):
    student_id = int(input("Enter the ID of the student to update: \n"))
    for student in list_students:
        if student.id == student_id:
            print("What would you like to update?")
            print("1. Name\n2. Age\n3. Grade\n4. Subjects\n")
            option = int(input("Enter your option: "))

            if option == 1:
                student.name = input("Enter the new name: \n")
            elif option == 2:
                student.age = int(input("Enter the new age: \n"))
            elif option == 3:
                student.grade = input("Enter the new grade: \n")
            elif option == 4:
                student.subjects = input("Enter the new subjects (comma-separated): \n").split(',')
            else:
                print("Invalid option.\n")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")

# Delete a student
def delete_student(list_students):
    student_id = int(input("Enter the ID of the student to delete: \n"))
    for student in list_students:
        if student.id == student_id:
            list_students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")

# View all students
def view_student(list_students):
    if not list_students:
        print("No students available.\n")
        return

    for student in list_students:
        student_data = student.display()
        print(f"ID: {student_data['id']}, Name: {student_data['name']}, Age: {student_data['age']}, "
              f"Grade: {student_data['grade']}, Subjects: {', '.join(student_data['subjects'])}\n")

# Save students to a file
def save_students_to_file(list_students, filename="students.json"):
    with open(filename, "w") as file:
        data = [student.display() for student in list_students]
        json.dump(data, file, indent=4)
    print(f"Students saved to {filename}\n")

# Load students from a file
def load_students_from_file(filename="students.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Student(**item) for item in data]
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.\n")
        return []

# Main program
if __name__ == "__main__":
    list_students = load_students_from_file()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Update a student")
        print("4. Delete a student")
        print("5. Save and exit")
        user_input = int(input("Enter your option: "))

        if user_input == 1:
            add_student(list_students)
        elif user_input == 2:
            view_student(list_students)
        elif user_input == 3:
            update_student(list_students)
        elif user_input == 4:
            delete_student(list_students)
        elif user_input == 5:
            save_students_to_file(list_students)
            break
        else:
            print("Invalid option. Please try again.\n")
