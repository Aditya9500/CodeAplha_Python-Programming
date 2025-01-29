import random

# List of words for the game
word_list = ["python", "hangman", "programming", "developer", "computer"]

# Choose a random word
word = random.choice(word_list)
word_display = ["_"] * len(word)
attempts = 6  # Number of incorrect guesses allowed
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(word_display))

while attempts > 0 and "_" in word_display:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
        print("Correct!", " ".join(word_display))
    else:
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left.")

if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
