# Excercise 11 - http://learnpythonthehardway.org/book/ex11.html

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# Extra Credit
# 1: raw_input is a Python Function that reads a line from input and converts it to a string.  It's the easiest way to obtain user input from the command line.
# 2: Other ways to use raw_input:

print "What year where you born?",
year_born = raw_input()
current_year = 2012
# while searching the interwebs I found you can use int(variable) to add
print "Then you must be:", int(current_year) - int(year_born), "years old"

# 3: Another form, I am going to create a simple calculator:

print "First Number:",
# raw_input won't work here, drop the 'raw_' or you are going to have fun time saying WTF!?
first_number = input()
print "Second Number:",
second_number = input()

#add = first_number + second_number # overkill IMO
print "If you add the two numbers you will get:", first_number + second_number  
print "If you subtract the two numbers you will get:", first_number - second_number
print "If you multiply the two numbers you will get:", first_number * second_number

# 4: Not sure, I need to come back to this one later.






































