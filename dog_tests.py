#!/usr/bin/env python3

""" Testing dogs """

# Import needed packages
import unittest
import read_dogs as rd

# Need to know what I am testing; a class, function...

# Create test subclass(es) of unittest.TestCase ("test fixtures")
class ValidDogClassTest(unittest.TestCase):
	# Tests whether valid dog objects have been successfully created

	# Define some known values that are good


	# Define some known values that are bad


	

	# Define tests
	def test_dogs(self):
		a_dog = rd.Dog("Randy", "Golden Retriever", "Yellow", 4)
		self.assertTrue(a_dog)

	# Test the functions used to verify the validity of the dog data
	def test_check_name(self):
		bad_name_dog = rd.Dog(4, )

	def test_check_breed(self):
		pass

# Offer external code execution (include all lines below this point in all test files)
def main():
	# Triggers default behavior of running all test fixtures in the file
	unittest.main()

if __name__ == '__main__':
	main()