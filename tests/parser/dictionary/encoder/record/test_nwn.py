# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetWriterNameRecord


"""
NWNRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPRRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetWriterNameRecord(record_type='NWN',
                                                transaction_sequence_n=3,
                                                record_sequence_n=15,
                                                writer_first_name='FIRST NAME',
                                                writer_last_name='LAST NAME',
                                                ip_n='ABC123',
                                                language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('NWN', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('FIRST NAME', encoded['writer_first_name'])
        self.assertEqual('LAST NAME', encoded['writer_last_name'])
        self.assertEqual('ABC123', encoded['ip_n'])
        self.assertEqual('ES', encoded['language_code'])