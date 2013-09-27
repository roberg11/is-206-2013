from sys import argv

script, input_file = argv

# Definition that reads a file given to the parameter
def print_all(f):
    print f.read()

# Definition that 'seeks' to the start of the file (in bytes) given to parameter
# The method seek() sets the file's current position at the
# offset. The whence argument is optional and defaults to 0,
# which means absolute file positioning, other values are 1
# which means seek relative to the current position and 2 means
# seek relative to the file's end.
def rewind(f):
    f.seek(0)

# Definition taking two parameters that counts the lines in the file
# and reads each line and prints them.
def print_a_line(line_count, f):
    print line_count, f.readline()

# Variable assigned to the method of opening the file given to argument variable
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

## Each time print_a_line is run, you are passing in a variable
## current_line. Write out what current_line is equal to on
## each function call, and trace how it becomes line_count in
## print_a_line.


current_line = 1
# Current line is 1 in this function call
print_a_line(current_line, current_file)

# Current line is 1 + 1 = 2 in this function call
current_line = current_line + 1
print "This is line nr: %r\n" % current_line
print_a_line(current_line, current_file)

# Current line is 2 + 1 = 3 in this function call
current_line = current_line + 1
print "This is line nr: %r\n" % current_line
print_a_line(current_line, current_file)

## Research the shorthand notation += and rewrite the script to use that.

## current_line += 1 is the equivalent of saying current_line = current_line + 1






