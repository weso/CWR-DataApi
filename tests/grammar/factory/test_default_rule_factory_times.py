# -*- coding: utf-8 -*-
import unittest
import time
import sys

from cwr.parser.decoder.file import default_grammar_factory

"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestDefaultRuleFactory(unittest.TestCase):
    def setUp(self):
        self._factory = default_grammar_factory()

    def test_10000(self):
        start = time.clock()
        if sys.version_info[0] == 2:
            for x in xrange(10000):
                self._factory.get_rule('transmission')
        else:
            for x in range(10000):
                self._factory.get_rule('transmission')
        end = time.clock()

        time_parse = (end - start)

        self.assertTrue(time_parse < 2)
