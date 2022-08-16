# use this library
from spellchecker import SpellChecker


# use examples from https://www.geeksforgeeks.org/spelling-checker-in-python/ to write function
def is_word_spelled_correct(word):
    pass


def check_list_for_spellling(words):
    for word in words:
        is_correct = is_word_spelled_correct(word)
        if is_correct:
            pass
        else:
            raise Exception(f"word {word} is not spelled correct")




