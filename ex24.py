# Excercise 24 - http://learnpythonthehardway.org/book/ex24.html

print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from institution
and requires an explanation
\n\t\t where there is none.
"""

print "-----------"
print poem
print "-----------"

five = 10 - 2 + 3 - 6
print "This should be five: %d" % (five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000 # first run, forgot the 4th 0 and had '0 crates' on the last line.
beans, jars, crates = secret_formula(start_point)
# ^--- I found that confusing because in the funtion it was "jelly_beans"

print "With this start point of %d" % (start_point)
print "We would have %d beans %d jars and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it this way:"
print "We have %d beans %d jars and %d crates" % secret_formula(start_point)

# Extra Credit
# 1. Make sure to do your checks: read it backwards, read it out loud, put comments above confusing parts.
# 2. Break the file on purpose, then run it to see what kinds of errors you get. Make sure you can fix it.
