# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_options

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestConfigOptions(unittest.TestCase):
    def setUp(self):
        self._rule = rule_options

    def test_zero_options(self):
        line = '()'

        result = self._rule.parseString(line)

        self.assertEqual(1, len(result))

        self.assertEqual('', result[0])

    def test_one_options(self):
        line = '(option2)'

        result = self._rule.parseString(line)

        self.assertEqual(1, len(result))

        self.assertEqual('option2', result[0])

    def test_two_options(self):
        line = '(option1, option2)'

        result = self._rule.parseString(line)

        self.assertEqual(2, len(result))

        self.assertEqual('option1', result[0])
        self.assertEqual('option2', result[1])
