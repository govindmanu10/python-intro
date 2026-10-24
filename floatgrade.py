grade = float(input("Enter your grade: "))
if grade > 20: 
    print("Invalid grade. enter a grade between 0 and 20.")
    if grade > 0:
        print("Invalid grade. enter a grade between 0 and 20.")
    elif grade >= 16:
        print("Grade is very good.")
    elif grade >= 14:
        print("Grade is good.")
    elif grade >= 12:
        print("Grade is fairly good.")
    elif grade >= 10:
        print("Grade is pass.")
    else:
        print("Grade is fail.")