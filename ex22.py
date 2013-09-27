# Word/character print. Multiline, single-quote, double-quote
print "Hello World"
print 'Hello World'
print """
Hello World
Hello World again
Hello World again and again
"""

# Math symbols +-/*

print 25 + 30 / 6 * 3 - 5

# Boolean characters < > == != <= >=

print 5 == 4
print 5 != 4
print 5 < 4
print 5 > 4
print 5 <= 4
print 5 >= 4

# Floating numbers

print 5.0 * 4
print 5.9 + 13.43

# Variables and format string '%r %s'

cars = 100
space_in_car = 4.0

print "Total space in cars is %r" % (cars * space_in_car)

# String inside string

binary = "binary"
do_not = "don't"
string1 = "Those who know %s and those who %s." % (binary, do_not)
print string1
print "Its fleece was white as %s." % 'snow'

# String and math
print "." * 10

# More string format
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("up", "down", "left", "right")

# Newline string \n
fruits = "\nApple\nOrange\nGrapefruit\nBanana"
print "Available fruits today: ", fruits

# Tabbed strings
tabby_cat = "\tThe tabbed cat."

# raw_input() Input from user into a variable
##age = raw_input()
##height = raw_input()
##weight = raw_input()
##
##print "So, you're %r, %r tall and %r heavy." % (
##    age, height, weight)













