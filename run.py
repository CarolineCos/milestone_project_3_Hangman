import random
from words import words

def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

word = get_word(words)
print(word)
"""
def play(word):
    word_completion = "_" * len(word)
    guess = False
    guessed_letters = []
    guessed_words = []
    tries = 7
"""