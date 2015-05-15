# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import NonRomanAlphabetTitleEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetTitleRecord


"""
NATRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNATRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = NonRomanAlphabetTitleEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetTitleRecord(record_type='NAT',
                                           transaction_sequence_n=3,
                                           record_sequence_n=15,
                                           title='THE TITLE',
                                           title_type='FT',
                                           language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('NAT', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('THE TITLE', encoded['title'])
        self.assertEqual('FT', encoded['title_type'])
        self.assertEqual('ES', encoded['language_code'])