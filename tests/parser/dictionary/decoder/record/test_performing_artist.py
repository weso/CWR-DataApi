# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import PerformingArtistDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPerformingArtistDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = PerformingArtistDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'PER'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['performing_artist_last_name'] = 'LAST NAME'
        data['performing_artist_first_name'] = 'FIRST NAME'
        data['performing_artist_ipi_name_n'] = 250165006
        data['performing_artist_ipi_base_n'] = 'I-000000229-7'

        record = self._decoder.decode(data)

        self.assertEqual('PER', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('LAST NAME', record.performing_artist_last_name)
        self.assertEqual('FIRST NAME', record.performing_artist_first_name)
        self.assertEqual(250165006, record.performing_artist_ipi_name_n)

        self.assertEqual('I-000000229-7', record.performing_artist_ipi_base_n)
