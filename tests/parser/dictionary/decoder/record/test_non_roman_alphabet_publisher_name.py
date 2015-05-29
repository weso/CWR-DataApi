# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import \
    NonRomanAlphabetPublisherNameDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNonRomanAlphabetPublisherNameDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetPublisherNameDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'NPN'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['publisher_sequence_n'] = 5
        data['ip_n'] = 'IP123'
        data['publisher_name'] = 'NAME'
        data['language_code'] = 'ES'

        record = self._decoder.decode(data)

        self.assertEqual('NPN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(5, record.publisher_sequence_n)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('NAME', record.publisher_name)
        self.assertEqual('ES', record.language_code)
