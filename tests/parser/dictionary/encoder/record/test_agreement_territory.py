# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import AgreementTerritoryDictionaryEncoder
from cwr.agreement import AgreementTerritoryRecord


"""
AgreementRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementTerritoryRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = AgreementTerritoryDictionaryEncoder()

    def test_encoded(self):
        data = AgreementTerritoryRecord(record_type='TER',
                                        transaction_sequence_n=3,
                                        record_sequence_n=15,
                                        tis_numeric_code=51,
                                        inclusion_exclusion_indicator='I')

        encoded = self._encoder.encode(data)

        self.assertEqual('TER', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(51, encoded['tis_numeric_code'])
        self.assertEqual('I', encoded['inclusion_exclusion_indicator'])