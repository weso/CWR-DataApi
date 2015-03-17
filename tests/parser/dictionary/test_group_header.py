# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.group import GroupHeader


"""
Group Header to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TesGroupHeaderDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = GroupHeader(record_type='GRH',
                           group_id=3,
                           transaction_type='AGR',
                           version_number='02.10',
                           batch_request_id=15)

        encoded = self._encoder.encode(data)

        self.assertEqual('GRH', encoded['record_type'])
        self.assertEqual(3, encoded['group_id'])
        self.assertEqual('AGR', encoded['transaction_type'])
        self.assertEqual('02.10', encoded['version_number'])
        self.assertEqual(15, encoded['batch_request_id'])