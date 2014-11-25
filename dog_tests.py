#!/usr/bin/env python3

""" Testing dogs """

# Import needed packages
import unittest
import read_dogs as rd

# Need to know what I am testing: a class, function...

# Create test subclass(es) of unittest.TestCase ("test fixtures")
class DogClassTest(unittest.TestCase):
    """ Tests whether the dog class is working """

    def test_dogs(self):
        a_dog = rd.Dog("Randy", "Golden Retriever", "Cream", 4)
        self.assertTrue(a_dog)




# Offer external code execution (include all lines below this point in all test files)
def main():
    # Triggers default behavior of running all test fixtures in the file
    unittest.main()

if __name__ == '__main__':
    main()














