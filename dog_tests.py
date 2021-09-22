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


class CheckDogNameTests(unittest.TestCase):
    """ Tests validity checking of names for Dog instances """

    # Create some sample objects that should fail under various tests
    num = 4
    str_list = ["something", "or", "other"]
    str_tuple = ("something", "or", "other")
    str_dict = {"component": "result"}

    def test_dog_name_is_not_a_number(self):
        """ Check that a numeric dog name fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_name, self.num)

    def test_dog_name_is_not_a_list(self):
        """ Check that a list of dog names fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_name, self.str_list)

    def test_dog_name_is_not_a_tuple(self):
        """ Check that a tuple of dog names fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_name, self.str_tuple)

    def test_dog_name_is_not_a_dict(self):
        """ Check that a dict with dog names fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_name, self.str_dict)


class CheckDogBreedTests(unittest.TestCase):
    """ Tests validity checking of breeds for Dog instances """

    # Create some sample objects that should fail under various tests
    num = 4
    str_list = ["something", "or", "other"]
    str_tuple = ("something", "or", "other")
    str_dict = {"component": "result"}

    def test_dog_breed_is_not_a_number(self):
        """ Check that a numeric dog breed fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_breed, self.num)

    def test_dog_breed_is_not_a_list(self):
        """ Check that a list of dog breeds fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_breed, self.str_list)

    def test_dog_breed_is_not_a_tuple(self):
        """ Check that a tuple of dog breeds fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_breed, self.str_tuple)

    def test_dog_breed_is_not_a_dict(self):
        """ Check that a dict with dog breeds fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_breed, self.str_dict)


class CheckDogColorTests(unittest.TestCase):
    """ Tests validity checking of color(s) for Dog instances """

    # Create some sample objects that should fail under various tests
    color = "Blue"
    color_list = ["Blue", "Black", "Brown"]
    case_color = "brown"
    num = 4
    str_tuple = ("something", "or", "other")
    str_dict = {"component": "result"}

    def test_dog_color_is_valid(self):
        """ Check that invalid colors fail """
        self.assertRaises(rd.InvalidColorError, rd.check_dog_color, self.color)

    def test_dog_colors_are_valid(self):
        """ Check that a list with an invalid color fails """
        self.assertRaises(rd.InvalidColorError, rd.check_dog_color, self.color_list)

    def test_dog_color_is_case_independent(self):
        """ Check that a color is not rejected due to case sensitivity """
        self.assertTrue(rd.check_dog_color(self.case_color))

    def test_dog_color_is_not_a_number(self):
        """ Check that a number for the dog color fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_color, self.num)

    def test_dog_color_is_not_a_tuple(self):
        """ Check that a tuple of dog colors fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_color, self.str_tuple)

    def test_dog_name_is_not_a_dict(self):
        """ Check that a dict fails """
        self.assertRaises(rd.NotStringError, rd.check_dog_color, self.str_dict)


class CheckDogAgeTests(unittest.TestCase):
    """ Tests validity checking of age for Dog instances """

    # Might also need to test for list, tuple, dict types
    num_list = [7, 3, 10]
    num_tuple = (7, 3, 10)
    num_dict = {"one": 1, "two": 2, "three": 3}

    def test_dog_age_is_not_a_string(self):
        """ Check that age is not a string """
        self.assertRaises(rd.NotNumericError, rd.check_dog_age, "five")

    def test_dog_age_is_not_too_large(self):
        """ Check that an unrealistic age fails """
        self.assertRaises(rd.InvalidAgeError, rd.check_dog_age, 25)

    def test_dog_age_is_not_negative(self):
        """ Check that a negative age fails """
        self.assertRaises(rd.InvalidAgeError, rd.check_dog_age, 0)

    def test_dog_age_is_not_zero(self):
        """ Check that an age of zero fails """
        self.assertRaises(rd.InvalidAgeError, rd.check_dog_age, 0)


# Offer external code execution (include all lines below this point in all test files)
def main():
    # Triggers default behavior of running all test fixtures in the file
    unittest.main()


if __name__ == '__main__':
    main()
