# Excercise 17 - http://learnpythonthehardway.org/book/ex17.html

# I am going to write a script that ask for the url you want to 'curl'

import urllib2

print "Hello and Welcome to pyCurl!"
print "Please type in the URL you want to curl:" 
f = raw_input()

u = urllib2.urlopen(f)

print u.read()

