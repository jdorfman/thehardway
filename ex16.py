# Excercise 16 - http://learnpythonthehardway.org/book/ex16.html

from sys import argv

script, filename = argv

# Reads the argument (test.txt)
print "We are going to erase %r" % filename
# This will allow the user to quit the script and not have the file truncated.
print "If you don't want to do that press Ctrl-C (^C)"
print "If you want to do that press return"

# this allows the user to erase the file. 'Enter/return' will allow the script to continue.
raw_input("?")

# Open the file with write privliges.
print "Opening the file..."
target = open(filename, 'w')

# Erase the file
print "Truncating the File"
target.truncate()

print "Now I am going to ask you for 3 lines."
# allow the user to input 3 lines
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to a file."

# This writes the users input to the file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Extra Credit #3, only took about 30 minutes... =)
target.writelines(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally we close it."
# save and close the file
target.close()

# Extra Credit 
# 1: Commenting now... How do you like dem apples?
# 2: Write a script that will read test.txt:

read_target = open(filename, 'r')

print "\n Here is what you wrote:"

print read_target.read()
read_target.close()

# 3: replace the 6 target.write with 1
# 4: We had to pass 'w' because that is the only way you can truncate a file. if you used 'a' it would just append this to the end of the file.
# 5: if you use 'w+' it will truncate the file meaning you won't have run 'target.truncate()'
# Read more here: http://docs.python.org/library/functions.html#open

