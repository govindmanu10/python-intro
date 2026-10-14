
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ")

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Error: Marks must be between 0 and 100.")
            return

        grade = calculate_grade(marks)

        print("\n--- Student Result ---")
        print(f"Name: {name}")
        print(f"Marks: {marks:g}/100")
        print(f"Grade: {grade}")

        if grade == "F":
            print("Status: Needs improvement")
        else:
            print("Status: Passed!")

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
