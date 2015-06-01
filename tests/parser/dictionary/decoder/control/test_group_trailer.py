# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import GroupTrailerDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestGroupTrailerDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = GroupTrailerDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'GRH'
        data['group_id'] = 5
        data['transaction_type'] = 'AGR'
        data['transaction_count'] = 111
        data['record_count'] = 222

        record = self._decoder.decode(data)

        self.assertEqual('GRH', record.record_type)
        self.assertEqual(5, record.group_id)
        self.assertEqual(111, record.transaction_count)
        self.assertEqual(222, record.record_count)
