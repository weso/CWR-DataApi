# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar


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
        self.grammar = get_record_grammar('writer')

    def test_valid_common(self):
        """
        Tests that Writer grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SWR00000179000005481178518  SURNAME                                      NAME                           C          0026169554761 0050061 0000061 00000    0000000000000             '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SWR', result.record_type)
        self.assertEqual(179, result.transaction_sequence_n)
        self.assertEqual(548, result.record_sequence_n)
        self.assertEqual('1178518', result.writer.ip_n)
        self.assertEqual('SURNAME', result.writer.writer_last_name)
        self.assertEqual('NAME', result.writer.writer_first_name)
        self.assertEqual(None, result.writer_unknown)
        self.assertEqual('C', result.writer_designation)
        self.assertEqual(None, result.writer.tax_id)
        self.assertEqual(261695547, result.writer.ipi_name_n)
        self.assertEqual(61, result.pr_society)
        self.assertEqual(5, result.pr_ownership_share)
        self.assertEqual(61, result.mr_society)
        self.assertEqual(0, result.mr_ownership_share)
        self.assertEqual(61, result.sr_society)
        self.assertEqual(0, result.sr_ownership_share)
        self.assertEqual(None, result.reversionary)
        self.assertEqual(None, result.first_recording_refusal)
        self.assertEqual(None, result.work_for_hire)
        self.assertEqual(0, result.writer.ipi_base_n)
        self.assertEqual(None, result.writer.personal_number)
        self.assertEqual(None, result.usa_license)

    def test_valid_common_b(self):
        """
        Tests that Writer grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'OWR00000286000014241178514  SURNAME                                      NAME                           CA         0000000000061 0600061 0600061 06000    0000000000000             '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('OWR', result.record_type)
        self.assertEqual(286, result.transaction_sequence_n)
        self.assertEqual(1424, result.record_sequence_n)
        self.assertEqual('1178514', result.writer.ip_n)
        self.assertEqual('SURNAME', result.writer.writer_last_name)
        self.assertEqual('NAME', result.writer.writer_first_name)
        self.assertEqual(None, result.writer_unknown)
        self.assertEqual('CA', result.writer_designation)
        self.assertEqual(None, result.writer.tax_id)
        self.assertEqual(0, result.writer.ipi_name_n)
        self.assertEqual(61, result.pr_society)
        self.assertEqual(60, result.pr_ownership_share)
        self.assertEqual(61, result.mr_society)
        self.assertEqual(60, result.mr_ownership_share)
        self.assertEqual(61, result.sr_society)
        self.assertEqual(60, result.sr_ownership_share)
        self.assertEqual(None, result.reversionary)
        self.assertEqual(None, result.first_recording_refusal)
        self.assertEqual(None, result.work_for_hire)
        self.assertEqual(0, result.writer.ipi_base_n)
        self.assertEqual(None, result.writer.personal_number)
        self.assertEqual(None, result.usa_license)

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
        self.assertEqual('A12345678', result.writer.ip_n)
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


class TestWriterGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('writer')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)