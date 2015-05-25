# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import basic

"""
Tests for Table/List Lookup (L) fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestLookupName(unittest.TestCase):
    def test_name_default(self):
        """
        Tests that the default field name is correct for optional fields.
        """
        field = basic.lookup(['AB1', 'CD2', 'EF3'])

        self.assertEqual('Lookup Field', field.name)

    def test_name_set(self):
        """
        Tests that the given field name is set correctly for optional fields.
        """
        name = "Field Name"
        field = basic.lookup(['AB1', 'CD2', 'EF3'], name=name)

        self.assertEqual(name, field.name)

    def test_name_set_no_changes(self):
        """
        Tests that the field name does not change for creating a new one
        """
        field1 = basic.lookup(['AB1', 'CD2', 'EF3'], name='field1')
        field2 = basic.lookup(['AB1', 'CD2', 'EF3'], name='field2')

        self.assertEqual('field1', field1.name)
        self.assertEqual('field2', field2.name)


class TestLookupValid(unittest.TestCase):
    """
    Tests that the lookup field accepts and parse valid values.
    """

    def setUp(self):
        self.lookup = basic.lookup(['AB1', 'CD2', 'EF3'])

    def test_valid(self):
        """
        Tests that the field accepts a valid value
        """
        result = self.lookup.parseString('CD2')
        self.assertEqual('CD2', result[0])


class TestLookupExceptionCompulsory(unittest.TestCase):
    def setUp(self):
        self.lookup = basic.lookup(['AB1', 'CD2', 'EF3'])

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
