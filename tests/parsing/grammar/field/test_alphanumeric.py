# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.parsing.grammar import field


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
        self.alpha = field.alphanum(5)

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


class TestAlphanumCompulsoryValid(unittest.TestCase):
    """
    Tests that the alphanumeric field accepts and parse valid values.
    """

    def setUp(self):
        self.alpha = field.alphanum(5, compulsory=True)

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


class TestAlphanumException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = field.alphanum(5)

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


class TestAlphanumCompulsoryException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.alpha = field.alphanum(5, compulsory=True)

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