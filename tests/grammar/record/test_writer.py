# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import writer


"""
CWR Writer grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWriterGrammar(unittest.TestCase):
    """
    Tests that the Writer grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = writer.writer

    def test_valid_full(self):
        """
        Tests that Writer grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SWR0000123400000023A12345678LAST NAME                                    FIRST NAME                    NA 92370341200014107338009020500100300001102312YYY I-000000229-7012345678901B'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SWR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.writer.ip_id)
        self.assertEqual('LAST NAME', result.writer.writer_last_name)
        self.assertEqual('FIRST NAME', result.writer.writer_first_name)
        self.assertEqual('N', result.writer_unknown)
        self.assertEqual('A', result.writer_designation)
        self.assertEqual(923703412, result.writer.tax_id)
        self.assertEqual(14107338, result.writer.ipi_name_n)
        self.assertEqual(9, result.pr_society)
        self.assertEqual(20.5, result.pr_ownership_share)
        self.assertEqual(10, result.mr_society)
        self.assertEqual(30, result.mr_ownership_share)
        self.assertEqual(11, result.sr_society)
        self.assertEqual(23.12, result.sr_ownership_share)
        self.assertEqual('Y', result.reversionary)
        self.assertEqual('Y', result.first_recording_refusal)
        self.assertEqual('Y', result.work_for_hire)
        self.assertEqual('I', result.writer.ipi_base_n.header)
        self.assertEqual(229, result.writer.ipi_base_n.id_code)
        self.assertEqual(7, result.writer.ipi_base_n.check_digit)
        self.assertEqual(12345678901, result.writer.personal_number)
        self.assertEqual('B', result.usa_license)