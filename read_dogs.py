#!/usr/bin/env python3

""" Import JSON dogs data file to python """

# Import needed packages
import json

# Define Dog class to be used with the imported JSON file
class Dog:
    """ Dog class """
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

# WHEN IMPORTING, WHAT ABOUT ERRORS FROM INCOMPLETE OBJECTS (ENTRIES)?

# Define what to do with the objects in the JSON file
def dog_unserialize(q):
    # strip off name with pop
    # name = q.pop('Name') # no default given, will throw KeyError if no name is provided in the object definition
    cls = Dog
    obj = cls.__new__(cls) # new instance
    for key, value in q.items():
        setattr(obj, key, value)
    return obj

# Open database of measures
jsfl = open('dogs.json')

# Load data from database
data = json.load(jsfl, object_hook=dog_unserialize) # object_hook returns dict, object_pairs_hook returns list of tuples

jsfl.close() # close JSON file

# Validate imported dogs



if __name__ == '__main__':
    main()

#####################

#x = json.loads('[{"__type__": "User", "name": "Dave Johnson", "username": "djohnson"},{"__type__": "User", "name": "John Smith", "username": "jsmith"}]', object_hook=object_decoder)