# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.record import ipa


"""
CWR Interested Party in Agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPAGrammar(unittest.TestCase):
    """
    Tests that the IPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = ipa.ipa

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('IPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('AC', result.agreement_role_code)
        self.assertEqual('I', result.ipi_base.header)
        self.assertEqual(229, result.ipi_base.id_code)
        self.assertEqual(7, result.ipi_base.check_digit)
        self.assertEqual(1234567890, result.ipi_name)
        self.assertEqual('A12345678', result.ip_id)
        self.assertEqual('LAST NAME', result.last_name)
        self.assertEqual('FIRST NAME', result.writer_name)
        self.assertEqual(9, result.pr_society)
        self.assertEqual(20.5, result.pr_share)
        self.assertEqual(10, result.mr_society)
        self.assertEqual(30, result.mr_share)
        self.assertEqual(11, result.sr_society)
        self.assertEqual(023.12, result.sr_share)

    def test_societies_lowest(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains the lowest possible society values.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    000020500000300000002312'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('IPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('AC', result.agreement_role_code)
        self.assertEqual('I', result.ipi_base.header)
        self.assertEqual(229, result.ipi_base.id_code)
        self.assertEqual(7, result.ipi_base.check_digit)
        self.assertEqual(1234567890, result.ipi_name)
        self.assertEqual('A12345678', result.ip_id)
        self.assertEqual('LAST NAME', result.last_name)
        self.assertEqual('FIRST NAME', result.writer_name)
        self.assertEqual(0, result.pr_society)
        self.assertEqual(20.5, result.pr_share)
        self.assertEqual(0, result.mr_society)
        self.assertEqual(30, result.mr_share)
        self.assertEqual(0, result.sr_society)
        self.assertEqual(023.12, result.sr_share)

    def test_valid_minimum(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'IPA0000123400000023AS00000000000             A12345678LAST NAME                                                                     00000   00000   00000'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('IPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('AS', result.agreement_role_code)
        self.assertEqual(None, result.ipi_base)
        self.assertEqual(0, result.ipi_name)
        self.assertEqual('A12345678', result.ip_id)
        self.assertEqual('LAST NAME', result.last_name)
        self.assertEqual('', result.writer_name)
        self.assertEqual(None, result.pr_society)
        self.assertEqual(0, result.pr_share)
        self.assertEqual(None, result.mr_society)
        self.assertEqual(0, result.mr_share)
        self.assertEqual(None, result.sr_society)
        self.assertEqual(0, result.sr_share)


class TestIPAGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = ipa.ipa

    def test_acquiror_missing_shares(self):
        """
        Tests that a exception is thrown when the IPA is an acquiror but no shares have been set.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009000000100000001100000'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_acquiror_missing_societies(self):
        """
        Tests that a exception is thrown when the IPA is an acquiror but no rights society have been set.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                       00205   03000   02312'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_pr_shares_missing_society(self):
        """
        Tests that a exception is thrown when PR shares have been set but no PR society is set.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                       020500010300000102312'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_mr_shares_missing_society(self):
        """
        Tests that a exception is thrown when MR shares have been set but no MR society is set.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    00102050   0300000102312'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_sr_shares_missing_society(self):
        """
        Tests that a exception is thrown when SR shares have been set but no SR society is set.
        """
        record = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    0010205000103000   02312'

        self.assertRaises(ParseException, self.grammar.parseString, record)