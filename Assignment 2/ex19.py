# Definition that takes two parameters.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # String using cheese_count parameter from def
    print "You have %d cheeses!" % cheese_count
    # String using boxes_of_crackers parameter from def
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Gives a value to each parameter in def cheese_and_crackers
print "We can just give the funtion numbers directly:"
cheese_and_crackers(20, 30)

# Assigns the value of two variables to the two parameters of
# the definition.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Gives a value to each variable using math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Combines variables and math to the parameters of the definition
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

