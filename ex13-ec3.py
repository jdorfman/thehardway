from sys import argv

script, arg1 = argv

name = raw_input("Name please: ")

print "Thanks %r for typing %r before running %r. If you didn't there would be mayhem!" % (name, arg1, script)
