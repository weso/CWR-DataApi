# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.nra import NPNRecord


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
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = NPNRecord(record_type='NPN',
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