# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import TransmissionTrailerDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestTransmissionTrailerDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = TransmissionTrailerDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'TRL'
        dict['group_count'] = 11
        dict['transaction_count'] = 22
        dict['record_count'] = 33

        record = self._decoder.decode(dict)

        self.assertEqual('TRL', record.record_type)
        self.assertEqual(11, record.group_count)
        self.assertEqual(22, record.transaction_count)
        self.assertEqual(33, record.record_count)
