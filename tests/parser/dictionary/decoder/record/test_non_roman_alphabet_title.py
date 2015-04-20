# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import NonRomanAlphabetTitleDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNonRomanAlphabetTitleDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetTitleDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'NAT'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['title'] = 'TITLE'
        dict['title_type'] = 'OL'
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('NAT', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('TITLE', record.title)
        self.assertEqual('OL', record.title_type)
        self.assertEqual('ES', record.language_code)