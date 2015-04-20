# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import PerformingArtistDictionaryDecoder
from cwr.other import IPIBaseNumber


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPerformingArtistDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = PerformingArtistDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'PER'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['performing_artist_last_name'] = 'LAST NAME'
        dict['performing_artist_first_name'] = 'FIRST NAME'
        dict['performing_artist_ipi_name_n'] = 250165006
        dict['performing_artist_ipi_base_n'] = IPIBaseNumber('I', 229, 7)

        record = self._decoder.decode(dict)

        self.assertEqual('PER', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('LAST NAME', record.performing_artist_last_name)
        self.assertEqual('FIRST NAME', record.performing_artist_first_name)
        self.assertEqual(250165006, record.performing_artist_ipi_name_n)
        self.assertEqual('I', record.performing_artist_ipi_base_n.header)
        self.assertEqual(229, record.performing_artist_ipi_base_n.id_code)
        self.assertEqual(7, record.performing_artist_ipi_base_n.check_digit)