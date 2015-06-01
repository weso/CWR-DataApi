# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import \
    NonRomanAlphabetWriterNameDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNonRomanAlphabetWriterNameDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetWriterNameDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'NPN'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['writer_first_name'] = 'FIRST NAME'
        data['writer_last_name'] = 'LAST NAME'
        data['ip_n'] = 'IP123'
        data['language_code'] = 'ES'

        record = self._decoder.decode(data)

        self.assertEqual('NPN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('FIRST NAME', record.writer_first_name)
        self.assertEqual('LAST NAME', record.writer_last_name)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('ES', record.language_code)
