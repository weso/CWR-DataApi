# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import NonRomanAlphabetAgreementPartyDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementTerritoryRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetAgreementPartyDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'NPA'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['ip_name'] = 'NAME'
        dict['ip_writer_name'] = 'WRITER'
        dict['ip_n'] = 'IP123'
        dict['language_code'] = 'ES'

        record = self._decoder.decode(dict)

        self.assertEqual('NPA', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('NAME', record.ip_name)
        self.assertEqual('WRITER', record.ip_writer_name)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('ES', record.language_code)