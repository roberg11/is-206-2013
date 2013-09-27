# Generators are used to create iterators, but with a different
# approach. Generators are simple functions which return an
# iterable set of items, one at a time, in a special way.

# When an iteration over a set of item starts using the
# for statement, the generator is run. Once the generator's function
# code reaches a "yield" statement, the generator yields its
# execution back to the for loop, returning a new value from the
# set. The generator function can generate as many values
# (possibly infinite) as it wants, yielding each one in its turn.

# Example of a generator function which returns 7 random integers.
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number

#### Exercise

# Write a generator function which returns the Fibonacci series.
# The first two numbers of the series is always equal to 1,
# and the consecutive number returned is the sum of the last
# two numbers.

def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def Fib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur
for i in Fib(10, 200):
    print i
