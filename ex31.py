# Excercise 31 - http://learnpythonthehardway.org/book/ex31.html

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake."
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        #EC
        print "Let's play another game shall we?"

        newgame = raw_input("yes or no: ")
        if newgame == "yes":
            print "\nOk great.  First you need to go here: http://learnpythonthehardway.org/book/ex31.html"
            print "Look at the comments, specifically first comment by bungula."

            comment = raw_input("Type in the last word on line 2: ")

            if comment == "slashes":
                print "You are correct!"
            elif comment == "1":
                print "I said the second line dummy."
            else:
                print "you suck dude."
       # end EC         
        elif newgame == "no":
            print "pussy"
        else:
                print "You can't handle it brah."
                
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins."
    print "3. Understanding resolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind if jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

#easter egg #EC
elif door == "9":
    print "Congrats. You found the easter egg."

else:
    print "You stumble around and fall on a knife and die. Good job!"



# Extra Credit aka EC
# Make new parts of the game and change what decisions people can make. Expand the game out as much as you can before it gets ridiculous.






