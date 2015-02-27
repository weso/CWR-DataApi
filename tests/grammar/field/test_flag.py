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


class TestFlagValid(unittest.TestCase):
    """
    Tests that the flag field accepts and parses valid values.
    """

    def setUp(self):
        self.flag = field.flag()

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Flag Field', self.flag.name)

    def test_true(self):
        """
        Tests that the flag field accepts true ('Y').
        """
        result = self.flag.parseString('Y')
        self.assertEqual('Y', result[0])

    def test_false(self):
        """
        Tests that the flag field accepts false ('N').
        """
        result = self.flag.parseString('N')
        self.assertEqual('N', result[0])

    def test_unknown(self):
        """
        Tests that the flag field accepts unknown ('U').
        """
        result = self.flag.parseString('U')
        self.assertEqual('U', result[0])

    def test_whitespace(self):
        """
        Tests that the flag field accepts a whitespace.
        """
        result = self.flag.parseString(' ')
        self.assertEqual(None, result[0])


class TestFlagCompulsoryValid(unittest.TestCase):
    """
    Tests that the flag field accepts and parses valid values.
    """

    def setUp(self):
        self.flag = field.flag(compulsory=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Flag Field', self.flag.name)

    def test_true(self):
        """
        Tests that the flag field accepts true ('Y').
        """
        result = self.flag.parseString('Y')
        self.assertEqual('Y', result[0])

    def test_false(self):
        """
        Tests that the flag field accepts false ('N').
        """
        result = self.flag.parseString('N')
        self.assertEqual('N', result[0])

    def test_unknown(self):
        """
        Tests that the flag field accepts unknown ('U').
        """
        result = self.flag.parseString('U')
        self.assertEqual('U', result[0])


class TestFlagException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.flag = field.flag()

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'n')

    def test_unknown_lower(self):
        """
        Tests that an exception is thrown when the unknown code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'u')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.flag.parseString, '')


class TestFlagCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.flag = field.flag(compulsory=True)

    def test_true_lower(self):
        """
        Tests that an exception is thrown when the true code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'y')

    def test_false_lower(self):
        """
        Tests that an exception is thrown when the false code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'n')

    def test_unknown_lower(self):
        """
        Tests that an exception is thrown when the unknown code is in lower letters.
        """
        self.assertRaises(ParseException, self.flag.parseString, 'u')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.flag.parseString, '')

    def test_whitespace(self):
        """
        Tests that an exception is thrown when the string is a whitespace.
        """
        self.assertRaises(ParseException, self.flag.parseString, ' ')
