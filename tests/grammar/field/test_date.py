# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic


"""
Tests for Date (D) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestDateValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.
    """

    def setUp(self):
        self.date = basic.date()

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Date Field', self.date.name)

    def test_common(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('20121121')[0]

        self.assertEqual(2012, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_year_ends_zero(self):
        """
        Tests that the date field accepts a year ending in zero.
        """
        result = self.date.parseString('20101121')[0]

        self.assertEqual(2010, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_zeros(self):
        """
        Tests that the date field accepts the empty date.
        """
        result = self.date.parseString('00000000')[0]

        self.assertEqual(None, result)

    def test_small_year(self):
        """
        Tests that the date field accepts an uncommonly short year.
        """
        result = self.date.parseString('00121121')[0]

        self.assertEqual(12, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_minimum(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('00010101')[0]

        self.assertEqual(1, result.year)
        self.assertEqual(1, result.month)
        self.assertEqual(1, result.day)


class TestCompulsoryValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.
    """

    def setUp(self):
        self.date = basic.date(compulsory=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Date Field', self.date.name)

    def test_common(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('20121121')[0]

        self.assertEqual(2012, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_year_ends_zero(self):
        """
        Tests that the date field accepts a year ending in zero.
        """
        result = self.date.parseString('20101121')[0]

        self.assertEqual(2010, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_small_year(self):
        """
        Tests that the date field accepts an uncommonly short year.
        """
        result = self.date.parseString('00121121')[0]

        self.assertEqual(12, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_minimum(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('00010101')[0]

        self.assertEqual(1, result.year)
        self.assertEqual(1, result.month)
        self.assertEqual(1, result.day)


class TestDateException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.date = basic.date()

    def test_wrong_day_too_high(self):
        """
        Tests that an exception is thrown when the day is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121133')

    def test_wrong_day_too_low(self):
        """
        Tests that an exception is thrown when the day is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121100')

    def test_wrong_month_too_high(self):
        """
        Tests that an exception is thrown when the month is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121312')

    def test_wrong_month_too_low(self):
        """
        Tests that an exception is thrown when the month is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20120012')

    def test_wrong_year_too_low(self):
        """
        Tests that an exception is thrown when the year is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '00001112')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by empty spaces.
        """
        self.assertRaises(ParseException, self.date.parseString, ' 20121121')

    def test_spaces_letters(self):
        """
        Tests that an exception is thrown when the string contains letters.
        """
        self.assertRaises(ParseException, self.date.parseString, '201211XV')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.date.parseString, '')


class TestDateCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.date = basic.date(compulsory=True)

    def test_wrong_day_too_high(self):
        """
        Tests that an exception is thrown when the day is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121133')

    def test_wrong_day_too_low(self):
        """
        Tests that an exception is thrown when the day is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121100')

    def test_wrong_month_too_high(self):
        """
        Tests that an exception is thrown when the month is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121312')

    def test_wrong_month_too_low(self):
        """
        Tests that an exception is thrown when the month is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '20120012')

    def test_wrong_year_too_low(self):
        """
        Tests that an exception is thrown when the year is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '00001112')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by empty spaces.
        """
        self.assertRaises(ParseException, self.date.parseString, ' 20121121')

    def test_spaces_letters(self):
        """
        Tests that an exception is thrown when the string contains letters.
        """
        self.assertRaises(ParseException, self.date.parseString, '201211XV')

    def test_zeros(self):
        """
        Tests that an exception is thrown when the year is invalid.
        """
        self.assertRaises(ParseException, self.date.parseString, '00000000')

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty.
        """
        self.assertRaises(ParseException, self.date.parseString, '')
