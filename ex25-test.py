
import ex25

sentence = "All good things come to those who wait."


words = ex25.break_words(sentence)
print words

sorted_words = ex25.sort_words(words) # s/words/sentence/ and you get: 
# ...'A', 'a', 'c', 'd', 'e', 'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'l', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 's', 's', 't', 't', 't', 't', 'w', 'w']
print sorted_words

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
# if you print ^ it adds 'none' below each line

print sorted_words

sorted_words = ex25.sort_sentence(sentence)
print sorted_words

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)



