# Excercise 28 - http://learnpythonthehardway.org/book/ex28.html

# Take each of these logic problems, and write out what you think the answer will be. In each case it will be either True or False.
# or true and false

True and True # True
False and True # False
1 == 1 and 2 == 1 # False
"test" == "test" # True
1 == 1 or 2 != 1 # True
True and 1 == 1 # True
False and 0 != 0 # False
True or 1 == 1 # True
"test" == "testing" # False
1 != 0 and 2 == 1 # False
"test" != "testing" # True
"test" == 1 # False
not (True and False) # True
not (1 == 1 and 0 != 1) # False
not (10 == 1 or 1000 == 1000) # False
not (1 != 10 or 3 == 4) # False
not ("testing" == "testing" and "Zed" == "Cool Guy") # True
1 == 1 and not ("testing" == 1 or 1 == 0) # False  - FAIL Answer = True
"chunky" == "bacon" and not (3 == 4 or 3 == 3) # False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") # True - FAIL Answer = False

print """

Results:

Missed 2 out of 20 =(

>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not ("testing" == 1 or 1 == 0)
True
>>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
False
>>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
False

"""

# Extra Credit:
# 1. There are a lot of operators in Python similar to != and ==. Try to find out as many "equality operators" as you can. They should be like: < or <=.
# 2. Write out the names of each of these equality operators. For example, I call != "not equal".
# 3. Play with the python by typing out new boolean operators, and before you hit enter try to shout out what it is. Do not think about it, just the first thing that comes to mind. Write it down then hit enter, and keep track of how many you get right and wrong.
# 4. Throw away that piece of paper from #3 away so you do not accidentally try to use it later.

# 1 & 2. Equality operators:
# Not Equal:
# !=  

# Equal:
# == 

# Less Than
# < 

# Less Than or Equal
# <= 

# Greater Than
# > 

# Greater Than or Equal
# >= 

# Object Identity:
# is 

# Negated Object Identity:
# is not 

# 3. 
3 == 3 < 4 != 3
5 > 4 and 8 == 9
not (1 == 1 and 0 != 1)
True and 3 == 0
1 == 1 or 2 == 1
not (10 != 1 or 1002 >= 1000)
"test" is "test5"
1 == 1 and 2 != 1
False and 1 == 1
True or 6 == 7
False or 0 == 0
"test" is not "testing"
1 != 0 and 2 == 1
not (True or 1 > 2)
False and 3 == 3
not (1 != 10 and 3 == 4)

