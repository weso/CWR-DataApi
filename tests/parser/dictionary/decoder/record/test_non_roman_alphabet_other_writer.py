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
        dict = {}

        dict['record_type'] = 'NOW'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['writer_first_name'] = 'FIRST NAME'
        dict['writer_name'] = 'NAME'
        dict['position'] = 21
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('NOW', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('FIRST NAME', record.writer_first_name)
        self.assertEqual('NAME', record.writer_name)
        self.assertEqual(21, record.position)
        self.assertEqual('ES', record.language_code)
