## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## Dog object inheriteded from Animal class
        ## has-a name.
        self.name = name

## Cat is-a(n) Animal. Inherits and animal object.
class Cat(Animal):

    def __init__(self, name):
        ## Cat object has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person object has a name of some kind.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person. Inherits from Person class.
class Employee(Person):

    def __init__(self, name, salary):
        ## Super lets you avoid referring to the Person class
        ## explicitly. Meaning you don't have to name the Person
        ## class to inherit from it.
        ## Employee is-a person object. Employee has-a name.
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-aPerson
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## Frank is-a Employee and has-a salary
frank = Employee("Frank", 120000)

## frank object has-a pet named Rover
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## crouse is-a salmon which is-a fish
crouse = Salmon()

## harry is-a halibut which is-a fish
harry = Halibut()
