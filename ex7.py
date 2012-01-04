# Excercise 7 - http://learnpythonthehardway.org/book/ex7.html

# Three lines of Mary and her lamb
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# Multiply the period ten times and print it to the screen
print "." * 10 # what'd that do? - Just ran it, it adds a row of 10 periods [.]

# Define Cheese Burger one character at a time.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch the comma on the end. Try removing it to see what happens...
# Print Cheese
print end1 + end2 + end3 + end4 + end5 + end6, # with out the comma it puts Burger below Cheese
# Print Burger
print end7 + end8 + end9 + end10 + end11 + end12

# mistakes: forgot the + between end10 & end 11 which resulted in a SyntaxError: invalid syntax

