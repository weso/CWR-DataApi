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


class TestGroupHeaderGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = getRecordGrammar('group_header')

    def test_valid_full(self):
        record = 'GRHAGR0000102.100130400001  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual(1, result.group_id)
        self.assertEqual('AGR', result.transaction_type)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(130400001, result.batch_request_id)
