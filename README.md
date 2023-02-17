# Hangman - Game

# Introduction
Project milestone 3 for Code Institute Full-stack development program: Python Terminal.<br><brZ>
This project was created by myself to show a simple game using python and ran through heroku. The main goal of the game is to guess letters in order to find the word that the computer randomly selects. 

[Live Project Here](https://hang-man-mp3.herokuapp.com/)

<p align="center"><img src="./assets/images/testing/am_i_respon_hm.png" alt="Hangman game webpage on multiple devices"></p>

## README Table Content

* [Introduction](#introduction)
* [User Experience UX](#user-experience---UX)
* [Design](#Design)
    * [Colours](#Colours)
* [Logic](#logic)
     * [Flowcharts](#flowcharts)

* Game Features
    * [Logo and Intro Message](#Logo-and-Intro-Message) 
    * [Hangman Stage 1](#Hangman-Stage-1)
    * [Hangman Stage 2](#Hangman-Stage-2) 
    * [Hangman Stage 3](#Hangman-Stage-3)
    * [Hangman Stage 4](#Hangman-Stage-4)
    * [Hangman Stage 5](#Hangman-Stage-5)
    * [Hangman Stage 6](#Hangman-Stage-6)
    * [Hangman Stage 7](#Hangman-Stage-7)
    * [Hangman Stage 8 - Lose](#Hangman-Stage-8---Lose)
    * [Hangman Stage 9 - Win](#Hangman-Stage-9---Win)
    * [Hangman Stage 10 - Win Extra](#Hangman-Stage-10---Win-Extra)
    * [Menu Options](#Menu-Options)
    * [Game Rules](#Game-Rules)
    * [Exit Game](#Exit-Game)
    * [How to Play](#how-to-play)
* [Storage Data](#Storage-Data)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Python Packages](#Python-Packages)
    * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
* [Testing](#testing)
    * [PEP 8 Online](#PEP-8-Online)
    * [Lighthouse](#Lighthouse)
    * [Functionality](#Functionality)
    * [Bugs](Bugs
* [Deploying this Project](#deployment-this-project)
    * [Forking this Project](#forking-this-project)
    * [Cloning this Project](#cloning-this-project)
* [Credits](#credits)
* [Content](#content)
## User Experience - UX

### User Stories

* As a website creator, I want to:
  
1. I want to build an game to navigate.
2. I want to build a simple game to understand.
3. I want to build a game with images being visible which changes when the user progresses
4. I want to build a game that keeps score
   
* As a first time user, I want to:

1. As a First Time user, i want the program to be easy to navigate
2. As a First Time user, i want to be able to see the progress of the hangman image displayed at all stages.
3. As a First Time user, i want to be shown progress in letters i've selected.
4. As a First Time user, i want to advised if an incorrect input has been selected.
   
* As a returning visitor, I want to:

1. As a Returning user, be able to play the game again with a different word as chosen by the computer.
2. As a Returning user, I want to be able to navigate through the app consistently.
3. As a Returning user, I want to beat my previous score.
   
## Design

#### Colours
* A Sort red was chosen as a background to make the app stand out from the page and Python Colorama Model was installed in which some simple colours were chosen to make the app more visually appealing.
The colours in the game are supplied by the Python Colorama Model

### Flowcharts 
<!-- ![Flowcharts](./assets/images/readme/hangman-flowcharts.jpg)<br>
I spent time planning and thinking about the logic and flow behind the game to ensure I had a general idea of how it could be built. I created flowcharts to assist me with the logical flow throughout the application. The charts were generated using [Lucidchart](https://lucid.app/) Integration and are shown below.<br> -->

## Features

### Logo and Game Options

![Logo and Game options menu](./assets/images/features/hm-home_screen.png)

* When opening the app, the user will be shown the a logo along along with the 
Game Options menu. <br>

### Play Game

![Ask Player Name and City](./assets/images/features/hm-play-game.png)
* After the player sees the intro feature, the computer will ask the user's to input their name and city.<br>

### Rules
![Empty Input for Name and City](./assets/images/features/hm-rules.png)
* If the player does not input their name and city, this alert will appear.<br>

### Close Game
![Welcome Message and Game Rules](./assets/images/features/hm-exit.png)
* After the user inputs their name and city, the program will display the welcome message and the game rules. The player then presses any key to start the game.<br>

## Game Features

### Hangman Stage 1
![Game Feature](./assets/images/features/hm-stage-1.png)<br><br>

A welcome message along with prompt to guess the word. The Hangman design is placed below the welcome prompt. The user then has a list of information to assist with the game. They are as foolow:
* Letters already guessed
* Correct guessed letters
* Number of guesses
* A prompt to have a guess
* An Input to guess a letter or the full word

A confirmation message is displayed over the hangman image once a leeter or word is selected. This is displayed as green for a correct letter or word, red for an incorrect letter or word and white for an invalid input.

### Hangman Stage 2 

![Hangman Stage 2 ](./assets/images/features/hm-stage-2.png)<br><br>
* When the player guesses a letter or word which is not in the word, the head part of the hangman image is displayed and The display stays green


### Hangman Stage 3

![Hangman Stage 3](./assets/images/features/hm-stage-3.png)
* When the player guesses a second letter or word which is not in the word, the body part of the hangman image is displayed and The display stays green

### Hangman Stage 4

![Hangman Stage 4](./assets/images/features/hm-stage-4.png)
* When the player guesses a third letter or word which is not in the word, the left arm part of the hangman image is displayed and The display colour changes to yellow

### Hangman Stage 5

![Hangman Stage 5](./assets/images/features/hm-stage-5.png)
* When the player guesses a fourth letter or word which is not in the word, the right arm part of the hangman image is displayed and The display colour stays yellow

### Hangman Stage 6

![Hangman Stage 6](./assets/images/features/hm-stage-6.png)
* When the player guesses a fifth letter or word which is not in the word, the left leg part of the hangman image is displayed and The display stays yellow

### Hangman Stage 7

![Hangman Stage 7](./assets/images/features/hm-stage-7.png)
* When the player guesses a sixth letter or word which is not in the word, the right leg part of the hangman image is displayed and The display colour changes to red

### Hangman Stage 8

![Hangman Stage 8](./assets/images/features/hm-stage-8.png)
* When the player guesses a seventh letter or word which is not in the word, the right foot part of the hangman image is displayed and The display colour stays red

### Hangman Stage 9/Lose

![Hangman Stage 9 - Lose](./assets/images/features/hm-end-game-lose.png)
* When the player guesses a eigth letter or word which is not in the word, the hamgman design is fully complete and The display colour stays red.

### Hangman Stage 9/Win

![Hangman Stage 9 - Win](./assets/images/features/hm-end-game-win.png)
* If the player guessed the full word, they have won the game. When this happens, a prompt that the user has won along with the total points for the game.

### Menu Options

![Menu Options](./assets/images/features/hm-options.png)
* In the end of the game users will have access to the menu where they can choose from these options: <br>
[A] - Play Game <br>
[B] - Game Rules <br>
[C] - Exit Game

### Game Rules
![Game Rules](./assets/images/features/hm-rules.png)
* The Leaderboard shows the 15 players with the best scores.

### Exit Game
![Exit Game](./assets/images/features/hm-exit.png)
* The players will see this message if they will chose to exit the game by typing [C].

### How to Play
![How to Play](./assets/images/how_to/hm-how-to-1.png)<br>
![How to Play](./assets/images/how_to/hm-how-to-2.png)<br>
![How to Play](./assets/images/how_to/hm-how-to-3.png)<br>
![How to Play](./assets/images/how_to/hm-how-to-4.png)<br>
![How to Play](./assets/images/how_to/hm-how-to-5.png)<br>
![How to Play](./assets/images/how_to/hm-bonus.png)<br>
* On opening a game, the user will see a prompt welcoming them to the game[1]
The player has 8 lives[5] in which he must slect a letter or guess the word the computer has randamly selected. This list is under data.txt. 
* The player can see how many letters are in the word[4] by the spaces displayed. The computer will ask the player to input a letter or a word [7],[6].
* If the user guesses a correct letter, they will see a message from the computer [7] the letter guessed displayed in the word length [4], the hangman stage will remain the same [2].
* If the user guesses an incorrect letter, a message from the computer [9] will display and the incorrect letter will be added to the incorrect letter list [3], the hangman stage will turn to the next stage [2] and the number of guesses will increase by 1 [5]
* When the player types an invalid input, they will see a message from the computer [8].
* When the user guesses the right word they will see a prompt notification along with the total score[10]![Hangman Stage 9 - Win](./assets/images/features/hm-end-game-win.png)
* If the user guessed the full word at once, they will win recive an extra 300 points feature[11]
* 8 letters incorrectly and the player will see a notifcation that they have lost.![Hangman Stage 9 - Win](./assets/images/features/hm-end-game-lose.png)

## Technologies Used
### Languages Used 

* [Python](https://www.python.org/)

#### Python Packages

* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): returns a random integer to get a random word
* [Datetime](https://pypi.org/project/DateTime/): returns the full date
* [Gspread](https://pypi.org/project/gspread/): allows communication with Google Sheets
* [Colorama](https://pypi.org/project/colorama/): allows terminal text to be printed in different colours / styles
* [Time](https://pypi.org/project/time/): defined time sleep
* [google.oauth2.service_accoun](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts
  
### Frameworks - Libraries - Programs Used

* [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)
    * Heroku was used to deploy the live project
* [VSCode](https://code.visualstudio.com/)
    * VSCode was used to create and edit the website
* [Lucidchart](https://lucid.app/)
    * Lucidchart was used to create the flowchart
* [PEP8](http://pep8online.com/)
    * The PEP8 was used to validate all the Python code
* [Patorjk](https://patorjk.com)
    * Patorjk (ASCII Art Generator) was used to draw the game logos

## Testing

### PEP 8 Online

The [PEP8](http://pep8online.com/) Validator Service was used to validate every Python file in the project to ensure there were no syntax errors in the project.

![PEP8](./assets/images/readme/hangman-pep8-results.jpg).
* No errors or warnings were found during the testing of the code in PEP8
  
### Lighthouse 

 Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on the Desktop.

* Desktop Results:

  ![Lighthouse Result](./assets/images/testing/hm-test-lighthouse.png).

  ## Functionality 
* The terminal has no issues and is working properly 
* The typewriter starts typing at the right time and is working correctly 
* The input for name and city have the right behaviour and shows the user an alert if the input is empty
* The game rules appear without any issues after the player submits their name and city
* The option to press any key to start a game is running well
* The game runs without any issues and as expected 
* At the end of the game, the Leaderboard is updating correctly
* All the menu options are working without any fails

## Bugs 
### Python Lines too Long
![Lines to long](./assets/images/readme/hangman-issue.jpg)
![Lines to long](./assets/images/readme/hangman-issue-result.jpg)

* When I first built the ASCII art for the logo I got the warning "line too long (126 > 79 characters)" from PEP8.<br>

### Fixed Bug
![Fix Bug](./assets/images/readme/hangman-issue-fixed.jpg)
* I had to rebuild the logo using the program Patorjk (ASCII Art Generator) to avoid these issues.
* 
## Deploying this Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/)
2. Click on the project to be forked
3. Find the Fork button at the top right of the page
4. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:
  
1. Open [GitHub](https://github.com/)
2. Click on the project to be cloned
3. You will be provided with three options to choose from, HTTPS, SSH, or GitHub CLI, click the clipboard icon in order to copy the URL
4. Once you click the button the fork will be in your repository
5. Open a new terminal
6. Change the current working directory to the location that you want the cloned directory
7. Type git clone and paste the URL copied in step 3
8. Press Enter and the project is cloned

## Credits

### Content

* All the content in the game is original 
* The terminal function and template for the deployable application was provided by [Code Institute - Template](https://github.com/Code-Institute-Org/python-essentials-template)
* The Python code for the typewriter was taken from the following tutorial: [Kwasii](outube.com/watch?v=A_1THfBpCH8)
  
### Information Sources / Resources

* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Scrimba - Pyhton](https://scrimba.com/learn/python)
* [Gambiter](http://gambiter.com/paper-pencil/Hangman_game.html)


## Special Thanks

  * Special thanks to my mentor Sandeep Aggarwal, my colleagues at Code Institute, Kasia Bogucka, Shellie Downie and Mairéad Gillic for their assistance throughout this project.



