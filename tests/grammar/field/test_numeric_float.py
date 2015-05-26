# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic

"""
Tests for Numeric (N) fields for float values.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNumericFloatName(unittest.TestCase):
    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.numeric_float(4, 2)

        self.assertEqual('Numeric Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.numeric_float(4, 2, name=name)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.numeric_float(4, 2, name='field1')
        field2 = basic.numeric_float(4, 2, name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class TestNumericFloatValid(unittest.TestCase):
    """
    Tests that the numeric float field accepts and parse valid values.
    """

    def setUp(self):
        self.num = basic.numeric_float(4, 2)

    def test_numeric(self):
        """
        Tests that the numeric float field accepts values of the correct number of characters.
        """
        result = self.num.parseString('1234')
        self.assertEqual(12.34, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric float field accepts values starting with zeros.
        """
        result = self.num.parseString('0123')
        self.assertEqual(1.23, result[0])

    def test_numeric_tail_zeros(self):
        """
        Tests that the numeric float field accepts values ending with zeros.
        """
        result = self.num.parseString('1230')
        self.assertEqual(12.3, result[0])

    def test_numeric_tail_only_zeros(self):
        """
        Tests that the numeric float field accepts values ending with zeros.
        """
        result = self.num.parseString('1200')
        self.assertEqual(12, result[0])


class TestNumericFloatUnevenValid(unittest.TestCase):
    """
    Tests that the numeric float field accepts and parse valid values.
    """

    def setUp(self):
        self.num = basic.numeric_float(5, 3)

    def test_numeric(self):
        """
        Tests that the numeric float field accepts values of the correct number of characters.
        """
        result = self.num.parseString('01234')
        self.assertEqual(12.34, result[0])

    def test_numeric_head_zeros(self):
        """
        Tests that the numeric float field accepts values starting with zeros.
        """
        result = self.num.parseString('00123')
        self.assertEqual(1.23, result[0])

    def test_numeric_tail_zeros(self):
        """
        Tests that the numeric float field accepts values ending with zeros.
        """
        result = self.num.parseString('01230')
        self.assertEqual(12.3, result[0])

    def test_numeric_tail_only_zeros(self):
        """
        Tests that the numeric float field accepts values ending with zeros.
        """
        result = self.num.parseString('01200')
        self.assertEqual(12, result[0])


class TestNumericFloatConstructorException(unittest.TestCase):
    def test_cols_negative(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.numeric_float, -1, 2)

    def test_cols_negative_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.numeric_float, -1, 2, True)

    def test_cols_zero(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.numeric_float, 0, 2)

    def test_cols_zero_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.numeric_float, 0, 2, True)

    def test_pos_negative(self):
        """
        Tests that an exception is thrown when the positive values size is set as negative.
        """
        self.assertRaises(BaseException, basic.numeric_float, 3, -1)

    def test_pos_negative_compulsory(self):
        """
        Tests that an exception is thrown when the positive values size is set as negative.
        """
        self.assertRaises(BaseException, basic.numeric_float, 3, -1, True)


class TestNumericFloatException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = basic.numeric_float(4, 2)

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

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')


class TestNumericFloatUnevenCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.num = basic.numeric_float(5, 3)

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

    def test_numeric_alphanumeric(self):
        """
        Tests that an exception is thrown when the field contains letters.
        """
        self.assertRaises(ParseException, self.num.parseString, '123ab')
