# Excercise 15 - http://learnpythonthehardway.org/book/ex15.html

from sys import argv

# filename = ex15_sample.txt
script, filename = argv

# txt = open(ex15_sample.txt)
txt = open(filename)

# print: Here is your file 'ex15_sample.txt'
print "Here is your file %r" % filename
# open ex15_sample.txt and read it (print it)
print txt.read()

# ask the user to type the file name
##print "Type that filename again:"
##file_again = raw_input("> ")

# create a variable that will open ex15_sample.txt
##txt_again = open(file_again)

# print the variable and read it (print out ex15_sample.txt)
##print txt_again.read()

# Extra Credit
# 1: Already started to write out what each line does in english.  Excercise by excercise I am starting to think like Zed...
# 2: If you are ever stumped google 'python THING' e.g. "python open"
# 3: comands are also called functions and methods
# 4: commenting out lines 17-24 and running the script again
# 5: commenting out lines 3 - 14 and runing the script again
