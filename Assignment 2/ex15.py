
# imports the module 'argv' from the 'sys' package
from sys import argv

# assigns two variables to the module argv
script, filename = argv

script = raw_input("script > ")
filename = raw_input("filename > ")

# Calls a function on 'txt' using 'open' to open a file using the file() type.
# It takes a parameter and returns a value to set to the variable 'txt'.
txt = open(filename)

# Print a line that ends with the variable 'filename'.
print "Here's your file %r:" % filename
# Calls a function on txt. The function 'open' returned a file and the dot '.' enables
# the use of a command: read()
print  txt.read()

# Assigns a value with raw_input() function.
print "Type the filename again:"
file_again = raw_input("> ")

# Assigns the input from the user to the variable txt_again and uses the built-in
# function open() to create a file object.
txt_again = open(file_again)

# Uses the command read() to read the file from the users input.
print txt_again.read()

# Important to close files when done with them.
txt.close()
txt_again.close()

txt_lines = open(filename)
lines = txt_lines.readlines()
print lines
txt_lines.close()
#### Study drills

# If you are not sure ask someone for help or search online.
# Many times searching for "python THING" will find answers for what that THING
# does in Python. Try searching for "python open."
#
#   Answer: The OPEN function: Before you can read or write a file, you have to open
#           it using Python's built-in open() function. This function creates a
#           FILE object, which would be utilized to call other support methods
#           associated with it.

# I used the name "commands" here, but they are also called "functions" and "methods."
# Search around online to see what other people do to define these.
# Do not worry if they confuse you. It's normal for programmers to confuse you with
# their vast extensive knowledge.

# Get rid of the part from lines 10-15 where you use raw_input and try the script then.
#   Answer: commented out from 'print "Type the filename again:"' to print txt_again.py
#           Runs fine.

# Use only raw_input and try the script that way. Think of why one way of getting the
# filename would be better than another.
#   Answer: You generally should avoid interactive user input if it's not a key feature.

# Run pydoc file and scroll down until you see the read() command (method/function).
# See all the other ones you can use? Skip the ones that have __ (two underscores)
# in front because those are junk. Try some of the other commands.

# Start python again and use open from the prompt. Notice how you can open
# files and run read on them right there?

# Have your script also do a close() on the txt and txt_again variables.
# It's important to close files when you are done with them.
