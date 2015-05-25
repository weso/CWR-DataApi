# -*- coding: utf-8 -*-

import unittest

from cwr.grammar.factory.config import rule_id

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestConfigId(unittest.TestCase):
    def setUp(self):
        self._rule = rule_id

    def test_common(self):
        line = '    id: the id'

        result = self._rule.parseString(line)[0]

        self.assertEqual('the id', result)
