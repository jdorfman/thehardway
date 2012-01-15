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

print "\n Lets print 3 lines"
current_line = 1 # define the first line = 1
print_a_line(current_line, current_file) # 1. first line of test.txt
current_line += 1 #current_line + 1 # current_line = 2
print_a_line(current_line, current_file) # 2. second line of test.txt
current_line += 1 #current_line = 1 # current_line = 3
print_a_line(current_line, current_file) # 3. third line of test.txt

current_file.close() # added that because it is good practice

# Extra Credit
# 1: Write english comments above each line to explain what is going on.
# 2: Each time print_a_line is run you are passing in a variable current_line. Write out what current_line is equal to on each function call, 
# and trace how it becomes line_count in print_a_line.
# 3: Find each place a function is used, and go check its def to make sure that you are giving it the right arguments.
# It looks like every function is right except the seek()
# I am still stumped with seek() - I read this: http://www.sthurlow.com/python/lesson10/ which makes more sense than python.org but still stumped
# 4: Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
# I was able to find a use for seek, but it kept breaking my print_a_line function
# Lets say you want to start printing test.txt after t in the on line 1:
# you would type:
# f.seek(8)
# f.read()
# he people out there. # < it will print that.
# 5: Research the shorthand notation += and rewrite the script to use that.
# += adds another value with the variable's value and assigns the new value to the variable.
# Just when I was going to give up...:
# Starting with line 31: current_line += 1 instead of current_line + current_line = 2





 
