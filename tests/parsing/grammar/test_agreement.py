# -*- encoding: utf-8 -*-
import unittest

from cwr.parsing.grammar import agreement

"""
CWR agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGrammarGroupHeader(unittest.TestCase):
    def test_valid_full(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20150405O201605062017060701234MYY0123456789012A'

        result = agreement.agreement.parseString(record)[0]

        self.assertEqual('AGR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('C1234567890123', result.agreement_id)
        self.assertEqual('D1234567890123', result.international_standard_code)
        self.assertEqual('OG', result.agreement_type)
        self.assertEqual(2012, result.start_date.year)
        self.assertEqual(1, result.start_date.month)
        self.assertEqual(2, result.start_date.day)
        self.assertEqual(2013, result.end_date.year)
        self.assertEqual(2, result.end_date.month)
        self.assertEqual(3, result.end_date.day)
        self.assertEqual(2014, result.retention_end_date.year)
        self.assertEqual(3, result.retention_end_date.month)
        self.assertEqual(4, result.retention_end_date.day)
        self.assertEqual('D', result.prior_royalty_status)
        self.assertEqual(2015, result.prior_royalty_start_date.year)
        self.assertEqual(4, result.prior_royalty_start_date.month)
        self.assertEqual(5, result.prior_royalty_start_date.day)
        self.assertEqual('O', result.post_term_collection_status)
        self.assertEqual(2016, result.post_term_collection_end_date.year)
        self.assertEqual(5, result.post_term_collection_end_date.month)
        self.assertEqual(6, result.post_term_collection_end_date.day)
        self.assertEqual(2017, result.signature_date.year)
        self.assertEqual(6, result.signature_date.month)
        self.assertEqual(7, result.signature_date.day)
        self.assertEqual(1234, result.works_number)
        self.assertEqual('M', result.sales_manufacture_clause)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(True, result.advance_given)
        self.assertEqual('0123456789012A', result.society_agreement_number)