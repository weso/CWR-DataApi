# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import NonRomanAlphabetWriterNameDictionaryDecoder

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
        dict = {}

        dict['record_type'] = 'NPN'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['writer_first_name'] = 'FIRST NAME'
        dict['writer_last_name'] = 'LAST NAME'
        dict['ip_n'] = 'IP123'
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('NPN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('FIRST NAME', record.writer_first_name)
        self.assertEqual('LAST NAME', record.writer_last_name)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('ES', record.language_code)
