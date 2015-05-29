# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import InstrumentationSummaryDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestInstrumentationSummaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = InstrumentationSummaryDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'SWR'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['number_voices'] = 2
        data['standard_instrumentation_type'] = 'BQU'
        data['instrumentation_description'] = 'DESCRIPTION'

        record = self._decoder.decode(data)

        self.assertEqual('SWR', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(2, record.number_voices)
        self.assertEqual('BQU', record.standard_instrumentation_type)
        self.assertEqual('DESCRIPTION', record.instrumentation_description)
