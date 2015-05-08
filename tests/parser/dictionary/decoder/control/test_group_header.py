# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import GroupHeaderDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupHeaderDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = GroupHeaderDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'GRH'
        dict['group_id'] = 5
        dict['transaction_type'] = 'AGR'
        dict['version_number'] = '02.10'
        dict['batch_request_id'] = 123456789

        record = self._decoder.decode(dict)

        self.assertEqual('GRH', record.record_type)
        self.assertEqual(5, record.group_id)
        self.assertEqual('AGR', record.transaction_type)
        self.assertEqual('02.10', record.version_number)
        self.assertEqual(123456789, record.batch_request_id)