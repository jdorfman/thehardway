# Excercise 29 - http://learnpythonthehardway.org/book/ex29.html

people = 20
cats = 30
dogs = 15

# Extra Credit 5:
#people = 23
#cats = 10
#dogs = 18

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats the world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs." 

if people == dogs:
    print "People are dogs..."


# Extra Credit

# 1. What do you think the if does to the code under it?
#       The 'if' lets 'print' (the code under) know if it is ok to output the statement. 
        
# 2. Why does the code under the if need to be indented 4 spaces?
#       Because it looks pretty?  Let me google... Python forces you to obey its indentation rules - http://bit.ly/yjU3IJ

# 3. What happens if it isn't indented?
#       If the code is not indented then python will give this error: IndentationError: expected an indented block

# 4. Can you put other boolean expressions from Ex. 27 in the if-statement? Try it.

if people != cats:
    print "Moar Cats!"

if people < cats and cats > dogs:
    print "Cats out number us!" 

if cats < dogs or dogs > cats:
    print "This shouldn't print (false statement)."

if cats < dogs or dogs < cats:
    print "This should print."

if not (cats > people and people < dogs):
    print "This should print because it is TRUE."

if not (cats > people or people < dogs):
    print "This shouldn't print because it is FALSE."


# 5. What happens if you change the initial variables for people, cats, and dogs?
# This Happens:

print """

Not many cats the world is saved!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs...
Moar Cats!
This shouldn't print (false statement).
This should print.
This should print because it is TRUE.
This shouldn't print because it is FALSE.

"""


