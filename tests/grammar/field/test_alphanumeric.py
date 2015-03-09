# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic


"""
Tests for Alphanumeric (A) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAlphanumValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = basic.alphanum(5)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Alphanumeric Field', self.alpha.name)

    def test_alphanum_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCD1')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_longer(self):
        """
        Tests that the alphanum field cuts strings which are longer than the required size.
        """
        result = self.alpha.parseString('ABCD1234')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_full_only_number(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('12345')
        self.assertEqual('12345', result[0])

    def test_alphanum_full_only_letters(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCDE')
        self.assertEqual('ABCDE', result[0])

    def test_alphanum_trailing_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and trailed by white spaces.
        """
        result = self.alpha.parseString('AB   ')
        self.assertEqual('AB', result[0])

    def test_alphanum_head_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and headed by white spaces.
        """
        result = self.alpha.parseString('   DE')
        self.assertEqual('DE', result[0])

    def test_alphanum_whites(self):
        """
        Tests that the alphanum field accepts values surrounded by whitespaces.
        """
        result = self.alpha.parseString('  C  ')
        self.assertEqual('C', result[0])

    def test_alphanum_empty(self):
        """
        Tests that the alphanum field accepts an empty string of the correct number of characters.
        """
        result = self.alpha.parseString('     ')
        self.assertEqual('', result[0])

    def test_spaces_between(self):
        """
        Tests that the alphanum field accepts a string of the correct number of characters with spaces in between.
        """
        result = self.alpha.parseString('AB CD')
        self.assertEqual('AB CD', result[0])


class TestAlphanumExtendedValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = basic.alphanum(5, extended=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Alphanumeric Field', self.alpha.name)

    def test_alphanum_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCD1')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_longer(self):
        """
        Tests that the alphanum field cuts strings which are longer than the required size.
        """
        result = self.alpha.parseString('ABCD1234')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_full_only_number(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('12345')
        self.assertEqual('12345', result[0])

    def test_alphanum_full_only_letters(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCDE')
        self.assertEqual('ABCDE', result[0])

    def test_alphanum_trailing_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and trailed by white spaces.
        """
        result = self.alpha.parseString('AB   ')
        self.assertEqual('AB', result[0])

    def test_alphanum_head_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and headed by white spaces.
        """
        result = self.alpha.parseString('   DE')
        self.assertEqual('DE', result[0])

    def test_alphanum_whites(self):
        """
        Tests that the alphanum field accepts values surrounded by whitespaces.
        """
        result = self.alpha.parseString('  C  ')
        self.assertEqual('C', result[0])

    def test_alphanum_empty(self):
        """
        Tests that the alphanum field accepts an empty string of the correct number of characters.
        """
        result = self.alpha.parseString('     ')
        self.assertEqual('', result[0])

    def test_spaces_between(self):
        """
        Tests that the alphanum field accepts a string of the correct number of characters with spaces in between.
        """
        result = self.alpha.parseString('AB CD')
        self.assertEqual('AB CD', result[0])

    def test_extended(self):
        """
        Tests that the alphanum field accepts a string of the correct number of characters with spaces in between.
        """
        text = 'AB\xc6\x8fC'
        result = self.alpha.parseString(text)
        self.assertEqual('AB\xc6\x8fC', result[0])


class TestAlphanumHugeValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = basic.alphanum(480)

    def test_common(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString(
            'THE NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ')
        self.assertEqual('THE NAME', result[0])

    def test_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString(
            'THEANAMEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(
            'THEANAMEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            result[0])

    def test_empty(self):
        """
        Tests that the alphanum field accepts an empty string of the correct number of characters.
        """
        result = self.alpha.parseString(
            '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ')
        self.assertEqual('', result[0])


class TestAlphanumCompulsoryValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = basic.alphanum(5, compulsory=True)

    def test_name(self):
        """
        Tests that the field is named correctly
        """
        self.assertEqual('Alphanumeric Field', self.alpha.name)

    def test_alphanum_full(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('ABCD1')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_longer(self):
        """
        Tests that the alphanum field cuts strings which are longer than the required size.
        """
        result = self.alpha.parseString('ABCD1234')
        self.assertEqual('ABCD1', result[0])

    def test_alphanum_full_only_number(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters.
        """
        result = self.alpha.parseString('12345')
        self.assertEqual('12345', result[0])

    def test_alphanum_trailing_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and trailed by white spaces.
        """
        result = self.alpha.parseString('AB   ')
        self.assertEqual('AB', result[0])

    def test_alphanum_head_whites(self):
        """
        Tests that the alphanum field accepts values of the correct number of characters and headed by white spaces.
        """
        result = self.alpha.parseString('   DE')
        self.assertEqual('DE', result[0])

    def test_alphanum_whites(self):
        """
        Tests that the alphanum field accepts values surrounded by whitespaces.
        """
        result = self.alpha.parseString('  C  ')
        self.assertEqual('C', result[0])

    def test_spaces_between(self):
        """
        Tests that the alphanum field accepts a string of the correct number of characters with spaces in between.
        """
        result = self.alpha.parseString('AB CD')
        self.assertEqual('AB CD', result[0])


class TestAlphanumConstructorException(unittest.TestCase):
    def test_cols_negative(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.alphanum, -1)

    def test_cols_negative_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as negative.
        """
        self.assertRaises(BaseException, basic.alphanum, -1, True)

    def test_cols_zero(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.alphanum, 0)

    def test_cols_zero_compulsory(self):
        """
        Tests that an exception is thrown when the columns are set as zero.
        """
        self.assertRaises(BaseException, basic.alphanum, 0, True)


class TestAlphanumException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = basic.alphanum(5)

    def test_alphanum_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.alpha.parseString, '')

    def test_alphanum_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB')

    def test_alphanum_wrong_no_caps(self):
        """
        Tests that an exception is thrown when the field is not using capitol letters.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'ABcDE')

    def test_invalid_char(self):
        """
        Tests that an exception is thrown when the field is not using capitol letters.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB\xc6\x8fE')


class TestAlphanumHugeException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = basic.alphanum(480)

    def test_alphanum_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.alpha.parseString, '')

    def test_alphanum_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB')


class TestAlphanumCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = basic.alphanum(5, compulsory=True)

    def test_alphanum_wrong_size_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.alpha.parseString, '')

    def test_alphanum_wrong_size_too_small(self):
        """
        Tests that an exception is thrown when the field is smaller than expected.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB')

    def test_alphanum_wrong_no_caps(self):
        """
        Tests that an exception is thrown when the field is not using capitol letters.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'ABcDE')

    def test_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        self.assertRaises(ParseException, self.alpha.parseString, '     ')

    def test_invalid_char(self):
        """
        Tests that an exception is thrown when the field is not using capitol letters.
        """
        self.assertRaises(ParseException, self.alpha.parseString, 'AB\xc6\x8fE')