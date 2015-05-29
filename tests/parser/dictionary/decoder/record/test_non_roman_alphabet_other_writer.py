# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import NonRomanAlphabetOtherWriterDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNonRomanAlphabetOtherWriterDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetOtherWriterDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'NOW'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['writer_first_name'] = 'FIRST NAME'
        data['writer_name'] = 'NAME'
        data['position'] = 21
        data['language_code'] = 'ES'

        record = self._decoder.decode(data)

        self.assertEqual('NOW', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('FIRST NAME', record.writer_first_name)
        self.assertEqual('NAME', record.writer_name)
        self.assertEqual(21, record.position)
        self.assertEqual('ES', record.language_code)
