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
    * [Leaderboard](#Leaderboard)
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
![Game Feature](./assets/images/features/hangman-feature-5.jpg)<br><br>

This feature displays where the main scene happens. Here the user can play and see the following information about the game:
* Numbers of letters chosen by the computer 
* Hangman stages
* Letters guessed right
* Letters guessed wrong
* Current score
* Current number of attempts
* Input to guess a letter or a full word
* Input letters to either guess a letter only or the full word

### Hangman Stage 2 

![Hangman Stage 2 ](./assets/images/readme/hangman-feature-6.jpg)<br><br>
Any time the player guesses a wrong letter, a part of the hangman appears
* 1 letter guessed wrong, the player will see the hangman and the first part of the hangman:  a rope, in green.

### Hangman Stage 3

![Hangman Stage 3](./assets/images/readme/hangman-feature-7.jpg)
* 2 letters guessed wrong the player will see the hangman and 2 parts of the hangman a rope and head in green.

### Hangman Stage 4

![Hangman Stage 4](./assets/images/readme/hangman-feature-8.jpg)
* 3 letters guessed wrong the player will see the hangman and 3 parts of the hangman rope, head and torso in yellow.

### Hangman Stage 5

![Hangman Stage 5](./assets/images/readme/hangman-feature-9.jpg)
* 4 letters guessed wrong the player will see the hangman and 4 parts of the hangman rope, head, torso and the right arm in yellow.

### Hangman Stage 6

![Hangman Stage 6](./assets/images/readme/hangman-feature-10.jpg)
* 5 letters guessed wrong the player will see the hangman and 5 parts of the hangman, rope, head, torso and both arms in red. Also the alert message "Danger Zone" will be displayed.

### Hangman Stage 7

![Hangman Stage 7](./assets/images/readme/hangman-feature-11.jpg)
* 6 letters guessed wrong and the player will see the hangman and 6 parts of the hangman rope, head, torso, both arms and left leg in red. Also the alert message "Danger Zone" will be displayed.

### Hangman Stage 8 - Lose

![Hangman Stage 8 - Lose](./assets/images/readme/hangman-feature-12.jpg)
* 7 letters guessed wrong the player will see the full hangman and the game is over.

### Hangman Stage 9 - Win

![Hangman Stage 9 - Win](./assets/images/readme/hangman-feature-13.jpg)
* If the player guessed the full word letter by letter, they will see this feature and will win the game and get 200 points.

### Hangman Stage 10 - Win Extra

![Hangman Stage 10 - Win Extra](./assets/images/readme/hangman-feature-14.jpg)
* If the player guessed all the letters that appear in the word thereby completing the word or at least guessing no more than 3 correct letters before completing the full word, this feature will appear.



