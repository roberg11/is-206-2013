
from sys import argv

script, user_name, country = argv
prompt = 'Ummm... '

print "Hi %s, I'm the %s script, and I will take you to %s." % (user_name, script, country)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "So %s is in %s" % (lives, country)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Allright, so you said %r about liking me.
You live in %r. Not sure where that is,
but I'm sure it's in %r.
And you have a %r computer. Nice.
""" % (likes, lives, country, computer)

#### Study drills

# Find out what Zork and Adventure were. Try to find a copy and play it.

# Change the prompt variable to something else entirely.
#   Answer: Changed to 'Umm...'

# Add another argument and use it in your script.
#   Answer: added country to the argument

# Make sure you understand how I combined a """ style
# multiline string with the % format activator as the last print.
