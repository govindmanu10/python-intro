score = (17, 12, 9, 15, 13)
your_score = int(input("Enter your score: "))
position = 0
for position, score in enumerate(score, start=1):
    if your_score > score:
        break
print(f"Your position is: {position}")
   
