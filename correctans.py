correct = ("b", "a", "d", "d")
answer = ("b", "c", "d", "c")
score = 0
for given, correct in zip(answer, correct):
    if given == correct:
        score += 1
print(f"Your score is: {score}/4")

                         


