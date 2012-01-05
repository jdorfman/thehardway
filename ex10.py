# Excercise 10 - http://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Extra Credit
# 1: Other escape charaters:
#       \" = Double Quote (")
#       \a = ASCII Bell (BEL)
#       \b = ASCII Backspace (BS)
#       \f = ASCII Formfeed (FF)
#       \n = ASCII Linefeed (LF)
#       \r = ASCII Carrige Return (CR)
#       \v = ASCII Vertical Tab (VT)       
# 2: Use ''' (triple-single-quote) instead. 

ec_fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print ec_fat_cat

# Can you see why you might use that instead of """? - It is easier/faster to type ''' I don't see a difference...
# 3: 
# 4:
# Need ro finish 3 & 4 - Got to watch storage wars...
# Errors:
# I forgot the y in tabby_cat so I got the following:
#   print tabb_cat
#   NameError: name 'tabb_cat' is not defined

