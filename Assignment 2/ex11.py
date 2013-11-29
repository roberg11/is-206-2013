print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#### Study drills

## Go online and find out what Python's raw_input does.
#   Answer: It presents a prompt to the user. It gets input from
#           the user and returns it in a string. raw_input([arg])
#           Contrary to input([arg]) it doesn't try to interpret the input
#           for the user.

## Can you find other ways to use it? Try some of the samples you find.
#   Answer: 

## Write another "form" like this to ask some other questions.
#   Answer:
print "Dividing the number: ",
initial_number = int(raw_input())
print "Divide the number by: ",
divide_by = int(raw_input())

result = initial_number / divide_by
print "Result: %r" % result

## Related to escape sequences, try to find out why the last line
## has '6\'2"' with that \' sequence. See how the single-quote
## needs to be escaped because otherwise it would end the string?
