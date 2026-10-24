import random
secret = random.randint(1, 100)
given = int(input("Enter a number between 1 and 100: "))
while given != secret:
    if given < secret:
        print("low number! Try again.")
    else:
        print(" higher number! Try again.")
    given = int(input("Enter a number between 1 and 100: "))
print("good! You guessed the correct number:", secret)