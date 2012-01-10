# Excercise 17 - http://learnpythonthehardway.org/book/ex17.html

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "\nCopying from %s to %s" % (from_file, to_file)

# we could put these two on one line too, how?
input = open(from_file)
indata = input.read()

#print "The input file is %d bytes long" % len(indata) # Sorry but you have been removed via EC #2

#print "Does this file even exists? %r" % exists(to_file) # Sorry but you have been removed via EC #2
#print "Read, hit Return to continue, CTRL-C to abort." 
#raw_input() # Sorry but you have been removed via EC #2

output = open(to_file, 'w')
output.write(indata)

print "\nAlright, all done."
output.close() # had to move this up from the bottom because it was causing output_read.read to fail

# I am adding this in so I don't have to 'cat ec17-to.txt' each time
output_read = open(to_file, 'r')

print "\nThis is what was copied to %s:" % (to_file)
print output_read.read()

output_read.close()
input.close()

# Extra Credit
# 1: I am researching 'import'. I am then going to start python and see what kind of trouble I can get in. http://docs.python.org/reference/simple_stmts.html#import

#>>> import urllib2
#>>> f = urllib2.urlopen('http://justindorfman.com')
#>>> print f.read(200)
#<!DOCTYPE html><html
#dir="ltr" lang="en-US"><head><link
#rel="stylesheet" type="text/css" href="http://justindorfmancom.jdorfman.netdna-cdn.com/wp-content/w3tc/min/9ff6fb02.9ca8e7.css" media="all" /><s
#######
# if you remove the 200 it will show all of the html. kind of like curl...
# I think I am starting to get this... see 'ex17-ec1.py'

# 2: This script is annoying according to Zed.  I shall remove (comment out) BS.

# 3: See 'ex17-ec2.py'

# 4: I use cat on the daily, along with curl, ssh & dig

# 5: I don't use windows so I can skip this one =)

# 6: output.close saves and closes the file.  If you don't have it in your script (in my case the right place...), it won't save the file.
