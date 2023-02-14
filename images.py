"""Images to display on each wrong guessed attempt"""
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

game_info = [
 # hangman game rules
 """
    _________________________________________________________________________
   |   ___________________________________________________________________   |
   |  |                                                                   |  |
   |  |                ===============================                    |  |
   |  |                | |                         | |                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                | |                         | |                    |  |
   |  |                ===============================                    |  |
   |  |                                                                   |  |
   |  |  1 - You have 8 attempts to try to find the right word by         |  |
   |  |      inputting letters or the full word                           |  |
   |  |  2 - If you guess a wrong letter you will lose an attempt and the |  |
   |  |      hangman will begin building                                  |  |
   |  |  3 - When you take 8 guesses, you will be hanged - Game Over      |  |
   |  |  POINTS:                                                          |  |
   |  |  4 - You can take a guess at the word but you will be deduted 2   |  |
   |  |  guesses                                                          |  |
   |  |___________________________________________________________________|  |
   |_________________________________________________________________________|
""",]
