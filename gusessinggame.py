import random
secret = random.randint(1, 100)
chances = 0
while chances < 10:
    given = int(input("Enter a number between 1 and 100: "))
    chances += 1
    if given == secret:
        print("Good! correct number:", secret)
        break
    elif given < secret:
        print("Low! Try again.")
    else:
        print("High! Try again.")
else:
    print("try over. The correct number was:", secret)