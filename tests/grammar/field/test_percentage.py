# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import special


"""
Tests for Percentage fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPercentageValid(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Percentage Field', self.perc.name)

    def test_common(self):
        """
        Tests that the alphanum field accepts a common number.
        """
        result = self.perc.parseString('05023')

        self.assertEqual(50.23, result[0])

    def test_no_decimal(self):
        """
        Tests that the alphanum field accepts a number with no decimals.
        """
        result = self.perc.parseString('05000')

        self.assertEqual(50, result[0])

    def test_no_integer(self):
        """
        Tests that the alphanum field accepts a number with no integer.
        """
        result = self.perc.parseString('00023')

        self.assertEqual(0.23, result[0])

    def test_max(self):
        """
        Tests that the alphanum field accepts 100%.
        """
        result = self.perc.parseString('10000')

        self.assertEqual(100, result[0])

    def test_min(self):
        """
        Tests that the alphanum field accepts 0%.
        """
        result = self.perc.parseString('00000')

        self.assertEqual(0, result[0])


class TestPercentage50Valid(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5, max=50)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Percentage Field', self.perc.name)

    def test_common(self):
        """
        Tests that the alphanum field accepts a common number.
        """
        result = self.perc.parseString('01223')

        self.assertEqual(12.23, result[0])

    def test_no_decimal(self):
        """
        Tests that the alphanum field accepts a number with no decimals.
        """
        result = self.perc.parseString('04100')

        self.assertEqual(41, result[0])

    def test_no_integer(self):
        """
        Tests that the alphanum field accepts a number with no integer.
        """
        result = self.perc.parseString('00023')

        self.assertEqual(0.23, result[0])

    def test_max(self):
        """
        Tests that the alphanum field accepts 100%.
        """
        result = self.perc.parseString('05000')

        self.assertEqual(50, result[0])

    def test_min(self):
        """
        Tests that the alphanum field accepts 0%.
        """
        result = self.perc.parseString('00000')

        self.assertEqual(0, result[0])


class TestPercentageCompulsoryValid(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5, compulsory=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Percentage Field', self.perc.name)

    def test_common(self):
        """
        Tests that the alphanum field accepts a common number.
        """
        result = self.perc.parseString('05023')

        self.assertEqual(50.23, result[0])

    def test_no_decimal(self):
        """
        Tests that the alphanum field accepts a number with no decimals.
        """
        result = self.perc.parseString('05000')

        self.assertEqual(50, result[0])

    def test_no_integer(self):
        """
        Tests that the alphanum field accepts a number with no integer.
        """
        result = self.perc.parseString('00023')

        self.assertEqual(0.23, result[0])

    def test_max(self):
        """
        Tests that the alphanum field accepts 100%.
        """
        result = self.perc.parseString('10000')

        self.assertEqual(100, result[0])


class TestPercentageConstructorException(unittest.TestCase):
    def test_too_small(self):
        self.assertRaises(BaseException, special.percentage, 2)

    def test_zero(self):
        self.assertRaises(BaseException, special.percentage, 0)

    def test_negative(self):
        self.assertRaises(BaseException, special.percentage, -1)


class TestPercentageException(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5)

    def test_above_max(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '15000')

    def test_empty(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '')


class TestPercentage50Exception(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5, max=50)

    def test_above_max(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '05001')

    def test_empty(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '')


class TestPercentageCompulsoryException(unittest.TestCase):
    """
    Tests that the percentage field accepts and parse valid values.
    """

    def setUp(self):
        self.perc = special.percentage(5, compulsory=True)

    def test_above_max(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '15000')

    def test_empty(self):
        """
        Tests that an exception is thrown when the value is set higher than the maximum value.
        """
        self.assertRaises(ParseException, self.perc.parseString, '')

    def test_zero(self):
        """
        Tests that an exception is thrown when the value is zero.
        """
        self.assertRaises(ParseException, self.perc.parseString, '00000')