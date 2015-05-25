# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_rules_list


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestConfigTerminalRule(unittest.TestCase):
    def setUp(self):
        self._rule = rule_rules_list

    def test_empty(self):
        line = 'sequence:' + '\n' + \
               '[' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('sequence', result.list_type)

        self.assertEqual(0, len(result.rules))

    def test_varied(self):
        line = 'sequence:' + '\n' + \
               '[' + '\n' + \
               'field: header (compulsory)' + '\n' + \
               'transaction: year' + '\n' + \
               ']'

        result = self._rule.parseString(line)

        self.assertEqual('sequence', result.list_type)

        self.assertEqual(2, len(result.rules))

        rule = result.rules[0]
        self.assertEqual('field', rule.rule_type)
        self.assertEqual('header', rule.rule_name)
        self.assertEqual('compulsory', rule.rule_options[0])

        rule = result.rules[1]
        self.assertEqual('transaction', rule.rule_type)
        self.assertEqual('year', rule.rule_name)
        self.assertEqual(0, len(rule.rule_options))