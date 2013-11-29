# Modules are simply Python files with .py extension, which implements a set
# of functions. Modules are imported from other modules using
# "import" command.

# The first time a module is loaded into a running a script, it is
# initialized by executing the code in the module once. If another
# module in your code imports the same module again, it will not be
# loaded twice but once only - so local variables inside the module
# act as a "singleton" - they are initialized only once.

# To import module "urllib" which enablees us to create read data
# from URLs.

# import the library
import urllib

# use it
##urllib.urlopen(...)

# To read about a function in the module we want: Use "help" function
# inside Python interpreter:
help(urllib.urlopen)

#### Writing modules
# To create a module of your own, simply create a new .py file
# with the module name and then import using the Python file name
# without .py extension using import command

#### Writing packages

# Packages are namespaces which contain multiple packages and
# modules themselves. The are simply directories, but with a twist.

# Each package in Python is a directory which !!MUST!! contain
# a special file called __init__.py. This file can be empty, and
# it indicates that the directory it contains is a Python package,
# so it can be imported the same way a module can be imported.

# If we create a directory called 'foo', which marks the package name
# we can then create a module inside that package called 'bar'.
# We also must not forget to add the __init__.py file inside the
# 'foo' directory.

# To use the module 'bar', we can import it in two ways:
# Must use the 'foo' prefix whenever we access the module 'bar'.
####import foo.bar

# or
# We import the module to our module's namespace.
####from foo import bar

# The __init__.py file can also decide which modules the package
# exports as the API, while keeping other modules internal, by
# overriding the __all__ variable, like so:
##__init__.py:
##
##__all__ = ["bar"]

#### Exercise
# In this exercise, you will need to print an alphabetically
# sorted list of all functions in the re module,
# which contain the word find.

import re

result = []
for x in dir(re):
    if x[:4] == "find":
        result.append(x)
print result

# 
