# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_terminal

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestConfigTerminalRule(unittest.TestCase):
    def setUp(self):
        self._rule = rule_terminal

    def test_not_options(self):
        line = 'field: header'

        result = self._rule.parseString(line)

        self.assertEqual('field', result.rule_type)
        self.assertEqual('header', result.rule_name)

    def test_one_option(self):
        line = 'field: header (compulsory)'

        result = self._rule.parseString(line)

        self.assertEqual('field', result.rule_type)
        self.assertEqual('header', result.rule_name)

        self.assertEqual(1, len(result.rule_options))

        self.assertEqual('compulsory', result.rule_options[0])

    def test_two_options(self):
        line = 'field: header (compulsory, optional)'

        result = self._rule.parseString(line)

        self.assertEqual('field', result.rule_type)
        self.assertEqual('header', result.rule_name)

        self.assertEqual(2, len(result.rule_options))

        self.assertEqual('compulsory', result.rule_options[0])
        self.assertEqual('optional', result.rule_options[1])

    def test_two_options_tabbed(self):
        line = '            field: header (compulsory, optional)'

        result = self._rule.parseString(line)

        self.assertEqual('field', result.rule_type)
        self.assertEqual('header', result.rule_name)

        self.assertEqual(2, len(result.rule_options))

        self.assertEqual('compulsory', result.rule_options[0])
        self.assertEqual('optional', result.rule_options[1])
