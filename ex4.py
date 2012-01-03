# Exercise no 4 - http://learnpythonthehardway.org/book/ex4.html

# cars is the variable and 100 is the value
cars = 100
# a variable with a 'floating point' number:
space_in_a_car = 4.0 #4.0
drivers = 30
passengers = 90
# this variable will show how many care are available to drive
cars_not_driven = cars - drivers
cars_driven = drivers
# This will calculate how many people can currently car pool 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
# 90 / 30
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available." 
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Extra Credit
# Mistake: NameError: name 'car_pool_capacity' is not defined
# Because the variable has an extra underscore '_' in carpool, it should be carpool_capacity.
# 1: 4.0 is used because we need the exact number of space in the car, not something rounded off. The floating point will give us an accurate count.
# 2: In computing, floating point describes a method of representing real numbers in a way that can support a wide range of values. Wikipedia
# 3: I wrote comments above the var assignments
# 6:
# jdorfman@jd:~/github/python/thehardway$ python
# Python 2.6.6 (r266:84292, Sep 15 2010, 15:52:39) 
# [GCC 4.4.5] on linux2
# >>> x = 1
# >>> i = 2
# >>> x + i
# 3



