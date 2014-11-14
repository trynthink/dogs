#!/usr/bin/env python3

""" Testing dogs """

# Import needed packages
import unittest
import read_dogs as rd

# Need to know what I am testing: a class, function...

# Create test subclass(es) of unittest.TestCase ("test fixtures")
class DogClassTest(unittest.TestCase):
	# Tests whether the dog class is working
	def test_dogs(self):
		a_dog = rd.Dog("Randy", "Golden Retriever", "Yellow", 4)
		self.assertTrue(a_dog)



class DogValidationTests(unittest.TestCase):
	# Tests validity checks for Dog instances

	# Define some known dogs that are good
	good_dogs = (rd.Dog("Picard", "Yorkshire Terrier", ["Brown", "White", "Black"], 4),
				 rd.Dog("Riker", "Alaskan Malamute", "Gray", 8),
				 rd.Dog("Geordi", "Boxer", "Brown", 3))

	# Define some known dogs that are bad
	bad_dogs = (rd.Dog("Anakin", 3, ["Green", "Blue", "Red"], "six"),
				 rd.Dog(8, (5, 6, 2), "Gray", 12),
				 rd.Dog("Boxer", "Brown", 3, 5))
		# Wrong type in any category
		# Breed not on list of acceptable breeds
		# Color not on list of acceptable colors

	# Define tests for the Dog instance validity check functions
	def test_validate_name(self):
		for dog in self.good_dogs:
			self.assertTrue(rd.validate_name(dog))

		for dog in self.bad_dogs:
			self.assertFalse(rd.validate_name(dog))

	def test_validate_breed(self):
		for dog in self.good_dogs:
			self.assertTrue(rd.validate_breed(dog))

		for dog in self.bad_dogs:
			self.assertFalse(rd.validate_breed(dog))

	def test_validate_color(self):
		for dog in self.good_dogs:
			self.assertTrue(rd.validate_color(dog))

		for dog in self.bad_dogs:
			self.assertFalse(rd.validate_color(dog))

	def test_validate_age(self):
		for dog in self.good_dogs:
			self.assertTrue(rd.validate_age(dog))

		for dog in self.bad_dogs:
			self.assertFalse(rd.validate_age(dog))



# Offer external code execution (include all lines below this point in all test files)
def main():
	# Triggers default behavior of running all test fixtures in the file
	unittest.main()

if __name__ == '__main__':
	main()


















