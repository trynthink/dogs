#!/usr/bin/env python3

""" Import JSON dogs data file to python """

# Import needed packages
import json

class Dog:
    """ Dog class """
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

# def dog_unserialize(q):
#     # strip off name with pop
#     # name = q.pop('Name') # no default given, will throw KeyError if no name is provided in the object definition
#     cls = dog
#     obj = cls.__new__(cls) # new instance
#     for key, value in q.items():
#         setattr(obj, key, value)
#         return obj

# jsfl = open('dogs.json') # open database of measures

# data = json.load(jsfl, object_hook=dog_unserialize) # object_hook returns dict, object_pairs_hook returns list of tuples
#     # create new instance of class dog for each dict/object in JSON file
#     # each instance should be named self.name

# jsfl.close() # close JSON file

if __name__ == '__main__':
    main()

#####################

#x = json.loads('[{"__type__": "User", "name": "Dave Johnson", "username": "djohnson"},{"__type__": "User", "name": "John Smith", "username": "jsmith"}]', object_hook=object_decoder)