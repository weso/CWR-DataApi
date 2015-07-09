# -*- coding: utf-8 -*-
import unittest
import time

from cwr.grammar.factory.rule import FieldRuleFactory
from cwr.grammar.factory.adapter import NumericAdapter

"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def _factory():
    adapters = {'numeric': NumericAdapter()}

    config_fields = {
        'test_field': {'type': 'numeric', 'name': 'Test Field',
                       'size': 3}}

    return FieldRuleFactory(config_fields, adapters)


class TestFieldRuleFactory(unittest.TestCase):
    def setUp(self):
        self._factory = _factory()

    def test_10000(self):
        start = time.clock()
        for x in xrange(10000):
            self._factory.get_rule('test_field')
        end = time.clock()

        time_parse = (end - start)

        self.assertLess(time_parse, 1)
