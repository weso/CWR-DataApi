# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import work_detail


"""
CWR Performing Artist grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPerformingArtistGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.performing

    def test_valid_full(self):
        record = 'PER0000123400000023LAST NAME                                    FIRST NAME                    00014107338I-000000229-7'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('PER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('LAST NAME', result.performing_artist_last_name)
        self.assertEqual('FIRST NAME', result.performing_artist_first_name)
        self.assertEqual(14107338, result.performing_artist_ipi_name_n)
        self.assertEqual('I', result.performing_artist_ipi_base_n.header)
        self.assertEqual(229, result.performing_artist_ipi_base_n.id_code)
        self.assertEqual(7, result.performing_artist_ipi_base_n.check_digit)
