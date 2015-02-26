# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar import field


"""
Tests for Time (T) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTimeValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.
    """

    def setUp(self):
        self.time = field.time()

    def test_common(self):
        """
        Tests that the time field accepts a valid time.
        """
        result = self.time.parseString('201510')[0]

        self.assertEqual(20, result.hour)
        self.assertEqual(15, result.minute)
        self.assertEqual(10, result.second)

    def test_max(self):
        """
        Tests that the time field accepts the highest possible time.
        """
        result = self.time.parseString('235959')[0]

        self.assertEqual(23, result.hour)
        self.assertEqual(59, result.minute)
        self.assertEqual(59, result.second)

    def test_min(self):
        """
        Tests that the time field accepts the lowest possible time.
        """
        result = self.time.parseString('000000')[0]

        self.assertEqual(0, result.hour)
        self.assertEqual(0, result.minute)
        self.assertEqual(0, result.second)


class TestTimeException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.time = field.time()

    def test_wrong_hour(self):
        """
        Tests that an exception is thrown when the hour is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '241122')

    def test_wrong_minute(self):
        """
        Tests that an exception is thrown when the minute is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '206022')

    def test_wrong_second(self):
        """
        Tests that an exception is thrown when the second is invalid.
        """
        self.assertRaises(ParseException, self.time.parseString, '203060')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.time.parseString, '')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by spaces.
        """
        self.assertRaises(ParseException, self.time.parseString, ' 203020')

    def test_too_short(self):
        """
        Tests that an exception is thrown when the string is too short.
        """
        self.assertRaises(ParseException, self.time.parseString, '03020')
