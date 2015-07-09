# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.factory.rule import FieldRuleFactory
from cwr.grammar.factory.adapter import LookupAdapter

"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def _factory():
    adapters = {'lookup': LookupAdapter()}

    config_fields = {
        'test_lookup': {'type': 'lookup', 'name': 'Test Lookup Field',
                        'size': 3, 'values': ['AB1', 'CD2', 'EF3']}}

    return FieldRuleFactory(config_fields, adapters)


class TestLookupFieldFactoryValid(unittest.TestCase):
    def setUp(self):
        self._factory = _factory()

    def test_creation(self):
        field_id = 'test_lookup'

        result = self._factory.get_rule(field_id)

        self.assertNotEqual(None, result)

    def test_optional_trailing_whitespace(self):
        field_id = 'test_lookup'

        result = self._factory.get_rule(field_id)
        result = result.parseString('CD2  ')[0]

        self.assertEqual('CD2', result)

    def test_compulsory_trailing_whitespace(self):
        field_id = 'test_lookup'

        result = self._factory.get_rule(field_id)
        result = result.parseString('CD2  ')[0]

        self.assertEqual('CD2', result)

    def test_returns_same(self):
        field_id = 'test_lookup'

        result1 = self._factory.get_rule(field_id)
        result2 = self._factory.get_rule(field_id)

        self.assertEqual(result1, result2)


class TestLookupFieldFactoryException(unittest.TestCase):
    def setUp(self):
        self._factory = _factory()

    def test_compulsory_heading_whitespace(self):
        field_id = 'test_lookup'

        field = self._factory.get_rule(field_id)

        self.assertRaises(ParseException, field.parseString, '   CD2')

    def test_whitespace_compulsory(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        field_id = 'test_lookup'

        field = self._factory.get_rule(field_id)

        self.assertRaises(ParseException, field.parseString, '   ')

    def test_empty_compulsory(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        field_id = 'test_lookup'

        field = self._factory.get_rule(field_id)

        self.assertRaises(ParseException, field.parseString, '')

    def test_invalid(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        field_id = 'test_lookup'

        field = self._factory.get_rule(field_id)

        self.assertRaises(ParseException, field.parseString, '123')

    def test_invalid_whitespace(self):
        """
        Tests that an exception is thrown when the field is empty and it shouldn't be.
        """
        field_id = 'test_lookup'

        field = self._factory.get_rule(field_id)

        self.assertRaises(ParseException, field.parseString, '12 ')
