# HANGMAN!

Hangman is a Python terminal game which runs on the code institutes mock terminal in Heroku.

The program randomly chooses a word for the word library which is hidden from the players view with underscores.
The player/user is given 6 chances to guess the word.

[Here is the live version of my project](https://hangman-project3.herokuapp.com)
<img width="743" alt="2021-11-28" src="https://user-images.githubusercontent.com/87449935/143765942-a7edaf96-3d4c-4867-805c-9112344748c7.png">

## How to play

Hangman is a pencil and paper game for two or more players. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

In this project the computer chooses a random word and replays the letters with underscore indicating the length of the word.

The player tries to guess the letters/word, for each incorrect letter a try is lost and a portion of the 'mans' body is drawen.
If the player does not guess the word before the image of the man is complete, they loss.


## Features

### Existing features

  * Random word generation
      * Word is randomly chosen
      * Player cannot see what the word is, as the letters are replaced with underscores

<img width="245" alt="2021-11-28 (1)" src="https://user-images.githubusercontent.com/87449935/143766269-a76a0c51-8e13-4434-8f1d-1b187048ef54.png">

* Accepts user imput
* Display letter if correct in the randomly chosen word display

<img width="154" alt="2021-11-28 (2)" src="https://user-images.githubusercontent.com/87449935/143766468-1933b4de-c124-48d3-b3b0-f70b61244633.png">

* Keeps a record of incorrect guessed

<img width="267" alt="2021-11-28 (3)" src="https://user-images.githubusercontent.com/87449935/143766735-b15cff9c-65b7-4ba3-b1d0-189424e1fd1a.png">

* Validates the user imput.
* Only letters a-z can be guessed and only one letter

 <img width="252" alt="2021-11-28 (6)" src="https://user-images.githubusercontent.com/87449935/143766740-a762a21f-e6fa-4502-b7ac-5d543617f0bd.png"> 
 
 ## Testing
 
 I manually tested my project by doing the following:
 
 * I used [pep8 online](http://pep8online.com/) and rectified the errors that were shown, all issues resolved:

<img width="682" alt="2021-11-28 (8)" src="https://user-images.githubusercontent.com/87449935/143766962-5eb23e8a-23fb-448f-9549-68eaeab0f33e.png">

 * I imputed incorrect data, symbols, numbers, blank imput and more that one letter.
 * Tested on the local terminal and the Code Institues Heroku terminal.
 
 ## Bugs
 
 
