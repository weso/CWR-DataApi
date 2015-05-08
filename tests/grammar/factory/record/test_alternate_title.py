# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import get_record_grammar


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
        self.grammar = get_record_grammar('work_alternate_title')

    def test_extended_character(self):
        record = 'ALT0000028200001380PA\xc6\x8f                                                        AT  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ALT', result.record_type)
        self.assertEqual(282, result.transaction_sequence_n)
        self.assertEqual(1380, result.record_sequence_n)
        self.assertEqual('PA\xc6\x8f', result.alternate_title)
        self.assertEqual('AT', result.title_type)
        self.assertEqual(None, result.language_code)

    def test_valid_full(self):
        record = 'ALT0000123400000023THE TITLE                                                   ATES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ALT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.alternate_title)
        self.assertEqual('AT', result.title_type)
        self.assertEqual('ES', result.language_code)
