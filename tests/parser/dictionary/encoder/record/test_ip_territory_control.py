# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import IPTerritoryOfControlDictionaryEncoder
from cwr.interested_party import IPTerritoryOfControlRecord

"""
Publisher or Writer Territory of Control to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestIPTerritoryOfControlRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = IPTerritoryOfControlDictionaryEncoder()

    def test_encoded(self):
        data = IPTerritoryOfControlRecord(record_type='MSG',
                                          transaction_sequence_n=3,
                                          record_sequence_n=15,
                                          ip_n='FG14',
                                          inclusion_exclusion_indicator='I',
                                          tis_numeric_code=76,
                                          sequence_n=135,
                                          pr_collection_share=50.5,
                                          mr_collection_share=60.5,
                                          sr_collection_share=70.5,
                                          shares_change=True)

        encoded = self._encoder.encode(data)

        self.assertEqual('MSG', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('FG14', encoded['ip_n'])
        self.assertEqual('I', encoded['inclusion_exclusion_indicator'])
        self.assertEqual(76, encoded['tis_numeric_code'])
        self.assertEqual(135, encoded['sequence_n'])
        self.assertEqual(50.5, encoded['pr_collection_share'])
        self.assertEqual(60.5, encoded['mr_collection_share'])
        self.assertEqual(70.5, encoded['sr_collection_share'])
        self.assertEqual(True, encoded['shares_change'])
