import random
from words import words


def get_word(words):
    """
    Randomly chooses a word from words.py and 
    loops until a word without a hypen or space is choosen
    """
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()



def play(word):
    """
    Replaces the letters of the choosen word with underscores.
    Saves the guessed letters and words.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Lets play Hangman")
    print(word_completion)
    print(guessed_letters)


    while not guessed and tries > 0:
        guess = input("Guess a word or letter: ").upper

        if len(guess) == 1 and guess.isalhpa():
            if guess in guessed_letters:
                print("You have already guessed", guess)
                elif guess not in word:
                    print("Sorry", guess, "is not in the word")
                    tries -= 1
                    guessed_letters.append.(guess) 
                else:
                    print("Great", guess, "is in the word!")
                    guessed_letters.append(guess)
                    




        




def main():
    word = get_word(words)
    play(word)
