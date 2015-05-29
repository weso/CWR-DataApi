# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import \
    NonRomanAlphabetAgreementPartyDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAgreementTerritoryRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetAgreementPartyDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'NPA'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['ip_name'] = 'NAME'
        data['ip_writer_name'] = 'WRITER'
        data['ip_n'] = 'IP123'
        data['language_code'] = 'ES'

        record = self._decoder.decode(data)

        self.assertEqual('NPA', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('NAME', record.ip_name)
        self.assertEqual('WRITER', record.ip_writer_name)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('ES', record.language_code)
