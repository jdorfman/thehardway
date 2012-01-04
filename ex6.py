# Excercise 6 - http://learnpythonthehardway.org/book/ex6.html

# Start the Joke. %d is used since it is a digit
x = "There are %d types of people." % 10
#punch line 
binary = "binary"
do_not = "don't"
# Get it? Because 1 = y 0 = no
y = "Those who know %s and those who %s." % (binary, do_not)

# Now print the joke (x) and the punch line (y)
print x
print y

# Print The joke again, this time with 'I Said' in front
print "I said: %r." % x
# Print the punch line again, this time with 'I also said'
print "I also said: '%s'." % y

# Define the evaluation, False meaning: Not Funny =(
hilarious = False
# Variable asking a question in the string. In this case %r will represent the answer "False"
joke_evaluation = "Isn't that joke so funny?! %r"
# Print the question and answer
print joke_evaluation % hilarious

# Define Left side (w) & Right side (e)
w = "This is the left side of..."
e = "This is the right side."

# w is first so it will be on the left, e is second so it is on the right. The + sign puts the two strings together on one line.
print w + e

# Extra Credit
# 1 - Comments explaining - check
# 2 - Are there 4 strings put inside another string?: No
# 3 - Then how many?: 6
# 4 - I explained why adding the two strings w and e with + makes a longer string.  See the comment on line 33, above the last print function.


