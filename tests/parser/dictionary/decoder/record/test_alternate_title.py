# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AlternateTitleDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAlternateTitleDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AlternateTitleDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'ALT'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['alternate_title'] = 'ALTERNATE TITLE'
        dict['title_type'] = 'FT'
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('ALT', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('ALTERNATE TITLE', record.alternate_title)
        self.assertEqual('FT', record.title_type)
        self.assertEqual('ES', record.language_code)
