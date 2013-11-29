# Creates variables called formatter
formatter = "%r %r %r %r"

# prints variable formatter and passes it to different inputs
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you  could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

### Study drills

#   Do your checks of your work, write down your
#   mistakes, and try not to make them on
#   the next exercise.
#       Answer: Ok.

#   Notice that the last line of output uses both
#   single-quotes and double-quotes for individual
#   pieces. Why do you think that is?
#       Answer: Line 9 has a single quote ( ' ) in it.
#               So to preserve the string it needs double quotation marks
#               to preserve the string.
