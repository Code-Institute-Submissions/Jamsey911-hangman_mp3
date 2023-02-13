"""
Hangman Game: Computer picks word from a list and user
has to guess the letters in the word.
User has 8 chances before game over.
"""

# Import Random
import random
import os

# Constants
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \_ |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''']

"""
List of words for computer to randomize
"""
file = open('data.txt', 'r')
WORDS = file.readlines()
file.close()
MY_WORD = 'a'
while len(MY_WORD) < 3:
    # makes sure word is at least 3 letters long
    MY_WORD = random.choice(WORDS)
    MY_WORD = str(MY_WORD).strip("[]")
    MY_WORD = str(MY_WORD).strip("\n")
    MY_WORD = str(MY_WORD).strip("\r")
    MY_WORD = str(MY_WORD).upper()


# """
# Lives generated for user to abide by
# """

LIVES = len(HANGMAN) - 1

# Initalize variables

current_guess = "-" * len(MY_WORD)

# Wrong game counter

WRONG_GUESSES = 0

# used letter tracker
used_letters = []

# Main loop
print("Welcome to Hangman")
print("Try to guess the word")
print(MY_WORD)

while WRONG_GUESSES < LIVES and current_guess != MY_WORD:
    print(HANGMAN[WRONG_GUESSES])
    print("You've used the following letters: ", used_letters)
    print("So far, the word is:", current_guess)
    print("You have", WRONG_GUESSES, "of 8 guesses left")

    guess = input("Select a letter:\n")
    if len(guess) == 1 and guess.isalpha():
        os.system("clear")
        guess = guess.upper()
    elif guess.upper() == MY_WORD:
        os.system("clear")
        print(HANGMAN[WRONG_GUESSES])
        break
    elif len(guess) == len(guess) and guess.upper() != MY_WORD:
        os.system("clear")
        print(guess + " is incorrect.")
        WRONG_GUESSES += 1
    else:
        os.system("clear")
        print(guess + " is an incorrect entry, please select a single letter.")
        continue


# Check letter
    while guess in used_letters:
        print("You've already guessed that letter:", guess)
        print(HANGMAN[WRONG_GUESSES])
        print("You've used the following letters: ", used_letters)
        print("So far, the word is:", current_guess)
        print("You have", WRONG_GUESSES, " of 8 guesses left")
        guess = input("Enter your guess:\n")
        os.system("clear")


# Add new guessed letter to list of guessed letters
    used_letters.append(guess)
    # print(used_letters)

    if guess in MY_WORD:
        print("You've guessed correctly")

        # Calcalate lives to add to lives

        new_current_guess = ""
        for letter in range(len(MY_WORD)):
            if guess == MY_WORD[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess
        print(new_current_guess)
    else:
        print("That was incorrect")
        WRONG_GUESSES += 1

# End of game
if WRONG_GUESSES == LIVES:
    print(HANGMAN[WRONG_GUESSES])
    print("You've been Hanged!")
    print("The correct word is: ", MY_WORD)

else:
    print("You've Won! The word was", MY_WORD)
