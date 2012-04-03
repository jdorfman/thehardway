# Excercise 25 - http://learnpythonthehardway.org/book/ex25.html

def break_words(stuff):
    """ This Function will break up words for us. """
    words = stuff.split(' ')
    return words

#def sort_words(words):
#    """ Sorts the words """
#    return sorted(words)

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """ Prints the first word after popping it off. """
    word = words.pop(0)
    print word


def print_last_word(words):
    """ This will print the last word, ya hurd? - Sorry I had to..."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """ Takes in a full sentence and returns the sorted words. """
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """ Prints the first and last words of the sentence. """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#My first attempt, I will run it later to see if it does the same as above
#def print_first_and_last(sentence):
#    """ Prints the first and last words of the sentence. """
#    first = print_first_word(sentence)
#   last = print_last_word(sentence)
#    print first last

def print_first_and_last_sorted(sentence):
    """ Sorts the words then prints the first and last one. """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



# Extra Credit

# 1 - 4 Complete


