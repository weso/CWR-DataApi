# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic


"""
Tests for Boolean (B) fields.

The following cases are tested (most tests are done for default and compulsory fields):

- Default name is set correctly
- Given name is set correctly
- Creating a new field does not change the existing ones names

- Accepts a value of true ('Y')
- Accepts a value of false ('N')
- Accepts an empty string (if optional)

- An exception is thrown when the values are in lower case
- An exception is thrown when the value is the empty string
- An exception is thrown when the value is an invalid character
- An exception is thrown when the value is a white space (if compulsory)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestBooleanName(unittest.TestCase):
    """
    Tests that the Boolean field name is set correctly.

    The following cases are tested:

    - Default name is set correctly
    - Given name is set correctly
    """

    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.boolean()

        self.assertEqual('Boolean Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.boolean(name=name)

        self.assertEqual(name, field.name)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.boolean(name='field1')
        field2 = basic.boolean(name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class TestBooleanValid(unittest.TestCase):
    """
    Tests that the compulsory Boolean field accepts and parse valid values.

    The following cases are tested:

    - Accepts a value of true ('Y')
    - Accepts a value of false ('N')
    """

    def setUp(self):
        self.field = basic.boolean()

    def test_true(self):
        """
        Tests that the Boolean field accepts true ('Y').
        """
        result = self.field.parseString('Y')
        self.assertEqual(True, result[0])

    def test_false(self):
        """
        Tests that the Boolean field accepts false ('N').
        """
        result = self.field.parseString('N')
        self.assertEqual(False, result[0])


class TestBooleanException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values on a compulsory field.

    The following cases are tested:

    - An exception is thrown when the values are in lower case
    - An exception is thrown when the value is the empty string
    - An exception is thrown when the value is a white space
    - An exception is thrown when the value is an invalid character
    """

    def setUp(self):
        self.field = basic.boolean()

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.field.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.field.parseString, 'n')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.field.parseString, '')

    def test_whitespace(self):
        """
        Tests that an exception is thrown when the string is a whitespace.
        """
        self.assertRaises(ParseException, self.field.parseString, ' ')

    def test_invalid(self):
        """
        Tests that an exception is thrown when the string is invalid.
        """
        self.assertRaises(ParseException, self.field.parseString, 'W')
