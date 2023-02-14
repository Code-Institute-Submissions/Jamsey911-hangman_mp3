"""
Hangman Game: Computer picks word from a list and user
has to guess the letters in the word or can take a guess
at the word for 2 lives.
User has 8 chances before game over.
"""

# Import Random
import random
import os
import images

# Constants


PLAY_AGAIN_MSG = """
A - PLAY AGAIN
B - GAME RULES
C - EXIT THE GAME
"""

"""
List of words for computer to randomize
"""


def select_word():
    # link to word sheet below
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
    return MY_WORD


def main_game():
    word = select_word()
    # Lives generated for user to abide by
    LIVES = len(images.HANGMAN) - 1
    # Initalize variables
    current_guess = "-" * len(word)
    # Wrong game counter
    WRONG_GUESSES = 0
    # used letter tracker
    used_letters = []
    # Main loop
    print("Welcome to Hangman")
    print("Try to guess the word")
    print(word)

    # Calcaltes how many lives are left
    while WRONG_GUESSES < LIVES and current_guess != word:
        print(images.HANGMAN[WRONG_GUESSES])
        print("You've used the following letters: ", used_letters)
        print("So far, the word is:", current_guess)
        print("You have", WRONG_GUESSES, "of 8 guesses left")

        guess = input("Select a letter:\n")
        # Checks if a single letter is entered
        if len(guess) == 1 and guess.isalpha():
            os.system("clear")
            guess = guess.upper()
        # Changes input to uppercase and checks if letter is in word
        elif guess.upper() == word:
            os.system("clear")
            break
        # 2 lives used if a word is incorrect
        elif len(guess) == len(word) and guess.upper() != word:
            os.system("clear")
            print(guess + " is incorrect.")
            WRONG_GUESSES += 1
        # Prompt for an incorrect value
        else:
            os.system("clear")
            print(guess + """is an incorrect entry, please select a
                single letter or take a guess at the word.""")
            continue
    # Check letter
        while guess in used_letters:
            print("You've already guessed that letter:", guess)
            print(images.HANGMAN[WRONG_GUESSES])
            print("You've used the following letters: ", used_letters)
            print("So far, the word is:", current_guess)
            print("You have", WRONG_GUESSES, " of 8 guesses left")
            guess = input("Enter your guess:\n").upper()
            os.system("clear")
    # Add new guessed letter to list of guessed letters
        used_letters.append(guess)
        # print(used_letters)

        if guess in word:
            print("You've guessed correctly")

            # Calcalate lives to add to lives

            NEW_CURRENT_GUESS = ""
            for letter in range(len(word)):
                if guess == word[letter]:
                    NEW_CURRENT_GUESS += guess
                else:
                    NEW_CURRENT_GUESS += current_guess[letter]

            current_guess = NEW_CURRENT_GUESS
            print(NEW_CURRENT_GUESS)
        else:
            print("That was incorrect")
            WRONG_GUESSES += 1

    # End of game
    if WRONG_GUESSES == LIVES:
        print(images.HANGMAN[WRONG_GUESSES])
        print("You've been Hanged!")
        print("The correct word is: ", word)
        end_game()
    else:
        print("You've Won! The word was", word)
        end_game()


def end_game():
    play_game = True
    while play_game:
        continue_playing = input("""
    A - PLAY AGAIN
    B - GAME RULES
    C - EXIT THE GAME
    """).upper()
        if continue_playing == "A":
            os.system("clear")
            print("You have decided to continue playing the game.")
            return main_game()
        if continue_playing == "C":
            print("Now closing the game...")
            play_game = False
        elif continue_playing == "B":
            os.system("clear")
            print(images.game_info, "Game Rules")
        else:
            print("That is not a valid option. Please try again.")


main_game()

