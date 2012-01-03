# This is Exercise no. 3 - http://learnpythonthehardway.org/book/ex3.html

print "I will now count my chickens:"


# Count the Hens
print "Hens", 25 + 30 / 6 
# Count the Roosters
print "Roosters", 100 - 25 * 3 % 4 

print "Now I will count the eggs:"

# Count the Eggs
print 3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6 

print "Is it true that 3 + 2 < 5 - 7"

# True or False? This will be false because -2 is less than 5
print 3 + 2 < 5 - 7

# Calculate 3 + 2
print "what is 3 + 2?", 3 + 2
# Calculate 5 - 7
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's false."

print "How about some more."

# True or False: Is 5 greater than -2?
print "Is it greater?", 5 > -2 # This will Print True
#True or False: Is 5 greater or equal to -2? 
print "Is it greater or equal?", 5 >= -2 # This will also print True
# True or false: Is 5 less than or equal to -2?
print "Is it less or equal?", 5 <= -2 # This will print False, because it is a negative number.

# Extra Credit:
# 1: Comments, done.
# 2:
# jdorfman@jd:~/github/python/thehardway$ python
# Python 2.6.6 (r266:84292, Sep 15 2010, 15:52:39) 
# [GCC 4.4.5] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 3 + 2 + 8 + 9
# 22
#####################
# 4: Research a "floating point" number.
# Basically it is a way for Python to take an extremely long number (0.1024382382837547347374) and rounds it off to be more human readable.
# From Python.org: ...more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead
# http://docs.python.org/tutorial/floatingpoint.html
# 3 & 5 see: ex3-ec.py

