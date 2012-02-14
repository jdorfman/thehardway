# Excercise 30 - http://learnpythonthehardway.org/book/ex30.html

# Defines what each variables value is
people = 30
cars = 40
buses = 15

# Extra Credit 2a.:
#people = 15
#cars = 30
#buses = 40

# Extra Credit 2b.:
#people = 4
#cars = 3
#buses = 10


# if cars are greater than people then print
if cars > people:
    print "We should take the cars. "
# or if (else if) there are more people than cars print 
elif cars < people:
    print "We should not take the cars." # This line will print with 2b. vars
# if none of the statements are true then print:
else:
    print "We can't decide."

# if there are more buses than cars print
if buses > cars:
    print "That's too many buses." # This line will print with 2b. vars
# or if there are more cars than buses print
elif buses < cars:
    print "Maybe we could take the buses."
# if neither statements are true then print:
else:
    print "We still can't decide."

# if there are more people then buses print
if people > buses:
    print "Alright, let's just take the buses." 
# any other statement besides more people than buses print
else:
    print "Fine, Let's just stay home." # This line will print with 2b. vars

# Extra credit 3.:


if people < buses and buses < cars:
    print "This line won't print."
else:
    print "This line will print."

if buses == people or people > cars:
    print "This line won't print."
else:
    print "This line will print."

# Extra Credit:

# 1. Try to guess what elif and else are doing.
# 2. Change the numbers of cars, people, and buses and then trace through each if-statement to see what will be printed.

    # 2a.:
    # We should take the cars. - elif
    # That's too many buses. - if
    # Fine, Let's just stay home. - else


# 3. Try some more complex boolean expressions like cars > people and buses < cars.
# 4. Above each line write an English description of what the line does.

