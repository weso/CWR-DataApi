# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import NonRomanAlphabetPublisherNameEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetPublisherNameRecord


"""
NPNRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPNRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = NonRomanAlphabetPublisherNameEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetPublisherNameRecord(record_type='NPN',
                                                   transaction_sequence_n=3,
                                                   record_sequence_n=15,
                                                   publisher_sequence_n=17,
                                                   ip_n='ABC123',
                                                   publisher_name='NAME',
                                                   language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('NPN', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(17, encoded['publisher_sequence_n'])
        self.assertEqual('ABC123', encoded['ip_n'])
        self.assertEqual('NAME', encoded['publisher_name'])
        self.assertEqual('ES', encoded['language_code'])