# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AlternateTitleDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAlternateTitleDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AlternateTitleDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'ALT'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['alternate_title'] = 'ALTERNATE TITLE'
        data['title_type'] = 'FT'
        data['language_code'] = 'ES'

        record = self._decoder.decode(data)

        self.assertEqual('ALT', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('ALTERNATE TITLE', record.alternate_title)
        self.assertEqual('FT', record.title_type)
        self.assertEqual('ES', record.language_code)
