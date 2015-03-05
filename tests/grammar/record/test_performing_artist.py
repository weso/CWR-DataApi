# -*- encoding: utf-8 -*-
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
        self.assertEqual('LAST NAME', result.last_name)
        self.assertEqual('FIRST NAME', result.first_name)
        self.assertEqual(14107338, result.ipi_name)
        self.assertEqual('I', result.ipi_base_number.header)
        self.assertEqual(229, result.ipi_base_number.id_code)
        self.assertEqual(7, result.ipi_base_number.check_digit)
