# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import PerformingArtistDictionaryEncoder
from cwr.work import PerformingArtistRecord
from cwr.other import IPIBaseNumber

"""
PerformingArtistRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPerformingArtistRecordRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = PerformingArtistDictionaryEncoder()

    def test_encoded(self):
        ipi_base = IPIBaseNumber('I', 229, 7)

        data = PerformingArtistRecord(record_type='PER',
                                      transaction_sequence_n=3,
                                      record_sequence_n=15,
                                      performing_artist_last_name='LAST NAME',
                                      performing_artist_first_name='FIRST NAME',
                                      performing_artist_ipi_name_n=14107338,
                                      performing_artist_ipi_base_n=ipi_base)

        encoded = self._encoder.encode(data)

        self.assertEqual('PER', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('LAST NAME', encoded['performing_artist_last_name'])
        self.assertEqual('FIRST NAME', encoded['performing_artist_first_name'])
        self.assertEqual(14107338, encoded['performing_artist_ipi_name_n'])

        self.assertEqual('I', encoded['performing_artist_ipi_base_n']['header'])
        self.assertEqual(229,
                         encoded['performing_artist_ipi_base_n']['id_code'])
        self.assertEqual(7,
                         encoded['performing_artist_ipi_base_n']['check_digit'])
