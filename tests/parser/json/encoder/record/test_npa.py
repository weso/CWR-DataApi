# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.encoder.cwrjson import JSONEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetAgreementPartyRecord


"""
NOWRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPARecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetAgreementPartyRecord(record_type='NPA',
                                                    transaction_sequence_n=3,
                                                    record_sequence_n=15,
                                                    ip_name='NAME',
                                                    ip_writer_name='WRITER NAME',
                                                    ip_n='ABC123',
                                                    language_code='ES')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('NPA', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('NAME', encoded['ip_name'])
        self.assertEqual('WRITER NAME', encoded['ip_writer_name'])
        self.assertEqual('ABC123', encoded['ip_n'])
        self.assertEqual('ES', encoded['language_code'])