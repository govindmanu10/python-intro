def get_student_details():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    return name, student_id


def display_student(name, student_id):
    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Student ID: {student_id}")


if __name__ == "__main__":
    name, student_id = get_student_details()
    display_student(name, student_id)