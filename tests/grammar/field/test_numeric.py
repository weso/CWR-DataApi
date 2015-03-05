# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic


"""
Tests for Numeric (N) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNumericValid(unittest.TestCase):
    """
    Tests that the numeric field accepts and parse valid values.
    """

    def setUp(self):
        self.num = basic.numeric(5)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Numeric Field', self.num.name)

    def test_numeric(self):
        """
        Tests that the numeric field accepts values of the correct number of characters.
        """
        result = self.num.parseString('12340')
        self.assertEqual(12340, result[0])

    def test_numeric_zeros(self):
        """
        Tests that the numeric field accepts zeros.
        """
        result = self.num.parseString('00000')
        self.assertEqual(0, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric field accepts values starting with zeros.
        """
        result = self.num.parseString('00123')
        self.assertEqual(123, result[0])


class TestNumericCompulsoryValid(unittest.TestCase):
    """
    Tests that the numeric field accepts and parse valid values.
    """

    def setUp(self):
        self.num = basic.numeric(5, compulsory=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Numeric Field', self.num.name)

    def test_numeric(self):
        """
        Tests that the numeric field accepts values of the correct number of characters.
        """
        result = self.num.parseString('12340')
        self.assertEqual(12340, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric field accepts values starting with zeros.
        """
        result = self.num.parseString('00123')
        self.assertEqual(123, result[0])


class TestNumericConstructorException(unittest.TestCase):
    def test_cols_negative(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.numeric, -1)

    def test_cols_negative_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.numeric, -1, True)

    def test_cols_zero(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.numeric, 0)

    def test_cols_zero_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.numeric, 0, True)


class TestNumericException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = basic.numeric(5)

    def test_numeric_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.num.parseString, '')

    def test_numeric_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '123')

    def test_numeric_negative(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '-1234')

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')


class TestNumericCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = basic.numeric(5, compulsory=True)

    def test_numeric_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.num.parseString, '')

    def test_numeric_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '123')

    def test_numeric_negative(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.num.parseString, '-1234')

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')
