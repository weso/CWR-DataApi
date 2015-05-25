# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import IPTerritoryOfControlDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPTerritoryOfControlDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = IPTerritoryOfControlDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'SPT'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['ip_n'] = 'IP123'
        dict['inclusion_exclusion_indicator'] = 'I'
        dict['tis_numeric_code'] = 12
        dict['sequence_n'] = 13
        dict['pr_collection_share'] = 50.1
        dict['mr_collection_share'] = 50.2
        dict['sr_collection_share'] = 50.3
        dict['shares_change'] = 'Y'

        record = self._decoder.decode(dict)

        self.assertEqual('SPT', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('I', record.inclusion_exclusion_indicator)
        self.assertEqual(12, record.tis_numeric_code)
        self.assertEqual(13, record.sequence_n)
        self.assertEqual(50.1, record.pr_collection_share)
        self.assertEqual(50.2, record.mr_collection_share)
        self.assertEqual(50.3, record.sr_collection_share)
        self.assertEqual('Y', record.shares_change)
