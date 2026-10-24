words = str(input("Enter a word: "))
vowels = 0
for i in words:
    if i in "aeiouAEIOU":
        vowels += 1 
print(" vowels in", words, "is", vowels)