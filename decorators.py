'''Decorators'''

# A decorator is a function that takes one function as an input and returns
# another function. Here is a simplified example:

def my_decorator(func):
    def wrapper(arg):
        print('Before {}() is called.'.format(func.__name__))
        func(arg)
        print('After {}() is called.'.format(func.__name__))
    return wrapper

@my_decorator
def squares(n):
    '''returns the square of a number'''
    print(n ** 2)

squares(6)
# Before squares() is called.
# 36
# After squares() is called.

# -----------------------------------------------------------------------------
# @functools.wraps():
# -----------------------------------------------------------------------------
# When you use a decorator, you're replacing one function (squares) with
# another (wrapper). While inside the decorator we can get see the original
# function being used but outside check this out:

print(squares.__name__)  # wrapper
print(squares.__doc__)   # None

# That's why we have functools.wraps. This takes a function used in a decorator
# and adds the functionality of copying over the functions name, docstring,
# arguments list, etc. See the difference:

from functools import wraps

def my_decorator(func):
    @wraps(func)  # Add this, everything else is the same
    def wrapper(arg):
        print('Before {}() is called.'.format(func.__name__))
        func(arg)
        print('After {}() is called.'.format(func.__name__))
    return wrapper

@my_decorator
def squares(n):
    '''returns the square of a number'''
    print(n ** 2)

print(squares.__name__)  # squares
print(squares.__doc__)   # returns the square of a number

# -----------------------------------------------------------------------------
# Returning results
# -----------------------------------------------------------------------------
# The function document_it() below defines a decorator that will:
#  - print the functions name and values of its arguments
#  - run the function with the arguments
#  - print the result
#  - return the modified function for use

def document_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper

# Here's our simple test function, first we'll do it without a decorator:
def add_ints(a, b):
    return a + b

decorated_add_ints = document_it(add_ints)
decorated_add_ints(3,5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

# Now with a decorator... a little less code:
@document_it
def add_ints(a, b):
    return a + b

add_ints(4, 5)
# Running function: add_ints
# Positional arguments: (4, 5)
# Keyword arguments: {}
# Result: 9

# -----------------------------------------------------------------------------
# Multiple decorators
# -----------------------------------------------------------------------------

def square_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

# The decorator that's closest to the actual function (above the def) runs
# first and then the one above that will run. The results will be the same no
# matter what order but the intermediate steps are different. Depending on what
# your decorators do, the order may be important.

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
# Running function: new_function
# Positional arguments: (4, 3)
# Keyword arguments: {}
# Result: 49
# 49

@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(4, 3))
# Running function: add_ints
# Positional arguments: (4, 3)
# Keyword arguments: {}
# Result: 7
# 49

# -----------------------------------------------------------------------------
# @property
# -----------------------------------------------------------------------------
# see decorators used as getter and setter methods in classes.py

# -----------------------------------------------------------------------------
# one last example:
# -----------------------------------------------------------------------------

import time

def timing(func):
    '''Outputs the time a function takes to execute.'''

    @wraps(func)
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1))
    return wrapper

@timing
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)

print(my_function())
# Time it took to run the function: 0.0011439323425292969
