# Number of cars available
cars = 100
#Space available in each car
space_in_car = 4.0
# Number of drivers for the cars
drivers = 30
# Number of passengers in need to be transferred
passengers = 90
# Number of cars which doesn't have any drivers
cars_not_driven = cars - drivers
# number of cars that has a driver
cars_driven = drivers
# Number of people who can be transported
carpool_capacity = cars_driven * space_in_car
# Average of passengers that can be put in each car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, " people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", average_passengers_per_car, " in each car."

### Study drills ###

# 1: I used 4.0 for space_in_a_car, but is that necessary?
#       What happens if it's just 4?
#       Answer: The result returns 120.0 and 120 with just '4'.
#               It is not necessary for that specific calculation

# 2: Remember that 4.0 is a "floating point" number. Find out what that means.
#       Answer: In computing, floating point describes a
#               method of representing an approximation of a real number
#               I.E.: 4.0 instead of just 4.

# 3: Write comments above each of the variable assignments.
#       See above

# 4: Make sure you know what = is called (equals) and
#    that it's making names for things.
#       Answer: '=' Assigns a value to the right to the variable name to the left.

# 5: Remember that _ is an underscore character.
#       Answer: And not a 'space', got it!

# 6: Try running python as a calculator like you did before and
#    use variable names to do your calculations.
#    Popular variable names are also i, x, and j.

i = 4
x = 5
j = 6

# z = 4 * 5 = 20
z = i * x
print z
# y = (6 + 4) / 5 = 2
y = (j + i) / x
print y

