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
txt.close() # Extra Credit #8
#print txt.readline()
#print txt.readlines()
#print txt.readline(5)

# ask the user to type the file name
print "Type that filename again:"
file_again = raw_input("> ")
# create a variable that will open ex15_sample.txt
txt_again = open(file_again)

# print the variable and read it (print out ex15_sample.txt)
print txt_again.read()
txt.close()

# Extra Credit
# 1: Already started to write out what each line does in english.  Excercise by excercise I am starting to think like Zed...
# 2: If you are ever stumped google 'python THING' e.g. "python open"
# 3: comands are also called functions and methods
# 4: commenting out lines 17-24 and running the script again - https://github.com/jdorfman/thehardway/commit/86dbc37e8da3f2ff31127826b3205a244600e98b
# 5: commenting out lines 3 - 14 and runing the script again - https://github.com/jdorfman/thehardway/commit/b75f20b6e42b9bb97a3846f6ae359e37ef23530e
# Think of why one way of getting the filename would be better than another.
# The only thing I can see why just using 'raw_input' instead of argv is because you don't have to import
# any libraries which I think would make the script run faster.
# 6: pydoc file:
#       readline() - line 15, printed the first line of ex15_sample.txt
#       readlines() - line 16, it printed ex15_sample.txt like this:
#                     ['This is stuff I typed into a file.\n', 'It is really cool stuff.\n', 'Lots and lots of fun to have in here.\n']
#       readlines(3) - line 17, print 5 bytes - This
# 7: brb starting up python... cool shit:
# >>> filename = 'ex15_sample.txt'
# >>> txt = open(filename)
# >>> print txt.read()
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# 8: run close() after the txt variables. It is important to close files when you are done.



