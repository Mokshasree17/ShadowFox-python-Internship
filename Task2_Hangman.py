import random

words = ["python", "amazon", "shadowfox", "internship", "laptop"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You Won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The word was:", word)