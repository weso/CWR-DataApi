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
    Tests that the flag field accepts and parse valid values.
    """

    def setUp(self):
        self.flag = field.flag()

    def test_true(self):
        """
        Tests that the boolean field accepts true ('Y').
        """
        result = self.flag.parseString('Y')
        self.assertEqual('Y', result[0])

    def test_false(self):
        """
        Tests that the boolean field accepts false ('N').
        """
        result = self.flag.parseString('N')
        self.assertEqual('N', result[0])

    def test_unknown(self):
        """
        Tests that the boolean field accepts unknown ('U').
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
