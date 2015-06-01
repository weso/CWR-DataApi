# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAgreementGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('agreement')

    def test_common(self):
        record = 'AGR000000010000000000041383606100              OS200006062017010120170101N        D20170101        00001SYY              '

        result = self.grammar.parseString(record)[0]
        self.assertEqual(1, result.transaction_sequence_n)
        self.assertEqual(0, result.record_sequence_n)
        self.assertEqual('00041383606100', result.submitter_agreement_n)
        self.assertEqual(None, result.international_standard_code)
        self.assertEqual('OS', result.agreement_type)
        self.assertEqual(2000, result.agreement_start_date.year)
        self.assertEqual(6, result.agreement_start_date.month)
        self.assertEqual(6, result.agreement_start_date.day)
        self.assertEqual(2017, result.agreement_end_date.year)
        self.assertEqual(1, result.agreement_end_date.month)
        self.assertEqual(1, result.agreement_end_date.day)
        self.assertEqual(2017, result.retention_end_date.year)
        self.assertEqual(1, result.retention_end_date.month)
        self.assertEqual(1, result.retention_end_date.day)
        self.assertEqual('N', result.prior_royalty_status)
        self.assertEqual(None, result.prior_royalty_start_date)
        self.assertEqual('D', result.post_term_collection_status)
        self.assertEqual(2017, result.post_term_collection_end_date.year)
        self.assertEqual(1, result.post_term_collection_end_date.month)
        self.assertEqual(1, result.post_term_collection_end_date.day)
        self.assertEqual(None, result.date_of_signature)
        self.assertEqual(1, result.number_of_works)
        self.assertEqual('S', result.sales_manufacture_clause)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(True, result.advance_given)
        self.assertEqual(None, result.society_assigned_agreement_n)

        self.assertEqual('AGR', result.record_type)

    def test_valid_full(self):
        """
        Tests that the Agreement grammar parses correctly formatted strings.

        This test contains all the optional fields.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('AGR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('C1234567890123', result.submitter_agreement_n)
        self.assertEqual('D1234567890123', result.international_standard_code)
        self.assertEqual('OG', result.agreement_type)
        self.assertEqual(2012, result.agreement_start_date.year)
        self.assertEqual(1, result.agreement_start_date.month)
        self.assertEqual(2, result.agreement_start_date.day)
        self.assertEqual(2013, result.agreement_end_date.year)
        self.assertEqual(2, result.agreement_end_date.month)
        self.assertEqual(3, result.agreement_end_date.day)
        self.assertEqual(2014, result.retention_end_date.year)
        self.assertEqual(3, result.retention_end_date.month)
        self.assertEqual(4, result.retention_end_date.day)
        self.assertEqual('D', result.prior_royalty_status)
        self.assertEqual(2010, result.prior_royalty_start_date.year)
        self.assertEqual(4, result.prior_royalty_start_date.month)
        self.assertEqual(5, result.prior_royalty_start_date.day)
        self.assertEqual('D', result.post_term_collection_status)
        self.assertEqual(2016, result.post_term_collection_end_date.year)
        self.assertEqual(5, result.post_term_collection_end_date.month)
        self.assertEqual(6, result.post_term_collection_end_date.day)
        self.assertEqual(2017, result.date_of_signature.year)
        self.assertEqual(6, result.date_of_signature.month)
        self.assertEqual(7, result.date_of_signature.day)
        self.assertEqual(1234, result.number_of_works)
        self.assertEqual('M', result.sales_manufacture_clause)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(True, result.advance_given)
        self.assertEqual('0123456789012A', result.society_assigned_agreement_n)

    def test_valid_minimum(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains none of the optional fields.
        """
        record = 'AGR0000123400000023C1234567890123              OG201201020000000000000000N        N00000000        01234 NN              '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('AGR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('C1234567890123', result.submitter_agreement_n)
        self.assertEqual(None, result.international_standard_code)
        self.assertEqual('OG', result.agreement_type)
        self.assertEqual(2012, result.agreement_start_date.year)
        self.assertEqual(1, result.agreement_start_date.month)
        self.assertEqual(2, result.agreement_start_date.day)
        self.assertEqual(None, result.agreement_end_date)
        self.assertEqual(None, result.retention_end_date)
        self.assertEqual('N', result.prior_royalty_status)
        self.assertEqual(None, result.prior_royalty_start_date)
        self.assertEqual('N', result.post_term_collection_status)
        self.assertEqual(None, result.post_term_collection_end_date)
        self.assertEqual(None, result.date_of_signature)
        self.assertEqual(1234, result.number_of_works)
        self.assertEqual(None, result.sales_manufacture_clause)
        self.assertEqual(False, result.shares_change)
        self.assertEqual(False, result.advance_given)
        self.assertEqual(None, result.society_assigned_agreement_n)


class TestAgreementGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('agreement')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
