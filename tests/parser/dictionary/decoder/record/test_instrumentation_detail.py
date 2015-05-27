# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import InstrumentationDetailDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestInstrumentationDetailDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = InstrumentationDetailDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'IND'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['instrument_code'] = 'AHN'
        dict['number_players'] = 2

        record = self._decoder.decode(dict)

        self.assertEqual('IND', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('AHN', record.instrument_code)
        self.assertEqual(2, record.number_players)
