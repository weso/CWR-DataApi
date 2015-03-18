# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.interested_party import IPTerritoryOfControlRecord


"""
Publisher or Writer Territory of Control to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPTerritoryOfControlRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = IPTerritoryOfControlRecord(record_type='MSG',
                                          transaction_sequence_n=3,
                                          record_sequence_n=15,
                                          ip_n='FG14',
                                          ie_indicator='I',
                                          tis_numeric_code=76,
                                          sequence_n=135,
                                          pr_col_share=50.5,
                                          mr_col_share=60.5,
                                          sr_col_share=70.5,
                                          shares_change=True)

        encoded = self._encoder.encode(data)

        self.assertEqual('MSG', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('FG14', encoded['ip_n'])
        self.assertEqual('I', encoded['ie_indicator'])
        self.assertEqual(76, encoded['tis_numeric_code'])
        self.assertEqual(135, encoded['sequence_n'])
        self.assertEqual(50.5, encoded['pr_col_share'])
        self.assertEqual(60.5, encoded['mr_col_share'])
        self.assertEqual(70.5, encoded['sr_col_share'])
        self.assertEqual(True, encoded['shares_change'])