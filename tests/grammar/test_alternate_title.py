# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import work_detail


"""
CWR Alternate Title grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAlternateTitleGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.alternate

    def test_valid_full(self):
        record = 'ALT0000123400000023THE TITLE                                                   ATES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ALT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.alternate_title)
        self.assertEqual('AT', result.alternate_title)
        self.assertEqual('ES', result.language)
