# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.factory.rule import FieldRuleFactory
from cwr.grammar.factory.adapter import NumericAdapter
from cwr.parser.decoder.file import default_grammar_factory

"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def _field_factory():
    adapters = {'numeric': NumericAdapter()}

    config_fields = {
        'test_field': {'type': 'numeric', 'name': 'Test Field',
                       'size': 3}}

    return FieldRuleFactory(config_fields, adapters)


class TestFieldRuleFactory(unittest.TestCase):
    def setUp(self):
        self._factory = _field_factory()

    def test_repeat(self):
        rule = self._factory.get_rule('test_field')
        rule_2 = self._factory.get_rule('test_field')

        self.assertEqual(rule, rule_2)


class TestDefaultRuleFactory(unittest.TestCase):
    def setUp(self):
        self._factory = default_grammar_factory()

    def test_repeat(self):
        rule = self._factory.get_rule('transmission')
        rule_2 = self._factory.get_rule('transmission')

        self.assertEqual(rule, rule_2)
