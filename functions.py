'''Functions, parameters and arguments'''

# Write a function with def() -------------------------------------------------

# Function names can start with letters or _ and contain only letters, numbers
# and _. Pass means do noting but move on. It's a placeholder.
# NOTE: it's good practice to put two spaces after each function definition,
# unless they're nested inside another function or class.

def myfunction(num1, num2): # num1, num2 are parameters
    pass

# Call the function() --------------------------------------------------------

myfunction(1, 2) # 1, 2 are arguments

# Reminder: return vs print --------------------------------------------------

def myfunction1(num1, num2):
    print(num1 * num2) # prints the result but returns None

def myfunction2(num1, num2):
    return num1 * num2 # prints nothing but returns the result

# example:
def heading(arg):
    print('{0:-^80}'.format(str(arg).title()))

heading('Positional Arguments')

# Positional Arguments -------------------------------------------------------

def menu(wine, cheese, dessert):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print(menu('chardonnay', 'cake', 'swiss'))

# Keyword Arguments ----------------------------------------------------------

print(menu(wine='chardonnay', dessert='cake', cheese='swiss'))

# Default Parameters ---------------------------------------------------------

def menu(wine, cheese, dessert='ice cream'):
    return {'wine': wine, 'cheese': cheese, 'dessert': dessert}

print (menu(wine='chardonnay', dessert='cake', cheese='swiss'))
print (menu(wine='chardonnay', cheese='swiss'))

# Example of local vs parameter set value ------------------------------------

# In this example the function is expected to run each time with a fresh empty
# result list, add the arg argument to it, and then print a single-item list.
# However, it's only empty the first time it's called. The second time, result
# still has one item from the previous call.

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')  # ['a']
buggy('b')  # ['a', 'b']
buggy('new list', ['hello', 'hello'])  # ['hello', 'hello', 'new list']

# This works better to have an empty list each time:

def works(arg):
    result=[]
    result.append(arg)
    print(result)

works('a')  # ['a']
works('b')  # ['b']

# Or fix the first one by passing in something else to indicate the first call:
# This whole example seems a bit semantic to me but perhaps it will be useful
# later on:

def nonbuggy(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)

nonbuggy('a')  # ['a']
nonbuggy('b')  # ['b']
nonbuggy('new list', ['hello', 'hello'])  # ['hello', 'hello', 'new list']

# Gather Positional Arguments with * -----------------------------------------

# The * operator used when defining a function means that any extra positional
# arguments passed to the function end up in the variable prefaced with the *
# which will be a tuple.

def print_args(*args):
    print(args, type(args))

print_args(1, 2, 3, 'hello')  # (1, 2, 3, 'hello') <class 'tuple'>
print_args(1)                 # (1,) <class 'tuple'>

# The * operator can also be used when calling functions and here it means the
# analogous thing. A variable prefaced by * when calling a function means that
# the variable contents should be extracted and used as positional arguments.

def add(x, y):
    return x + y

nums = [13, 7]
add(*nums)  # returns 20

# This example uses both methods at the same time:

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

nums = [13, 7, 10, 40, 30]
add(*nums)  # returns 100

# You can have required and optional parameters. The required ones come first:

def print_more(required1, required2, *args):
    print('first argument is required:', required1)
    print('second argument is required:', required2)
    print('the rest:', args)

print_more('red', 'green')
# first argument is required: red
# second argument is required: green
# the rest: ()

print_more('red', 'green', 'one', 'two', 'three
# first argument is required: red
# second argument is required: green
# the rest: ('one', 'two', 'three')


# Gather Keyword Arguments with ** -------------------------------------------

# ** does for dictionaries & key/value pairs exactly what * does for iterables
# and positional parameters demonstrated above. Here's it being used in the
# function definition:

def print_kwargs(**kwargs):
    print(kwargs, type(kwargs))

print_kwargs(x=1, y=2, z='hi')  # {'x': 1, 'y': 2, 'z': 'hi'} <class 'dict'>

# And here we're suing it in the function call:

def add(x, y):
    return x + y

nums = {'x': 13, 'y': 7}
add(**nums)  # returns 20

# And here we're using it in both places"

def print_kwargs(**kwargs):
    for key in kwargs:
        print(key, 'in french is', kwargs[key])

colours = {'red': 'rouge', 'yellow': 'jaune', 'green': 'vert', 'black': 'noir'}

print_kwargs(**colours)
# red in french is rouge
# yellow in french is jaune
# green in french is vert
# black in french is noir

# see also terminology.py for another example that feeds dictionary values to
# a class instance.

# Docstrings -----------------------------------------------------------------

def myfunction1(arg):
    '''this is where you can provide a brief description of the function'''
    print(arg)

def myfunction2(arg):
    '''
    This lets
    you
    do
    a *longer*
    description
    '''
    print(arg)

print(myfunction1.__doc__)
print(myfunction2.__doc__)

# Functions as Arguments -----------------------------------------------------

# Functions are objects, just like numbers, strings, tuples, lists,
# dictionaries, etc. They can be assigned to variables, used as arguments to
# other functions, or returned from other functions.

def answer():
    print(100)

def run_something(func):
    func()

run_something(answer)

# The parameter names arg1 and arg2 don't need to match those in the following
# function, just using those names as examples:

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 10)

# An example with a variable number of arguments:

def sum_args(*args):
    print(sum(args))

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 2, 3, 1, 4)

# Nested functions ------------------------------------------------------------

# This is pretty straight forward. When we call the outer() function it in
# turn calls the inner function. The inner function used a variable x that's
# defined in the outer functions namespace. The inner function looks for x
# first in its own local namespace, then failing that looks in the surrounding
# namespace. If it didn't find it there, it would check the global namespace
# next (see namespaces.py).

def outer():
    x = 1
    def inner():
        print(x)
    inner()

outer()  # 1

# Closure --------------------------------------------------------------------

# Consider that the namespace created for our functions are created from
# scratch each time the function is called and then destroyed when the
# function ends. According to this, the following should not work.

def outer():
    x = 1
    def inner():
        print(x)
    return inner

a = outer()
print(outer)  # <function outer at 0x1014a3510>
print(a)      # <function outer.<locals>.inner at 0x100762e18>

# At first glance, since we are returning inner from the outer function and
# assigning it to a new variable, that new variable should no longer have
# access to x because x only exists while the outer function is running.

a()  # 1

# But it does work because of a special feature called closure. An inner
# function knows the value of x that was passed in and remembers it. The line
# return inner returns this specialized copy of the inner function (but
# doesn't call it). That's a closure... a dynamically created function that
# remembers where it came from.

def outer(x):
    def inner():
        print(x)
    return inner

a = outer(2)
b = outer(3)

a()  # 2
b()  # 3

# From this example you can see that closures - the fact that functions
# remember their enclosing scope - can be used to build custom functions that
# have, essentially, a hard coded argument. We aren’t passing the numbers
# to our inner function but are building custom versions of our inner function
# that "remembers" what number it should print.


# lambda() -------------------------------------------------------------------

# The lambda function is an anonymous function expressed as a single statement
# Use it instead of a normal tiny function.

def edit_story(words, func):
    for word in words:
        print(func(word))

sounds = ['thud', 'hiss', 'meow', 'tweet']

def headline(testing):
    return testing.capitalize() + '!'

edit_story(sounds, headline)

# Using lambda, the headline function can be replaced this way:

edit_story(sounds, lambda word: word.capitalize() + '!')