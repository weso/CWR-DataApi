# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.work import InstrumentationDetailRecord


"""
InstrumentationDetailRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestRecordingDetailRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = InstrumentationDetailRecord(record_type='SWR',
                                           transaction_sequence_n=3,
                                           record_sequence_n=15,
                                           instrument_code='AHN',
                                           number_players=2)

        encoded = self._encoder.encode(data)

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('AHN', encoded['instrument_code'])
        self.assertEqual(2, encoded['number_players'])