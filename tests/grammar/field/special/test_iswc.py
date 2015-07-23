# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import special

"""
Tests for ISWC fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestISWCResultName(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.iswc = special.iswc()

    def test_common(self):
        code = 'T0345246801'

        result = self.iswc.parseString(code)

        self.assertEqual('T0345246801', result.iswc)


class TestISWCValid(unittest.TestCase):
    """
    Tests that the ISWC accepts and parses valid values.
    """

    def setUp(self):
        self.iswc = special.iswc()

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'T0345246801'

        result = self.iswc.parseString(code)[0]

        self.assertEqual('T0345246801', result)

    def test_max(self):
        """
        Tests the highest possible value.
        """
        code = 'T9999999999'

        result = self.iswc.parseString(code)[0]

        self.assertEqual('T9999999999', result)

    def test_min(self):
        """
        Tests the lowest possible value.
        """
        code = 'T0000000000'

        result = self.iswc.parseString(code)[0]

        self.assertEqual('T0000000000', result)


class TestISWCException(unittest.TestCase):
    """
    Tests that exceptions are thrown when using invalid values
    """

    def setUp(self):
        self.iswc = special.iswc()

    def test_only_header(self):
        """
        Tests that an exception is thrown when only the header is set.
        """
        code = 'T          '

        self.assertRaises(ParseException, self.iswc.parseString, code)

    def test_only_numbers_no_header(self):
        """
        Tests that an exception is thrown when only 10 numbers and no header are received.
        """
        code = '9999999999'

        self.assertRaises(ParseException, self.iswc.parseString, code)

    def test_only_numbers(self):
        """
        Tests that an exception is thrown when 11 numbers are received.
        """
        code = '99999999999'

        self.assertRaises(ParseException, self.iswc.parseString, code)

    def test_empty(self):
        """
        Tests that an exception is thrown when the string is empty
        """
        code = ''

        self.assertRaises(ParseException, self.iswc.parseString, code)

    def test_whitespaces(self):
        """
        Tests that an exception is thrown when the string is composed of only whitespaces
        """
        code = '           '

        self.assertRaises(ParseException, self.iswc.parseString, code)

    def test_too_short_empty(self):
        """
        Tests that an exception is thrown when the string is too short
        """
        code = 'T999999999'

        self.assertRaises(ParseException, self.iswc.parseString, code)
