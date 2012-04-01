# http://learnpythonthehardway.org/book/ex33.html
# Got a little help: http://stackoverflow.com/q/9857059/1258484

i = 0 
numbers = []

def theloop(numb, plusnum):
	global i
	while i < numb:
		print "At the top of i is %d" % i
		numbers.append(i)

		i = i + plusnum
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
		print "The numbers: "
		for num in numbers:
			print num

theloop(7, 2)


# Extra Credit

#Convert this while loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#Now use this function to rewrite the script to try different numbers.
#Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
#Rewrite the script again to use this function to see what effect that has.
#Now, write it to use for-loops and range instead. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
