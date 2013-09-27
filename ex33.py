# Moved everything inside definition to scope the variables

def while_function(a):
	numbers = []
	i = 0
	while i < a:
		print "At the top i is %d" % i
		numbers.append(i) # this numbers is the global one

		i += 2
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	return numbers

# Print definition
def print_results(nums):
	print "The numbers: "
	for num in nums:
		print num

# This calls the definition print_results with a parameter that calls
# while_fun(a).
print_results( while_function(6) )
while_function(5)
