import random

words = ("warlock", "hydra", "rat", "demon", "dragon lord", "were lion")
word = random.choice(words)
correct = word

print("Word lenght is ", len(word))
print("You may ask for 3 letters and i will tell you if word contains those letters: ")
print(word)
for x in range(3):
    letter = input("Ask me for letter: ")
    try:
        word.index(letter)
    except ValueError:
        print("wrong guessa")
    else:
        print("Found!")

# while count < 3:
#     letter = input("Ask me for letter: ")
#     if word.find(letter) > -1:
#         print("Found!")
#     else:
#         print("Not found!")
#     count += 1

while word != input("Guess word: "):
    print("Try again!")

print("good job")