# Excercise 18 - http://learnpythonthehardway.org/book/ex18.html

# *args is like the argv prarmeter but for functions
def print_two(*args): 
    arg1, arg2 = args # indenting unpacks the arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# def = define, giving the function a name. Keep it short and relevant
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_one(arg1):
    print "arg1: %r" % (arg1)

def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# Don't get discouraged, think "mini script" when Zed says "function"

# Function Check List:
    # 1. Did you start your function definition with def?
    # 2. Does your function name have only characters and _ (underscore) characters.
    # 3. Did you put an open parenthesis ( right after the function name?
    # 4. Did you put your argumnets after the parenthesis ( separated bt commas?
    # 5. Did you make each argument unique? (No duplicate names)
    # 6. Did you put a close parenthesis and a colon ): after the arguments?
    # 7. Did you indent all lines of code you in the function 4 spaces? No more, no less.
    # 8. Did you "end" your function by going back to writing with no indent? (dedenting we call it)
    
    # Run = use or call
    
    # 1. Did you call/use/run this fucntion by typing its name?
    # 2. Did you put a ( character after the name to run it?
    # 3. Did you put the values you want into the parenthesis separated by commas?
    # 4. Did you end the funtion call with a ) character?
    
    # Run, Call, Use all mean the same thing.
    # Use, Call, Run all mean the same thing.
    # Call, Use, Run all mean the same thing.
























