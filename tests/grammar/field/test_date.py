# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic


"""
Tests for Date (D) fields.

The following cases are tested (most tests are done for default and compulsory fields):

- Default name is set correctly
- Given name is set correctly
- Creating a new field does not change the existing ones names

- Accepts a year ending in several zeros
- Accepts a year ending in a single zero
- Accepts a valid date
- Accepts a date composed of zeros (empty date) (if not compulsory)
- Accepts a year beginning with zeros
- Accepts the smallest possible date

- An exception is thrown when the day is too high
- An exception is thrown when the day is too low
- An exception is thrown when the month is too high
- An exception is thrown when the month is too low
- An exception is thrown when the date begins with empty spaces
- An exception is thrown when the date contains letters
- An exception is thrown when the date is the empty string
- An exception is thrown when the date is composed of zeros (empty date) (if compulsory)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestDateName(unittest.TestCase):
    """
    Tests that the field name is set correctly.

    The following cases are tested:

    - Default name is set correctly
    - Given name is set correctly
    """

    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.date()

        self.assertEqual('Date Field', field.name)

    def test_name_default_compulsory(self):
        """
        Tests that the default field name is correct for optional fields, for compulsory fields.
        """
        field = basic.date(compulsory=True)

        self.assertEqual('Date Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.date(name=name)

        self.assertEqual(name, field.name)

    def test_name_set_compulsory(self):
        """
        Tests that the given field name is set correctly for optional fields, for compulsory fields.
        """
        name = "Field Name"
        field = basic.date(name=name, compulsory=True)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.date(name='field1')
        field2 = basic.date(name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class TestDateValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values.

    The following cases are tested:

    - Accepts a year ending in several zeros
    - Accepts a year ending in a single zero
    - Accepts a valid date
    - Accepts a date composed of zeros (empty date)
    - Accepts a year beginning with zeros
    - Accepts the smallest possible date
    """

    def setUp(self):
        self.date = basic.date()

    def test_year_ends_zero_several(self):
        """
        Tests that the date field accepts a date where the year ends in zeros.
        """
        result = self.date.parseString('20000606')[0]

        self.assertEqual(2000, result.year)
        self.assertEqual(6, result.month)
        self.assertEqual(6, result.day)

    def test_year_ends_zero(self):
        """
        Tests that the date field accepts a year ending in a zero.
        """
        result = self.date.parseString('20101121')[0]

        self.assertEqual(2010, result.year)
        self.assertEqual(11, result.month)
        self.assertEqual(21, result.day)

    def test_common(self):
        """
        Tests that the date field accepts a valid date.
        """
        result = self.date.parseString('20121121')[0]

        self.assertEqual(2012, result.year)
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
        Tests that the date field accepts the smallest valid date.
        """
        result = self.date.parseString('00010101')[0]

        self.assertEqual(1, result.year)
        self.assertEqual(1, result.month)
        self.assertEqual(1, result.day)


class TestCompulsoryValid(unittest.TestCase):
    """
    Tests that the date field accepts and parse valid values if it is compulsory.

    The following cases are tested:

    - Accepts a year ending in several zeros
    - Accepts a year ending in a single zero
    - Accepts a valid date
    - Accepts a year beginning with zeros
    - Accepts the smallest possible date
    """

    def setUp(self):
        self.date = basic.date(compulsory=True)

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
        Tests that the date field accepts the smallest valid date.
        """
        result = self.date.parseString('00010101')[0]

        self.assertEqual(1, result.year)
        self.assertEqual(1, result.month)
        self.assertEqual(1, result.day)


class TestDateException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values

    The following cases are tested:

    - An exception is thrown when the day is too high
    - An exception is thrown when the day is too low
    - An exception is thrown when the month is too high
    - An exception is thrown when the month is too low
    - An exception is thrown when the date begins with empty spaces
    - An exception is thrown when the date contains letters
    - An exception is thrown when the date is the empty string
    """

    def setUp(self):
        self.date = basic.date()

    def test_wrong_day_too_high(self):
        """
        Tests that an exception is thrown when the day is too high.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121133')

    def test_wrong_day_too_low(self):
        """
        Tests that an exception is thrown when the day is too low.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121100')

    def test_wrong_month_too_high(self):
        """
        Tests that an exception is thrown when the month is too high.
        """
        self.assertRaises(ParseException, self.date.parseString, '20121312')

    def test_wrong_month_too_low(self):
        """
        Tests that an exception is thrown when the month is too low.
        """
        self.assertRaises(ParseException, self.date.parseString, '20120012')

    def test_spaces_head(self):
        """
        Tests that an exception is thrown when the string is headed by empty spaces.
        """
        self.assertRaises(ParseException, self.date.parseString, ' 20121121')

    def test_letters(self):
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

    The following cases are tested:

    - An exception is thrown when the day is too high
    - An exception is thrown when the day is too low
    - An exception is thrown when the month is too high
    - An exception is thrown when the month is too low
    - An exception is thrown when the date begins with empty spaces
    - An exception is thrown when the date contains letters
    - An exception is thrown when the date is the empty string
    - An exception is thrown when the date is composed of zeros (empty date) (if compulsory)
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
