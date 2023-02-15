"""Importing color to add to images"""
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Images to display on each wrong guessed attempt

HANGMAN = [Fore.GREEN + '''
  +---+
  |   |
      |
      |
      |
      |
=========''', Fore.GREEN + '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', Fore.GREEN + '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', Fore.YELLOW + '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', Fore.YELLOW + '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', Fore.YELLOW + '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', Fore.YELLOW + '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', Fore.RED + '''
  +---+
  |   |
  O   |
 /|\  |
 / \_ |
      |
=========''', Fore.RED + '''
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========''']

# Game Rules to be displayed when selected

GAME_INFO = Fore.BLUE + """
    ______________________________________________________________________
   |   ________________________________________________________________   |
   |  |                                                                |  |
   |  |                ===============================                 |  |
   |  |                | |                         | |                 |  |
   |  |                | |   G A M E   R U L E S   | |                 |  |
   |  |                | |                         | |                 |  |
   |  |                ===============================                 |  |
   |  |                                                                |  |
   |  |  1 - You have 8 attempts to try to find the right word by      |  |
   |  |      inputting letters or the full word                        |  |
   |  |  2 - If you guess a wrong letter you will lose an attempt and  |  |
   |  |      the hangman will begin building                           |  |
   |  |  3 - When you take 8 guesses, you will be hanged - Game Over   |  |
   |  |      POINTS:                                                   |  |
   |  |  4 - You can take a guess at the word but you will be deduted  |  |
   |  |      2 guesses                                                 |  |
   |  |________________________________________________________________|  |
   |______________________________________________________________________|
"""

# Logo to display when opening game

LOGO = Fore.CYAN + '''
                  _
                  | |                                            
                  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                  | | | | (_| | | | | (_| | | | | | | (_| | | | |
                  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |
                                    |___/    '''
