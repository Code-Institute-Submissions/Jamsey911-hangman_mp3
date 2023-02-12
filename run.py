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
my_word = 'a'
while len(my_word) < 3:
    # makes sure word is at least 3 letters long
    my_word = random.choice(WORDS)
    my_word = str(my_word).strip("[]")
    my_word = str(my_word).strip("\n")
    my_word = str(my_word).strip("\r")
    my_word = str(my_word).upper()


# """
# Lives generated for user to abide by
# """

LIVES = len(HANGMAN) - 1

# Initalize variables

current_guess = "-" * len(my_word)

# Wrong game counter

wrong_guesses = 0

# used letter tracker
used_letters = []

# Main loop
print("Welcome to Hangman")
print("Try to guess the word")
print(my_word)

while wrong_guesses < LIVES and current_guess != my_word:
    print(HANGMAN[wrong_guesses])
    print("You've used the following letters: ", used_letters)
    print("So far, the word is:", current_guess)
    print("You have", wrong_guesses, "of 8 guesses left")

    guess = input("Select a letter:")
    if len(guess) == 1 and guess.isalpha():
        os.system("clear")
        guess = guess.upper()
    elif guess.upper() == my_word:
        os.system("clear")
        print(HANGMAN[wrong_guesses])
        break
    else:
        os.system("clear")
        print(guess + " is an incorrect entry, please select a single letter.")
        continue


# Check letter
    while guess in used_letters:
        print("You've already guessed that letter:", guess)
        print(HANGMAN[wrong_guesses])
        print("You've used the following letters: ", used_letters)
        print("So far, the word is:", current_guess)
        print("You have", wrong_guesses, " of 8 guesses left")
        guess = input("Enter your guess:")
        os.system("clear")


# Add new guessed letter to list of guessed letters
    used_letters.append(guess)
    # print(used_letters)

    if guess in my_word:
        print("You've guessed correctly")

        # Calcalate lives to add to lives

        new_current_guess = ""
        for letter in range(len(my_word)):
            if guess == my_word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess
        print(new_current_guess)
    else:
        print("That was incorrect")
        wrong_guesses += 1

# End of game
if wrong_guesses == LIVES:
    print(HANGMAN[wrong_guesses])
    print("You've been Hanged!")
    print("The correct word is: ", my_word)

else:
    print("You've Won! The word was", my_word)
