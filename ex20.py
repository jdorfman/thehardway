# Excercise 20 - http://learnpythonthehardway.org/book/ex20.html

#Import the argument variable module
from sys import argv

# input_file (test.txt) is going to be the argument variable 
script, input_file = argv

# First function (mini script): print_all is the function and f most likely stands for 'file'.
def print_all(f):
    print f.read() # this will print the whole file to stdout

# I need to look this up I am not sure WTF is going on here:    
def rewind(f):
    print f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline() # read one line at a time

current_file = open(input_file) # open test.txt, come to think of it there is no close function Zed!

print "First lets print the whole file: \n"
print_all(current_file) # execute the first function: print out everything from test.txt

print "Now lets rewind, kind of like a tape."
rewind(current_file) # for me this does nothing except print 'none'

print "Lets print 3 lines"
current_line = 1 # define the first line (1)
print_a_line(current_line, current_file) # 1. first line of test.txt
current_line = current_line + 1 # 2
print_a_line(current_line, current_file) # 2. second line of test.txt
current_line = current_line + 1 # 3
print_a_line(current_line, current_file) # 3. third line of test.txt

current_file.close() # added that because it is good practice

# Extra Credit
# 1: Write english comments above each line to explain what is going on.
# 2: 
