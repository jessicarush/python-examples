# REVIEW of Lists, Tuples, Dictionaries & Sets 

# Compare data structures:

colours_list = ['red', 'orange', 'black']
colours_tuple = ('red', 'orange', 'black')
colours_dict = {'red' : 'Pantone 185C' , 'orange' : 'Pantone 021C' , 'black' : 'Pantone 6C'}
colours_set = {'red', 'orange', 'black'}

# in each case use [] brackets to access a single element (except sets which don't support indexing):

print(colours_list[2])
print(colours_tuple[2])
print(colours_dict['black'])

"""
You can combine data structures for example you can make:
 - a tuple of lists
 - a list of lists
 - a dictionary of lists (only the values van be lists)
"""

colors = ['magenta', 'red', 'cyan']
moods = ['happy', 'sad', 'confused']
senses = ['smell', 'touch', 'taste']

dict_of_lists = {
    'Colors' : colors,
    'Moods' : moods,
    'Senses' : senses,
}

"""
Note:
Dictionary keys must be immutable, therefor you cannot use a list or
another dictionary as a key, but you CAN use a tuple because tuples
are immutable too. A good example of this is with mapping... the GPS
coorinates may be the key:
places = {
    (44, -93, 344) : 'home',
    (27, -80, 200) : 'work',
    }
"""