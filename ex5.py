# Excercise 5 - http://learnpythonthehardway.org/book/ex5.html

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 # pounds / lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# %s is for strings like 'Zed A. Shaw' or 'White'
print "Let's talk about %s." % my_name
# %d is needed for numbers or else you will get long decimals...
print "He is %d inches tall." % my_height
print "He is %d pounds heavy" % my_weight
print "Actually that is not that heavy"
# back to using %s for strings
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# this line is tricky, try to get it exaxtly right...
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)



