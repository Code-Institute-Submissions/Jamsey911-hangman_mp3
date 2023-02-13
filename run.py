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
C - EXIT THE GAME
"""

"""
List of words for computer to randomize
"""
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


# """
# Lives generated for user to abide by
# """
def MAIN_GAME():
    LIVES = len(images.HANGMAN) - 1

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


# Calcaltes how many lives are left
    while WRONG_GUESSES < LIVES and current_guess != MY_WORD:
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
        elif guess.upper() == MY_WORD:
            os.system("clear")
            break
        # 2 lives used if a word is incorrect
        elif len(guess) == len(MY_WORD) and guess.upper() != MY_WORD:
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
            guess = input("Enter your guess:\n")
            os.system("clear")
    # Add new guessed letter to list of guessed letters
        used_letters.append(guess)
        # print(used_letters)

        if guess in MY_WORD:
            print("You've guessed correctly")

            # Calcalate lives to add to lives

            NEW_CURRENT_GUESS = ""
            for letter in range(len(MY_WORD)):
                if guess == MY_WORD[letter]:
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
        print("The correct word is: ", MY_WORD)

    else:
        print("You've Won! The word was", MY_WORD)
        user_input = input(f"{PLAY_AGAIN_MSG}>>> ").lower()
        while True:
            if user_input == "a":
                os.system("clear")
                print("You have decided to continue playing the game.")
                return MAIN_GAME()
            if user_input == "c":
                print("Now closing the game...")
                print("Thanks for playing, Hope to see you again soon!")
                break
            else:
                print("That is not a valid option. Please try again.")
                user_input = input(f"{PLAY_AGAIN_MSG}>>> ").lower()


MAIN_GAME()
