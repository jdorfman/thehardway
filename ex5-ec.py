# Excercise 5 - http://learnpythonthehardway.org/book/ex5.html

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # pounds / lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# %r is for strings like 'Zed A. Shaw' or 'White'
print "Let's talk about %r." % name
# %d is needed for numbers or else you will get long decimals...
print "He is %d inches tall." % height
print "He is %d pounds heavy." % weight
print "Actually that is not that heavy."
# back to using %r for strings
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffe." % teeth

# this line is tricky, try to get it exactly right...
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Extra Credit:
# 1: remove 'my_' gedit find and replace
# 2: When I switch %s to %r it started printing 'Zed A. Shaw' instead of Zed A. Shaw.
# 3: Have Fun: http://docs.python.org/release/2.5.2/lib/typesseq-strings.html
# 4: write some variables that convert the inches and pounds to centimeters and kilos:
# inches to centimeters - 2.54cm in 1 inch - pounds to kilos - 0.45359237 in 1 pount
cm = 2.54
cm_height = cm * height
print "%s is this tall in centimeters: %s" % (name, cm_height)

kilo = 0.45359237
kilo_pound = kilo * weight
print "%s weighs about %d kilos." % (name, kilo_pound)



















