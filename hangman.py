import random

# 1. List of words
words = ["python", "computer", "coding", "program", "developer"]

# 2. Choose a random word
word = random.choice(words)

# 3. Create hidden version of the word
display = ["_"] * len(word)

# 4. Number of incorrect guesses
wrong_guesses = 0

# 5. Store letters already guessed
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# 6. Game loop
while wrong_guesses < 6 and "_" in display:

    print("Word:", " ".join(display))
    print("Wrong guesses:", wrong_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Check if input is one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # 7. Check whether letter is in the word
    if guess in word:
        print("✅ Correct guess!\n")

        # Reveal the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!\n")


# 8. Check game result
if "_" not in display:
    print("🎉 You won!")
    print("The word was:", word)

else:
    print("💀 Game over!")
    print("The word was:", word)