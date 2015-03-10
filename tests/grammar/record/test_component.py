# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import work_detail


"""
CWR Component grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestComponentGrammar(unittest.TestCase):
    """
    Tests that the NWN grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = work_detail.component

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('COM', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual('ABCD0123456789', result.submitter_id)
        self.assertEqual(3, result.duration.hour)
        self.assertEqual(2, result.duration.minute)
        self.assertEqual(1, result.duration.second)
        self.assertEqual('LAST NAME 1', result.last_name_1)
        self.assertEqual('FIRST NAME 1', result.first_name_1)
        self.assertEqual(14107338, result.ipi_name_1)
        self.assertEqual('LAST NAME 2', result.last_name_2)
        self.assertEqual('FIRST NAME 2', result.first_name_2)
        self.assertEqual(14107339, result.ipi_name_2)
        self.assertEqual('I', result.ipi_base_1.header)
        self.assertEqual(229, result.ipi_base_1.id_code)
        self.assertEqual(7, result.ipi_base_1.check_digit)
        self.assertEqual('I', result.ipi_base_2.header)
        self.assertEqual(230, result.ipi_base_2.id_code)
        self.assertEqual(7, result.ipi_base_2.check_digit)