# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.factory.field import DefaultFieldFactory

from data.accessor import CWRTables
from data.accessor import CWRConfiguration


"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()


class TestLookupFieldFactoryValid(unittest.TestCase):
    def setUp(self):
        self.factory = DefaultFieldFactory(_config.load_field_config_table(), CWRTables())

    def test_creation(self):
        id = 'original_transaction_type'

        result = self.factory.get_field(id)

        self.assertNotEqual(None, result)

    def test_optional_empty_whitespaces(self):
        id = 'original_transaction_type'

        result = self.factory.get_field(id)
        result = result.parseString('   AGR')

        self.assertNotEqual(None, result)

    def test_optional_valid(self):
        id = 'original_transaction_type'

        result = self.factory.get_field(id)
        result = result.parseString('AGR  ')

        self.assertNotEqual('AGR', result)

    def test_compulsory_valid(self):
        id = 'original_transaction_type'

        result = self.factory.get_field(id, compulsory=True)
        result = result.parseString('AGR  ')

        self.assertNotEqual('AGR', result)

    def test_returns_same(self):
        id = 'original_transaction_type'

        result1 = self.factory.get_field(id)
        result2 = self.factory.get_field(id)

        self.assertEqual(result1, result2)


class TestLookupFieldFactoryException(unittest.TestCase):
    def setUp(self):
        self.factory = DefaultFieldFactory(_config.load_field_config_table(), CWRTables())

    def test_whitespace_compulsory(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        id = 'original_transaction_type'

        field = DefaultFieldFactory(_config.load_field_config_table(), CWRTables()).get_field(id, compulsory=True)

        self.assertRaises(ParseException, field.parseString, '   ')

    def test_empty_compulsory(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        id = 'original_transaction_type'

        field = DefaultFieldFactory(_config.load_field_config_table(), CWRTables()).get_field(id, compulsory=True)

        self.assertRaises(ParseException, field.parseString, '')

    def test_empty(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        id = 'original_transaction_type'

        field = DefaultFieldFactory(_config.load_field_config_table(), CWRTables()).get_field(id)

        self.assertRaises(ParseException, field.parseString, '')

    def test_invalid(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        id = 'original_transaction_type'

        field = DefaultFieldFactory(_config.load_field_config_table(), CWRTables()).get_field(id)

        self.assertRaises(ParseException, field.parseString, '123')

    def test_invalid_whitespace(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        id = 'original_transaction_type'

        field = DefaultFieldFactory(_config.load_field_config_table(), CWRTables()).get_field(id)

        self.assertRaises(ParseException, field.parseString, '12 ')