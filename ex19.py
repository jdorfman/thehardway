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
cheese_and_crackers(cheese_count, boxes_of_crackers)


print "We can even do math inside:"
cheese_and_crackers(30 + 30, 40 + 90)

print "We can combine the two, variables and math:"
cheese_and_crackers(cheese_count + 30, boxes_of_crackers + 50)

# Extra Credit:
# 1: Comment above each line explaining what is happening in English
