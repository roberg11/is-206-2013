

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
look = "Look over \"here\"."

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print look

##while True:
##    for i in ["/", "-", "|", "\\", "|"]:
##        print "%s\r" % i,

skinny_cat = """
'''asdf'''
asdf
asdf
asdf
"""
print skinny_cat

#### Study drills

#   Memorize all the escape sequences by putting them on flash cards.
#       Answer: Ok.

#   Use ''' (triple-single-quote) instead.
#   Can you see why you might use that instead of """?
#       Answer: The only reason to use triple single-quotation marks
#               is if the sentence contains triple double-quotation marks.
text1 = '''This string contains """ so use triple-single-quotes.'''
text2 = """This string contains ''' so use triple-double-quotes."""

#   Combine escape sequences and format strings to create a more
#   complex format.
#       Answer: 

#   Remember the %r format? Combine %r with double-quote and
#   single-quote escapes and print them out. Compare %r with %s.
#   Notice how %r prints it the way you'd write it in your file,
#   but %s prints it the way you'd like to see it?
#       Answer:
text3 = "I said: %r, and also a %r."  % (tabby_cat, persian_cat)
text4 = "I said: %s, and also %s."  % (tabby_cat, persian_cat)
print text3
print text4


