# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import InstrumentationSummaryEncoder
from cwr.work import InstrumentationSummaryRecord


"""
InstrumentationSummaryRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestRecordingDetailRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = InstrumentationSummaryEncoder()

    def test_encoded(self):
        data = InstrumentationSummaryRecord(record_type='SWR',
                                            transaction_sequence_n=3,
                                            record_sequence_n=15,
                                            number_voices=2,
                                            standard_instrumentation_type='BQU',
                                            instrumentation_description='DESCRIPTION')

        encoded = self._encoder.encode(data)

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(2, encoded['number_voices'])
        self.assertEqual('BQU', encoded['standard_instrumentation_type'])
        self.assertEqual('DESCRIPTION', encoded['instrumentation_description'])