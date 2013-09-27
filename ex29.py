dogs = 20
people = 30
cats = 15

# If cats is more than people print message
if people < cats:
    print "Too many cats! The world is doomed!"

# If cats is less than people print message
if people > cats:
    print "Not many cats! The world is saved!"

# If people is less than dogs, print message
if people < dogs:
    print "The world is drooled on!"

# If people is more than dogs, print message
if people > dogs:
    print "The world is dry!"

# Adds 5 to variable dogs ( 15 + 5 )
dogs += 5

# If people is greater than or equal to dogs, print message
if people >= dogs:
    print "People are greater than or equal to dogs."

# If people is less than or equal to dogs, print message
if people <= dogs:
    print "People are less than or equal to dogs."

# If people and dogs is the same, print message
if people == dogs:
    print "People are dogs."

# If the body of the if-statement is not indented it is not
# considered as a part of the if-statement

# Can you put other boolean expressions from Exercise 27 in the if-statement?

if people == dogs or dogs > cats:
    print "Either people are dogs or dogs dominate cats."

if people < dogs:
    print "The world is drooled on!"
elif people == dogs:
    print "People are dogs."
else:
    print "People are greater than dogs."

