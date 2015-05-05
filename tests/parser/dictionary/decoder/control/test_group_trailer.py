# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import GroupTrailerDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupTrailerDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = GroupTrailerDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'GRH'
        dict['group_id'] = 5
        dict['transaction_type'] = 'AGR'
        dict['transaction_count'] = 111
        dict['record_count'] = 222

        record = self._decoder.decode(dict)

        self.assertEqual('GRH', record.record_type)
        self.assertEqual(5, record.group_id)
        self.assertEqual(111, record.transaction_count)
        self.assertEqual(222, record.record_count)