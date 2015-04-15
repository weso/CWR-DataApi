# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getRecordGrammar


"""
CWR Group Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupTrailerGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = getRecordGrammar('group_trailer')

    def test_valid_full(self):
        record = 'GRT000010000017900000719   0000000000'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRT', result.record_type)
        self.assertEqual(1, result.group_id)
        self.assertEqual(179, result.transaction_count)
        self.assertEqual(719, result.record_count)
