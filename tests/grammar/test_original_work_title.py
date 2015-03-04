# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import work_detail


"""
CWR Original Work Title for Versions grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestOriginalWorkTitleGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.version

    def test_valid_full(self):
        record = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('VER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('LAST NAME 1', result.last_name_1)
        self.assertEqual('FIRST NAME 1', result.first_name_1)
        self.assertEqual('THE SOURCE', result.source)
        self.assertEqual(14107338, result.ipi_name_1)
        self.assertEqual('I', result.ipi_base_1.header)
        self.assertEqual(229, result.ipi_base_1.id_code)
        self.assertEqual(7, result.ipi_base_1.check_digit)
        self.assertEqual('LAST NAME 2', result.last_name_2)
        self.assertEqual('FIRST NAME 2', result.first_name_2)
        self.assertEqual(14107339, result.ipi_name_2)
        self.assertEqual('I', result.ipi_base_2.header)
        self.assertEqual(230, result.ipi_base_2.id_code)
        self.assertEqual(7, result.ipi_base_2.check_digit)
        self.assertEqual('ABCD0123456789', result.work_id)
