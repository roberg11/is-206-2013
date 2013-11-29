
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

## Combine raw_input with argv to make a script that gets more input
## from a user.

fruit = raw_input("Name a fruit: ")
vegetable = raw_input("Name a vegetable: ")

print "The name of the fruit: %r. The name of the vegetable: %r." % (fruit, vegetable)

####    Study drills

## Try giving fewer than three arguments to your script.
## See that error you get? See if you can explain it.
##  Answer: ValueError: need more than 3 values to unpack.
#           Because the script assigns four values to pass the
#           ArgumentValue the program won't run with less or more.

## Write a script that has fewer arguments and one that has more.
## Make sure you give the unpacked variables good names.
#   Answer: 'python ex13.py apple orange' gives the error:
#               ValueError: need more than 3 values to unpack


## Remember that modules give you features. Modules. Modules.
## Remember this because we'll need it later.
