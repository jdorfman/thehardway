# http://learnpythonthehardway.org/book/ex35.html

from sys import exit

def helpme():
	print """
			
-----------------------------------------------------------------
|                                      |                        |
|                                      |                        |
|           GOLD ROOM                  |                        |
|                                      |                        |
|                                      |                        |
|                                      |                        |
|-------------______-------------------|                        |
|                                      |                        |
|                                      |      Clthlhu ROOM      |
|                   BEAR ROOM          |                        |
|                                      |                        |
|                                      |                        |
|                   Left Door >        |       < Right Door     |
--------------------------------______---______------------------
|                                                               |
|                                                               |
-----------------------------------------------------------------
                                   Dark Room
		  """
	start()		


def gold_room():
	print "This room is full of gold.  How much do you take?"

# Still need to figure this 'bug' out
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy, You Win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		#exit(0)

def bear_room():
	print "There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?"
	print "\n1. Take the Honey from the bear."
	print "2. Taunt the bear.\n"
	bear_moved = False

	while True:
		next = raw_input("> ")
		
		if next == "1":
			dead("The bear looks at you and slaps your face off")
		elif next == "2" and not bear_moved:
			print "the bear has moved from the door. Hit enter to go through now."
			bear_moved = True
		elif next == "" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means. Please type 1 or 2"

def cthulhu_room():
	print "Here you see the great evil Clthlhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next :
		start()
	elif "head" in next:
		dead("Well that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a in a dark room.\nThere is a door to your right and left.\nWhich one do you take?\nType M for a Map."

	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	elif next == "M":
		helpme()
	elif next == "":
		print "To lazy to type? No problem I can take care of that for you...\n"
		bear_room()
	else:
		dead("You stumble around the room until you starve.")

start()

# Extra Credit

# 1. Draw a map of the game and how you flow through it.
# 2. Fix all of your mistakes, including spelling mistakes.
# 3. Write comments for the functions you do not understand. Remember doc comments?
# 4. Add more to the game. What can you do to both simplify and expand it.
# 5. The gold_room has a weird way of getting you to type a number. What are all the bugs in this way of doing it? Can you make it better than just checking if "1" or "0" are in the number? Look at how int() works for clues.
