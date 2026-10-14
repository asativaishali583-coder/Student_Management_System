import csv
import os

FILE_NAME = "students.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Marks"])


def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        marks = float(input("Enter Student Marks (0-100): "))

        if not student_id or not name:
            print("Error: ID and name cannot be empty.")
            return

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return

        if not 0 <= marks <= 100:
            print("Error: Marks must be between 0 and 100.")
            return

        with open(FILE_NAME, "r", newline="") as file:
            students = list(csv.DictReader(file))

        if any(student["ID"] == student_id for student in students):
            print("Error: Student ID already exists.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, marks])

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter a valid age and marks.")
    except OSError as error:
        print(f"File error: {error}")


def view_students():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            students = list(csv.DictReader(file))

        if not students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        for student in students:
            print(
                f"ID: {student['ID']} | "
                f"Name: {student['Name']} | "
                f"Age: {student['Age']} | "
                f"Marks: {student['Marks']}"
            )

    except OSError as error:
        print(f"File error: {error}")


def search_student():
    student_id = input("Enter Student ID to search: ").strip()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            students = list(csv.DictReader(file))

        for student in students:
            if student["ID"] == student_id:
                print("\nStudent Found!")
                print(student)
                return

        print("Student not found.")

    except OSError as error:
        print(f"File error: {error}")


def main():
    initialize_file()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()