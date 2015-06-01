# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AgreementTerritoryDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAgreementTerritoryRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AgreementTerritoryDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'TER'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['tis_numeric_code'] = 28
        data['inclusion_exclusion_indicator'] = 'I'

        record = self._decoder.decode(data)

        self.assertEqual('TER', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(28, record.tis_numeric_code)
        self.assertEqual('I', record.inclusion_exclusion_indicator)
