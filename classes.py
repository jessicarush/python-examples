'''Classes'''

# A string and an integer are examples of built-in Python classes.
# A class is logical grouping of data and functions. The "integer" class is
# like an instruction manual for making integer objects. To make your own
# object, you'll need to first define a class:

class Person():
    pass

# You can create an object from a class (instantiating) by calling it as if it
# were a function:

henry = Person()

# In this case, Person() creates an individual object from the Person class and
# assigns it the name henry.

class Person():
    def __init__(self):
        pass

# The __init__ is a special method that initializes an individual object from
# its class definition. The self argument specifies that it refers to the
# individual object itself. When you define __init__() in a class definition,
# its first parameter should always be self. Although self is not a reserved
# word in Python, it's common usage.

# NOTE: It's NOT necessary to have an __init__ method in every class definition.
# It's used to do anything that's needed to distinguish this object from
# others created from the same class.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

astronaut = Person('Roberta Bondar', 40)
baker = Person('Mrs. Lovett', 35)

# NOTE: the name value passed in is saved with the object as an attribute.
# When a variable is bound to an instance of a class, it's called a data
# attribute. You can read and write this attribute directly by using dot
# notation:

print(astronaut.name)
astronaut.age = 20

# You aren't limited to the attributes set in the class. You can still assign
# new instance variables not present in the class:

baker.friend = 'Todd'

# Data attributes can be obtained in several ways when it comes to working with
# replacement fields. The second example is easier to read.

print('Name {} age {}, name {} age {}'.format(
    astronaut.name, astronaut.age, baker.name, baker.age))

print('Name {0.name} age {0.age}, name {1.name} age {1.age}'.format(
    astronaut, baker))

# Class attributes ------------------------------------------------------------

class Person():

    nationality = 'Canadian'  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class attributes will be available to all instances. Basically if you type
# something like baker.nationality, it will check first in baker for the value,
# if it doesn't fins it there it will look in the class. Note that if you do a
# new assignment for an instance, you are not reassigning the original
# variable, you are creating a new local instance variable with the same name:

baker.nationality = 'British'  # local instance variable

# __dict__ --------------------------------------------------------------------

# A dictionary or other mapping object is used to store an object’s (writable)
# attributes. Use __dict__ to see all the attributes:

print(baker.__dict__)
print(astronaut.__dict__)
print(Person.__dict__)

# Inheritance -----------------------------------------------------------------

# Creating a new class from an existing class, with some additions or changes.
# When you use inheritance, the new class can automatically use all the code
# from the old class without copying any of it. You only define what you need
# to add or change in the new class and this overrides the behavior of the old
# class. The original class is the parent, superclass or base class.
# The new one is the child, subclass or derived class.

class Car():
    pass

class Honda(Car):
    pass

a_car = Car()
a_honda = Honda()

# The object called a_honda is an instance of the class Honda, but it also
# inherits whatever Car can do. Unless there is an override of a parents
# function in the child's:

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

person = Person('Fudd')
doctor = MDPerson('Fudd')

print(person.name)  # Fudd
print(doctor.name)  # Doctor Fudd

# super() ---------------------------------------------------------------------

# If you override a method like __init__ , you can retrieve attributes back
# from the parent using super():

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

# The above could be written like this:

class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email

# But then we would loose our inheritance. If the definition of the parent
# class changes, using super() ensures the child will inherit the changes.

# Another example:

class Enemy():
    def __init__(self, name='Enemy', hp=0, lives=1):
        self.name = name
        self.hp = hp
        self.lives = lives

    def __str__(self):
        return "{0.name} – Lives: {0.lives}, Hit points: {0.hp}".format(self)

class Vampire(Enemy):
        def __init__(self, name):
            super().__init__(name=name, hp=12, lives=3)

# In the above example, we are able to change the default values that were set
# for the base class. Note when creating a vampire object, we will only be able
# to pass in an argument for name. But it will automatically get 12 hit points
# and 3 lives.

bat = Enemy('Batty')
spider = Enemy('Crawly', 10, 1)
spike = Vampire('Spike')

print(bat)      # Batty – Lives: 1, Hit points: 0
print(spider)   # Crawly – Lives: 1, Hit points: 10
print(spike)    # Spike – Lives: 3, Hit points: 12

# Multiple Inheritance and super() --------------------------------------------

class Animal:
  def __init__(self, name):
    print(name, 'is an animal.');

class Mammal(Animal):
  def __init__(self, name):
    print(name, 'is a warm-blooded animal.')
    super().__init__(name)

class NonWingedMammal(Mammal):
  def __init__(self, name):
    print(name, "can't fly.")
    super().__init__(name)

class NonMarineMammal(Mammal):
  def __init__(self, name):
    print(name, "can't swim.")
    super().__init__(name)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self, name):
    print(name, 'has 4 legs.');
    super().__init__(name)

chihuahua = Dog('Chihuahua')
bat = NonMarineMammal('Bat')

# Chihuahua has 4 legs.
# Chihuahua can't swim.
# Chihuahua can't fly.
# Chihuahua is a warm-blooded animal.
# Chihuahua is an animal.
# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.

# Calling methods from a class ------------------------------------------------

# There are a couple of ways to call a method from a class:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True

    def deceased(self):
        self.alive = False

snape = Person('Severus Snape', 38)

# call the method (function) like this:
snape.deceased()
print(snape.alive)

# or like this:
Person.deceased(snape)
print(snape.alive)

# Getter and Setter methods with property() -----------------------------------

# Some object oriented languages support private object attributes that can't
# be accessed from the outside. They have to write getter and setter methods to
# read and write the values on these private attributes. Python doesn't need
# these because all attributes and methods are public. A good way to hide
# attributes is to use property(). The naming convention for hidden attributes
# is __whatever (see documenting_naming.py).

