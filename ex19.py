# Excercise 19 - http://learnpythonthehardway.org/book/ex19.html

# Let's Define a Function (mini script) called cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # The following will be executed when 'cheese_and_crackers' is called
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that is enough for a party!"
    print "Get a blanket. \n"
    
print "We can just give the function numbers directly:"
# 20 & 30 will replace %d (% cheese_count, % boxes_of_crackers)
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
cheese_count = 30
boxes_of_crackers = 40
#                    30           40
cheese_and_crackers(cheese_count, boxes_of_crackers)


print "We can even do math inside:"
#                     60        130   
cheese_and_crackers(30 + 30, 40 + 90)

print "We can combine the two, variables and math:"
#                               60               90   
cheese_and_crackers(cheese_count + 30, boxes_of_crackers + 50)

# Extra Credit:
# 1: Comment above each line explaining what is happening in English
# 2: Start at the bottom and read each line backwards, saying all the important characters.
# 3: Write at least one more function of your own design, and run it 10 different ways:

def zoe(walk_zoe, feed_zoe):
    print "I walk Zoe %r times a day." % walk_zoe
    print "I feed Zoe %r times a day. \n" % feed_zoe

# 1st way
zoe(2,2)

# 2nd way
walk_zoe = 2
feed_zoe = 2
zoe(walk_zoe, feed_zoe)

# 3rd way
print "How many times should you walk Zoe?"
walk_zoe = raw_input("> ")
print "How many times should you feed Zoe?"
feed_zoe = raw_input("> ")
zoe(walk_zoe, feed_zoe)

# 4th way
walk_zoe = (1 + 1)
feed_zoe = (2 + 0)
zoe(walk_zoe, feed_zoe)

# 5th way
walk_zoe = 1
feed_zoe = 1
zoe(walk_zoe + 1, feed_zoe + 1)

# 6th way
i = 1
x = 1
# I already defined walk_zoe and feed_zoe above =)
zoe(i + walk_zoe, x + feed_zoe)

# 7th way
walk_zoe = (2 * i)
feed_zoe = (1 * x + 1)
zoe(walk_zoe, feed_zoe)

# 8th way, starting to run out of ideas...
# Not sure how to get rid of the /n's
from sys import argv # I know this should be at the top, but this is Extra Credit, so STFU.

script, fn = argv

# fn = ex19ec = the file with '2' in it
of = open(fn)
walk_zoe = of.read()
of.close()
of = open(fn)
feed_zoe = of.read()
zoe(walk_zoe, feed_zoe)
of.close()

# 9th way - Really running out of ideas...

walk_zoe = 2
feed_zoe = 2
ascii_zoe = '''
      I <3
   _   _   _  
  / \ / \ / \ 
 ( Z ) o ) e )
  \_/ \_/ \_/ 
            '''
print ascii_zoe
zoe(walk_zoe, feed_zoe)


# 10th way

length = 'ii'
walk_zoe = len(length)
feed_zoe = len(length)
zoe(walk_zoe, feed_zoe)


