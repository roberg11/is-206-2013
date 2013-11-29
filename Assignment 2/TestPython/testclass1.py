# Objects are and encapsulation of variables
# and functions into a single entit. Objects get their
# variables and functions from classes. Classes are
# essentially a template to create your objects.


# Basic class
class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."

# Variable myobjectx holds an object of the class
# "MyClass" that contains the variable and the
# function defined within the class called "MyClass".
myobjectx = MyClass()

# To access the variable inside the object "MyObject"
myobjectx.variable

# To print the string inside variable
print myobjectx.variable

# You can create multiple objects from the same class
# (have the same variables and functions defined).
# Each object contains independent copies of
# variables defined in the class. For instance:
# Define another object with the "MyClass"
# and change the string in the variable:
myobjecty = MyClass()
myobjecty.variable = "yackity"

# Print both values:
print myobjectx.variable # Print "blah"
print myobjecty.variable # Print "yackity"

# Access a function inside an object
myobjectx.function() # Prints "This is a message inside..."

# Class defined for vehicles

#define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00 
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
#your code goes here
MyCar1 = Vehicle()
MyCar1.name = "Fer"
MyCar1.kind = "convertible"
MyCar1.color = "red"
MyCar1.value = 60000.00

MyCar2 = Vehicle()
MyCar2.name = "Jump"
MyCar2.kind = "van"
MyCar2.color = "blue"
MyCar2.value = 10000.00


#checking code
print MyCar1.description()
print MyCar2.description()

