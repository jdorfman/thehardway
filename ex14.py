# Excercise 14 - http://learnpythonthehardway.org/book/ex14.html

from sys import argv

script, user_name, fav_drink = argv # added fav_drink for EC #3
#prompt = '> '
# Extra Credit #2
prompt = '--> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I would like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What type of computer do you have?"
computer = raw_input(prompt)

print """
Alright so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Now open a cold %r.
""" % (likes, lives, computer, fav_drink)

# Extra Credit
# 1: Not really into games so I'll pass.  Thanks though.
# 2: Switched the prompt variable to -->
# 3: The argument I will add is Favorite Drink
# Works: Now open a cold 'Diet Coke'.
# 4: Oh I noticed, now I know you can do that.  I am sure it will come in handy. """ %
