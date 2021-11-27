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
    
    while "-" in randomly_chosen_word or " " in randomly_chosen_word:
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
    letter = ""

    while is_letter_valid is False:
        guess = input("Guess a letter:\n ")
        guess.upper()
        if len(guess) <= 0 or len(guess) > 1:
            print("Guess must be 1 letter")
        elif guess.isalpha():
            if guess in correctly_guessed_letters or guess in incorrectly_guessed_letters:
                print("You have already guessed this letter" + guess + ".  Try again")
            else:   
                is_letter_valid = True
        else:
            print("Guess must be a letter (a-z)")
    
    return guess


def guess_letter():
    """
    Checks if the letter in in the random word and will append it to the correct variable
    """
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global tries

    guess = get_valid_letter()

    if guess in randomly_chosen_word:
        correctly_guessed_letters.append(guess)
    else:
        incorrectly_guessed_letters.append(guess)
        tries -= 1

def is_game_over():
    global tries
    global game_over
    global correctly_guessed_letters

    if tries <= 0:
        game_over = True
        draw_hangman()
        print("You lost, the word was " + randomly_chosen_word + ". Try again.")
    else:
        guessed_all_letters = True
        for guess in randomly_chosen_word:
            if guess not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print("You Won.")

def main():

    global game_over

    print("Lets play Hangman!\n")
    get_word(words)

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print("\n")
            print("Incorrect guesses: ")
            print(incorrectly_guessed_letters)

        guess_letter()
        is_game_over()
    
        


main()