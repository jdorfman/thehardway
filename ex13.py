# Excercise 13 - http://learnpythonthehardway.org/book/ex13.html

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

# import allows you to add features (modules) to your script from the python feature (module) set. e.g.: import the sys module
# argv = argument variable (not verbose, nub)
# If you have an argument with two words you must do the following:
# python ex13.py 'DIET COKE' apple Yum
# _______________^ notice that sexy '

# Extra Credit

# 1: If you give the script less than 3 args you will get the following error:
# ValueError: need more than 3 values to unpack
# The reason we get that ValueError is because in order for the script to run it needs 3 (no more, no less) arguments.

# 2: See ex13-ec2a.py and ex13-ec2b.py

# 3: See ex13-ec3.py

# 4: Modules give you features.
# Modules give you features.
# What gives you features in Python? MODULES!!!!
