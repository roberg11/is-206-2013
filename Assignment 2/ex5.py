name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's hot too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %r, and %d I get %d." % (
    age, height, weight, age + height + weight)

### Study drills

#   Change all the variables so there isn't the
#   my_ in front. Make sure you change the name everywhere,
#   not just where you used = to set them.
#       Answer: See above


#   Try more format characters. %r is a very useful one.
#   It's like saying "print this no matter what."
#       Answer: Changed print nr 2 to %r and print nr 7 to "%d, %r, and %d I get %d"

#   Search online for all of the Python format characters.
#       Answer:
#               'd' & 'i' Signed integer decimal
#               'o' Signed octal value
#               'u' Obsolete type - it is identical to 'd'
#               'e' Floating point exponential format(lowercase)
#               'f' Floating point decimal format
#               'c' Single character (accepts integer or single character string)
#               'r' String (converts any Python object using repr())
#               's' String (converts any Python object using str())
#               '%' No argument is converted, results in a '%' character in the result.

#   Try to write some variables that convert the inches and
#   pounds to centimeters and kilos.
#   Do not just type in the measurements.
#   Work out the math in Python.
#       Answer:

inches_to_centimeters = 2.54
pounds_to_kilos = 0.453592

print "If he's %d inches tall, he's also %d centimeters tall." % (height, inches_to_centimeters * height)
print "If he weighs %d pounds, he also weighs %d kilograms." % (weight, pounds_to_kilos * weight)
