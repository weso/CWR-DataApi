# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import NonRomanAlphabetPublisherNameDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNonRomanAlphabetPublisherNameDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetPublisherNameDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'NPN'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['publisher_sequence_n'] = 5
        dict['ip_n'] = 'IP123'
        dict['publisher_name'] = 'NAME'
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('NPN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(5, record.publisher_sequence_n)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('NAME', record.publisher_name)
        self.assertEqual('ES', record.language_code)
