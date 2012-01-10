# Excercise 17 - http://learnpythonthehardway.org/book/ex17.html
# See how short you can make the script. I could make this 1 line long.
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
input = open(from_file)
indata = input.read()
output = open(to_file, 'w')
output.write(indata)
output.close()
input.close()

# That is as small as I can make it.  One day I will make it one-line, one day...
