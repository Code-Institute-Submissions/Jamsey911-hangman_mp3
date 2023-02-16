"""
Hangman Game: Computer picks word from a list and user
has to guess the letters in the word or can take a guess
at the word for 2 lives.
User has 8 chances before game over.
"""
import random
import os
import design

import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Opening page
PLAY_AGAIN_MSG = """
  A - PLAY GAME
  B - GAME RULES
  C - EXIT THE GAME
"""

TXT = " "
X = TXT.center(23)

RULES = design.GAME_INFO

LOGO = design.LOGO


def select_word():
    """List of words for computer to randomize"""
    # link to word sheet below
    file = open('data.txt', encoding="utf-8")
    words = file.readlines()
    file.close()
    my_word = "a"
    while len(my_word) < 3:
        # makes sure word is at least 3 letters long
        my_word = random.choice(words)
        my_word = str(my_word).strip("[]")
        my_word = str(my_word).strip("\n")
        my_word = str(my_word).strip("\r")
        my_word = str(my_word).upper()
    return my_word


def main_game():
    """Main game loop"""
    word = select_word()
    # Lives generated for user to abide by
    lives = len(design.HANGMAN) - 1
    # Initalize variables
    current_guess = "-" * len(word)
    # Wrong game counter
    wrong_guesses = 0
    # used letter tracker
    used_letters = []
    # Calcalates score
    score = 0
    # Main loop
    print("\n", X, " Welcome to Hangman."
          "\n", X, "Try to guess the word")
    print(word)

    # Calcaltes how many lives are left
    while wrong_guesses < lives and current_guess != word:
        print(design.HANGMAN[wrong_guesses])
        print("You've used the following letters: ", used_letters,
              "\nSo far, the word is:", current_guess,
              "\nYou have", wrong_guesses, "of 8 guesses left")

        #  Input for player to enter their guess
        guess = input("Enter your guess:\n").upper()

        # Checks if a single letter is entered
        if len(guess) == 1 and guess.isalpha():
            os.system("clear")
            guess = guess.upper()
        # Changes input to uppercase and checks if guess is the word
        elif guess == word:
            os.system("clear")
            score += 300
            break
        # 2 lives used if a word is incorrect
        elif len(guess) == len(word) and guess != word:
            os.system("clear")
            print("\n", X, guess + " is incorrect.")
            wrong_guesses += 1
        # Prompt for an incorrect value
        else:
            os.system("clear")
            print(guess, " is an incorrect entry, please select a single"
                         "\nletter or take a guess at the word.")
            continue
    # Check letter
        while guess in used_letters:
            os.system("clear")
            print("\n", X, "You've already guessed that letter:", guess,
                  design.HANGMAN[wrong_guesses])
            print("You've used the following letters: ", used_letters,
                  "\nSo far, the word is:", current_guess)
            print("You have", wrong_guesses, " of 8 guesses left")
            guess = input("Enter your guess:\n").upper()

    # Add new guessed letter to list of guessed letters
        used_letters.append(guess)
        # print(used_letters)

        if guess in word:
            os.system("clear")
            score += 25
            print(X, f"{Fore.GREEN}You've guessed correctly")

            # Checks if the guessed letter is in the word
            new_current_guess = ""
            for letter in range(len(word)):
                if guess == word[letter]:
                    new_current_guess += guess
                else:
                    new_current_guess += current_guess[letter]

            current_guess = new_current_guess
        else:
            os.system("clear")
            print(X, f"{Fore.RED} {guess} is incorrect")
            wrong_guesses += 1
    game_over(wrong_guesses, word, lives, score)


def game_over(wrong_guesses, word, lives, score):
    """Calcalates wrong guesses to guesses left """
    if wrong_guesses == lives:
        print(X, design.HANGMAN[wrong_guesses])
        print(X, f"{Fore.RED}You've been Hanged! The correct word is: ", word)
        start_options()
    else:
        print(X, design.HANGMAN[wrong_guesses])
        print(X, f"{Fore.GREEN}You've Won! The word was", word)
        print(X, "Your score is: ", score)
        start_options()


def start_options():
    """Displays game options screen"""
    play_game = True
    while play_game:
        continue_playing = input(PLAY_AGAIN_MSG).upper()
        if continue_playing == "A":
            os.system("clear")
            return main_game()
        if continue_playing == "C":
            print(X, "Now closing the game...")
            play_game = False
        elif continue_playing == "B":
            os.system("clear")
            print(RULES)
        else:
            print("That is not a valid option. Please try again.")


print(LOGO)
start_options()
