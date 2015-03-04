# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar import field


"""
Tests for Table/List Lookup (L) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestLookupName(unittest.TestCase):
    def test_default_name(self):
        """
        Tests that the field is named correctly
        """
        lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3)

        self.assertEqual('Lookup Field', lookup.name)

    def test_default_name_compulsory(self):
        """
        Tests that the field is named correctly
        """
        lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3, compulsory=True)

        self.assertEqual('Lookup Field', lookup.name)

    def test_give_name_factory_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        lookup1 = field.lookup(('AB1', 'CD2', 'EF3'), columns=3, name='field1')
        lookup2 = field.lookup(('AB1', 'CD2', 'EF3'), columns=3, name='field2')

        self.assertEqual('field1', lookup1.name)
        self.assertEqual('field2', lookup2.name)


class TestLookupValid(unittest.TestCase):
    """
    Tests that the lookup field accepts and parse valid values.
    """

    def setUp(self):
        self.lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3)

    def test_valid(self):
        """
        Tests that the field accepts a valid value
        """
        result = self.lookup.parseString('CD2')
        self.assertEqual('CD2', result[0])

    def test_empty(self):
        """
        Tests that the field accepts the empty string
        """
        result = self.lookup.parseString('   ')
        self.assertEqual(None, result[0])


class TestLookupValidCompulsory(unittest.TestCase):
    """
    Tests that the lookup field accepts and parse valid values.
    """

    def setUp(self):
        self.lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3, compulsory=True)

    def test_valid(self):
        """
        Tests that the field accepts a valid value
        """
        result = self.lookup.parseString('CD2')
        self.assertEqual('CD2', result[0])


class TestLookupException(unittest.TestCase):
    def setUp(self):
        self.lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3)

    def test_invalid(self):
        """
        Tests that an exception is thrown when parsing an invalid value
        """
        self.assertRaises(ParseException, self.lookup.parseString, 'AEI')

    def test_empty(self):
        """
        Tests that an exception is thrown when parsing an invalid value
        """
        self.assertRaises(ParseException, self.lookup.parseString, '')


class TestLookupExceptionCompulsory(unittest.TestCase):
    def setUp(self):
        self.lookup = field.lookup(('AB1', 'CD2', 'EF3'), columns=3, compulsory=True)

    def test_invalid(self):
        """
        Tests that an exception is thrown when parsing an invalid value
        """
        self.assertRaises(ParseException, self.lookup.parseString, 'AEI')

    def test_empty(self):
        """
        Tests that an exception is thrown when parsing an invalid value
        """
        self.assertRaises(ParseException, self.lookup.parseString, '')

    def test_whitespace(self):
        """
        Tests that an exception is thrown when parsing an invalid value
        """
        self.assertRaises(ParseException, self.lookup.parseString, '   ')