the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# Starts at 0 and does 6 counts. 0, 1, 2, 3, 4, 5
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# You can avoid the loop by using
elements_without_loop = range(0, 6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

#### Study drills

    # Take a look at how you used range. Look up the range function to understand it.
## range(stop) -> list of integers
## range(start, stop[, step]) -> list of integers
## Return a list containing an arithmetic progression of integers.


    
    # Other operations on lists:
##append(...)
##    L.append(object) -- append object to end
##
##count(...)
##    L.count(value) -> integer -- return number of occurrences of value
##
##extend(...)
##    L.extend(iterable) -- extend list by appending elements from the iterable
##
##index(...)
##    L.index(value, [start, [stop]]) -> integer -- return first index of value.
##    Raises ValueError if the value is not present.
##
##insert(...)
##    L.insert(index, object) -- insert object before index
##
##pop(...)
##    L.pop([index]) -> item -- remove and return item at index (default last).
##    Raises IndexError if list is empty or index is out of range.
##
##remove(...)
##    L.remove(value) -- remove first occurrence of value.
##    Raises ValueError if the value is not present.
##
##reverse(...)
##    L.reverse() -- reverse *IN PLACE*
##
##sort(...)
##    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
##    cmp(x, y) -> -1, 0, 1
