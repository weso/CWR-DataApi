# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AgreementTerritoryDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementTerritoryRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AgreementTerritoryDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'TER'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['tis_numeric_code'] = 28
        dict['inclusion_exclusion_indicator'] = 'I'

        record = self._decoder.decode(dict)

        self.assertEqual('TER', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(28, record.tis_numeric_code)
        self.assertEqual('I', record.inclusion_exclusion_indicator)
