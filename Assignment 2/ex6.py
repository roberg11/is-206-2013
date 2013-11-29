# String where %d variable is determined as 10
x = "There are %d types of people." % 10
# Simple string 1
binary = "binary"
# Simple string 2
do_not = "don't"
# String combining Simple string 1 & 2 to %s and %s variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints variable x where %d variable equals 10
print x
# Prints variable y where 2 strings are bound to %s and %s
print y

# Prints %r variable as x string and shows it inside ' characters.
print "I said: %r." % x
# Prints '%s' in the same way as %r regardless of ' characters.
print "I also said: '%s'." % y

# Boolean variable put to False
hilarious = False
# String with unassigned %r variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints joke_evaluation string and assigns %r variable to boolean variable
print joke_evaluation % hilarious

# Simple string 3
w = "This is the left side of..."
# Simple string 4
e = "a string with a right side."

# Combines simple string 3 and 4 into one printable string.
print w + e

### Study drills

#   Go through this program and write a comment
#   above each line explaining it.
#       Answer: see above

#   Find all the places where a string is put inside a string.
#   There are four places.
#       Answer: There are 6 places.
#                   1. x = %d % 10
#                   2. y = %s & %s % (binary, do_not)
#                   3. "I said: %r." % x 
#                   4. "I also said: 's%'." % y
#                   5. print joke_evaluation % hilarious
#                   6. print w + e

#   Are you sure there are only four places?
#   How do you know? Maybe I like lying.
#       Answer: There are 6 places, stop lying!

#   Explain why adding the two strings w and e with + makes
#   a longer string.
#       Answer: String concatenation. Python takes the first part and
#               adds it to the second part. Because it's not mathematical
#               python interprets the strings separately and adds them together to one string.


