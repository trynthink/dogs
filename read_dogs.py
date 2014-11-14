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

# def dog_unserialize(q):
#     # strip off name with pop
#     # name = q.pop('Name') # no default given, will throw KeyError if no name is provided in the object definition
#     cls = dog
#     obj = cls.__new__(cls) # new instance
#     for key, value in q.items():
#         setattr(obj, key, value)
#         return obj

# Define exceptions for Dog objects
class DogError(Exception): pass
class NotStringError(DogError): pass
class InvalidAgeError(DogError): pass
class NotNumericError(DogError): pass
class InvalidColorError(DogError): pass

# Define Dog object validation functions
def check_dog_name(dog):
	""" Check that an acceptable name is given to a dog """
	if not isinstance(dog["Name"], str):
		raise NotStringError, "Dog name entered is not a string"

def check_dog_breed(dog):
	""" Check that an acceptable breed is given for a dog """
	is not isinstance(dog["Breed"], str):
		raise NotStringError, "Dog breed entered is not a string"

def check_dog_color(dog):
	""" Check that an acceptable color is provided for a dog """
	colors = ["White", "Black", "Brown", "Sable", "Gray", "Fawn", "Cream"]
	
	if not isinstance(dog["Color"], str):
	for color in dog["Color"]:
		# STOPPED HERE

def check_dog_age(dog):
	pass



# jsfl = open('dogs.json') # open database of measures

# data = json.load(jsfl, object_hook=dog_unserialize) # object_hook returns dict, object_pairs_hook returns list of tuples

# jsfl.close() # close JSON file

# Validate imported dogs



if __name__ == '__main__':
    main()

#####################

#x = json.loads('[{"__type__": "User", "name": "Dave Johnson", "username": "djohnson"},{"__type__": "User", "name": "John Smith", "username": "jsmith"}]', object_hook=object_decoder)