# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar import field


"""
Tests for Boolean (B) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestBooleanValid(unittest.TestCase):
    """
    Tests that the boolean field accepts and parse valid values.
    """

    def setUp(self):
        self.boolean = field.boolean()

    def test_true(self):
        """
        Tests that the boolean field accepts true ('Y').
        """
        result = self.boolean.parseString('Y')
        self.assertEqual(True, result[0])

    def test_false(self):
        """
        Tests that the boolean field accepts false ('N').
        """
        result = self.boolean.parseString('N')
        self.assertEqual(False, result[0])

    def test_whitespace(self):
        """
        Tests that the boolean field accepts empty strings.
        """
        result = self.boolean.parseString(' ')
        self.assertEqual(False, result[0])


class TestBooleanCompulsoryValid(unittest.TestCase):
    """
    Tests that the boolean field accepts and parse valid values.
    """

    def setUp(self):
        self.boolean = field.boolean(compulsory=True)

    def test_true(self):
        """
        Tests that the boolean field accepts true ('Y').
        """
        result = self.boolean.parseString('Y')
        self.assertEqual(True, result[0])

    def test_false(self):
        """
        Tests that the boolean field accepts false ('N').
        """
        result = self.boolean.parseString('N')
        self.assertEqual(False, result[0])


class TestBooleanException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.boolean = field.boolean()

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'n')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.boolean.parseString, '')

    def test_invalid(self):
        """
        Tests that an exception is thrown when the string is invalid.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'W')


class TestBooleanCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.boolean = field.boolean(compulsory=True)

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'n')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.boolean.parseString, '')

    def test_whitespace(self):
        """
        Tests that an exception is thrown when the string is a whitespace.
        """
        self.assertRaises(ParseException, self.boolean.parseString, ' ')

    def test_invalid(self):
        """
        Tests that an exception is thrown when the string is invalid.
        """
        self.assertRaises(ParseException, self.boolean.parseString, 'W')
