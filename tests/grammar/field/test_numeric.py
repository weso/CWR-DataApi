# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic

"""
Tests for Numeric (N) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNumericName(unittest.TestCase):
    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.numeric(5)

        self.assertEqual('Numeric Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.numeric(5, name=name)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.numeric(5, name='field1')
        field2 = basic.numeric(5, name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class TestNumericCompulsoryValid(unittest.TestCase):
    """
    Tests that the numeric field accepts and parse valid values.
    """

    def setUp(self):
        self.num = basic.numeric(5)

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


class TestNumericCompulsoryException(unittest.TestCase):
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

    def test_whitespaces(self):
        """
        Tests that an exception is thrown when the field is composed of whitespaces.
        """
        self.assertRaises(ParseException, self.num.parseString, '     ')

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

    def test_spaces_between(self):
        """
        Tests that an exception is thrown when the field contains whitespaces between the numbers.
        """
        self.assertRaises(ParseException, self.num.parseString, '12 34')
