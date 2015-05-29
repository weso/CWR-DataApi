# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import NonRomanAlphabetPerformanceDataDictionaryDecoder
from cwr.other import IPIBaseNumber

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNonRomanAlphabetPerformanceDataDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = NonRomanAlphabetPerformanceDataDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'NPR'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['performing_artist_first_name'] = 'FIRST NAME'
        data['performing_artist_name'] = 'NAME'
        data['performing_artist_ipi_name_n'] = 250165006
        data['performing_artist_ipi_base_n'] = IPIBaseNumber('I', 229, 7)
        data['language_code'] = 'ES'
        data['performance_language'] = 'EN'
        data['performance_dialect'] = 'EUS'

        record = self._decoder.decode(data)

        self.assertEqual('NPR', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('FIRST NAME', record.performing_artist_first_name)
        self.assertEqual('NAME', record.performing_artist_name)
        self.assertEqual(250165006, record.performing_artist_ipi_name_n)
        self.assertEqual('I', record.performing_artist_ipi_base_n.header)
        self.assertEqual(229, record.performing_artist_ipi_base_n.id_code)
        self.assertEqual(7, record.performing_artist_ipi_base_n.check_digit)
        self.assertEqual('ES', record.language_code)
        self.assertEqual('EN', record.performance_language)
        self.assertEqual('EUS', record.performance_dialect)
