# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import \
    NonRomanAlphabetPerformanceDataDictionaryEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetPerformanceDataRecord

"""
NPRRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNPRRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = NonRomanAlphabetPerformanceDataDictionaryEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetPerformanceDataRecord(record_type='NPA',
                                                     transaction_sequence_n=3,
                                                     record_sequence_n=15,
                                                     performing_artist_first_name='FIRST NAME',
                                                     performing_artist_name='NAME',
                                                     performing_artist_ipi_name_n=14107338,
                                                     performing_artist_ipi_base_n='I-000000229-7',
                                                     language_code='ES',
                                                     performance_language='EN',
                                                     performance_dialect='SC')

        encoded = self._encoder.encode(data)

        self.assertEqual('NPA', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('FIRST NAME', encoded['performing_artist_first_name'])
        self.assertEqual('NAME', encoded['performing_artist_name'])
        self.assertEqual(14107338, encoded['performing_artist_ipi_name_n'])
        self.assertEqual('I-000000229-7',
                         encoded['performing_artist_ipi_base_n'])
        self.assertEqual('ES', encoded['language_code'])
        self.assertEqual('EN', encoded['performance_language'])
        self.assertEqual('SC', encoded['performance_dialect'])
