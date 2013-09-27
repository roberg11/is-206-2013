# A dictionary is a data type similar to arrays, but works with keys and  values,
# Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc)
# instead of using its index to address it.

# E.g. a dictionary of phone numbers
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

# Alternatively, a dictionary can be initialized with the same values
# in the following notation.
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

# Iterating over dictionaries
# A dictionary does not keep the order of values stored in it.
for name, number in phonebook.iteritems():
    print "Print number of %s is %d" % (name, number)

# Removing a value use either of the following:
##del phonebook["John"]

# or
##phonebook.pop("John")

phonebook["Jake"] = 938273443
phonebook.pop("Jill")
