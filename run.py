import random
from words import words

correctly_guessed_letters = []
incorrectly_guessed_letters = []
randomly_chosen_word = ""
tries = 6
game_over = False



def get_word(words):
    """
    Randomly chooses a word from words.py and 
    loops until a word without a hypen or space is choosen
    """

    global randomly_chosen_word

    randomly_chosen_word = random.choice(words)
    while "-" in word or " " in word:
        randomly_chosen_word = random.choice(words)
    
    return randomly_chosen_word.upper()

def draw_word():

    """
    Checks if the letter is in the randomly chosen word. 
    Either displays the letter or an underscore.
    """
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

def draw_hangman():
    """
    The different stages of the game if there is an incorrect guess
    """
    global tries

    if tries == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    
    elif tries == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    
    elif tries == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    
     elif tries == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+--------+")
    
    elif tries == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")
    
    elif tries == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")

     elif tries == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")
        

def get_valid_letter():
    """
    Validates if user imput is a letter and whether it has been used previously
    """
    
    is_letter_valid = False
    guess = ""

    while is_letter_valid is False:
        guess = input("Guess a letter: ").upper

        if len(guess) <= 0 or len(guess) >1:
            print("Guess must be 1 letter")
        elif guess.isalpha():
            if guess in correctly_guessed_letters or guess in incorrectly_guessed_letters:
                print("You have already guessed this letter. Try again")
            else:
                is_letter_valid = True
        else:
            print("Guess must be a letter (a-z)")
    
    return guess




        




def main():
    word = get_word(words)
    play(word)