# The property() method returns a property attribute. It makes a method
# (a function in a class) behave like an attribute. This allows us to create a
# read-only attribute of __name.

# The property method take four optional parameters:
# – fget - function for getting the attribute value
# – fset - function for setting the attribute value
# – fdel - function for deleting the attribute value
# – doc - string that contains the docstring for the attribute

# property(fget=None, fset=None, fdel=None, doc=None)

class Person():
    def __init__(self, value):
        self.__name = value

    def getName(self):
        print('Getting name')
        return self.__name

    def setName(self, value):
        print('Setting name to ' + value)
        self.__name = value

    def delName(self):
        print('Deleting name')
        del self.__name

    # Set property to use getName, setName and delName methods
    name = property(getName, setName, delName, 'Name property')


p = Person('Adam')
print(p.name)  # Adam

p.name = 'John'
del p.name

# Getter and Setter methods using decorators ----------------------------------

class Person():
    def __init__(self, value):
        self.__name = value

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name


p = Person('Tim')
print(p.name)  # Tim

p.name = 'Paul'
del p.name

# Uses for Getters and Setters ------------------------------------------------

# While you shouldn't necessarily worry about private attributes in Python,
# getter and setter methods can be useful in situations where you want to set
# up some sort of validation for the values that the data attributes can be set
# to. In the following example, lives is not allowed to be a negative number.

# NOTE: In the previous examples, the data attributes have a slightly different
# name from the property (__name, name) because we were trying to hide the,
# attribute, but it should be pointed out that these names have to be different.

class Player():
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

# Uses for property() ---------------------------------------------------------

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.diameter)  # 10

c.radius = 7
print(c.diameter)  # 14

# c.diameter = 4  # this will raise an AttributeError

# Create a setter to make the diameter method also accept new values:

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0  # best to specify floats when dividing

c = Circle(5)
print(c.diameter) # 10

c.diameter = 20  # now this will also work
print(c.radius)  # 10.0

# Instance methods ------------------------------------------------------------

# Some data(attributes) and functions(methods) are part of the class itself and
# some are part of the objects that are created from that class. When you see
# an initial self argument in methods within a class def, it's an instance
# method. These are the types of methods you normally write. The first
# parameter of an instance method is self. Any change made to the class
# affects all of its objects.

# Class methods ---------------------------------------------------------------

# A class method is a method you can call on the class itself. Use the
# @classmethod decorator to indicate the following function is a class method.
# The first parameter to the method is the class itself: cls ('cls' is used
# because the word class is already taken).

# This class method will count how many objects have been made from it:

class A():
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A")

    @classmethod
    def children(cls):
        print("A has", A.count, "objects made from it.")

# testing:
test1 = A()
test2 = A()
test3 = A()
test4 = A()

A.children()

# NOTE: you can also write class methods outside of classes. You might do this
# if you wanted to create a class method that you could call on many classes.

# Static methods --------------------------------------------------------------

# The third type of method in a class def is a static method. If affects
# neither the class nor its objects. It's just there for convenience. Begin
# with the @static method decorator, no initial self or class parameter:

class A():
    @staticmethod
    def note():
        print('This is a static method')

A.note()


# Review ----------------------------------------------------------------------

# In this example note how the subclasses are using the parents __init__
# method. Because of this we can use the variable self.words in the subclasses.

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'

class Question(Quote):
    def says(self):
        return self.words + '?'

class Exclamation(Quote):
    def says(self):
        return self.words + '!'

person1 = Quote('Bob', 'Hello')
person2 = Question('Bill', 'What')
person3 = Exclamation('Bruce', 'OK')

# testing:
print(person1.who(), ': ', person1.says())  # Bob :  Hello.
print(person2.who(), ': ', person2.says())  # Bill :  What?
print(person3.who(), ': ', person3.says())  # Bruce :  OK!

# Here's another class that has no relation to the previous classes
# (descendants of Quote), but will use the same method names:

class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'

brook = BabblingBrook()

# Now a function that runs the who() and says() methods of any object:

def who_says(obj):
    print(obj.who(), ': ', obj.says())

# testing:
who_says(person1)  # Bob :  Hello.
who_says(person2)  # Bill :  What?
who_says(person3)  # Bruce :  OK!
who_says(brook)    # Brook :  Babble

# An interesting example ------------------------------------------------------

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coordinates: " + str(self.__dict__)

def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)

print(add(one, two))  # Coordinates: {'x': 400, 'y': 400}

# Summary of Terms ------------------------------------------------------------

# Class: template for creating objects. All objects created using the same
# class will have the same characteristics.
# Object: an instance of a class.
# Instantiate: create an instance of a class.
# Method: a function defined in a class.
# Attribute: a variable bound to an instance of a class.

# Classes and Objects versus Modules ------------------------------------------

# Objects are most useful when you need a number of individual instances that
# have similar behavior (methods), but differ in their internal attributes.
# Classes support inheritance, modules don't.
# If you want only one of something, a module might be best. No matter how many
# times a Python module is referenced in a program, only one copy is loaded.
# If you have a number of variables that contain multiple values and can be
# passed as arguments to multiple functions, it might be better to define them
# as classes. For example, you might use a dictionary with keys size and color
# to represent an image. You could create a different dictionary for each image
# in your program, and pass them as arguments to functions such as scale() or
# transform(). This can get messy as you add more keys and functions.
# It's simpler to define an Image class with attributes size or color and
# methods scale() and transform(). Then, all the data and methods for a color
# image are defined in one place. Use the simplest solution to the problem.
# A dict, list, or tuple is simpler, smaller, and faster than a module, which
# is usually simpler than a class.
