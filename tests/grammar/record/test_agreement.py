# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.record import agreement

"""
CWR agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGrammarAgreement(unittest.TestCase):
    def setUp(self):
        self.grammar = agreement.agreement

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
        self.assertEqual(2010, result.prior_royalty_start_date.year)
        self.assertEqual(4, result.prior_royalty_start_date.month)
        self.assertEqual(5, result.prior_royalty_start_date.day)
        self.assertEqual('D', result.post_term_collection_status)
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

    def test_valid_minimum(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains none of the optional fields.
        """
        record = 'AGR0000123400000023C1234567890123              OG201201020000000000000000N00000000N000000000000000001234 NN              '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('AGR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('C1234567890123', result.agreement_id)
        self.assertEqual('', result.international_standard_code)
        self.assertEqual('OG', result.agreement_type)
        self.assertEqual(2012, result.start_date.year)
        self.assertEqual(1, result.start_date.month)
        self.assertEqual(2, result.start_date.day)
        self.assertEqual(None, result.end_date)
        self.assertEqual(None, result.retention_end_date)
        self.assertEqual('N', result.prior_royalty_status)
        self.assertEqual(None, result.prior_royalty_start_date)
        self.assertEqual('N', result.post_term_collection_status)
        self.assertEqual(None, result.post_term_collection_end_date)
        self.assertEqual(None, result.signature_date)
        self.assertEqual(1234, result.works_number)
        self.assertEqual(None, result.sales_manufacture_clause)
        self.assertEqual(False, result.shares_change)
        self.assertEqual(False, result.advance_given)
        self.assertEqual('', result.society_agreement_number)


class TestGrammarGroupHeaderException(unittest.TestCase):
    def setUp(self):
        self.grammar = agreement.agreement

    def test_works_zero(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060700000MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_missing_agreement_id(self):
        """
        Tests that a exception is thrown when the Submitter Agreement Number is missing.
        """
        record = 'AGR0000123400000023              D1234567890123OG201201022013020320140304D20100405O201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_prior_royalty_missing_date(self):
        """
        Tests that a exception is thrown when the Prior Royalty Status is set to Date and this date is missing.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D00000000D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_prior_royalty_none_and_date(self):
        """
        Tests that a exception is thrown when the Prior Royalty Status is set to None and the date is set.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304N20100405D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_prior_royalty_all_and_date(self):
        """
        Tests that a exception is thrown when the Prior Royalty Status is set to All and the date is set.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304A20100405D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_missing_date(self):
        """
        Tests that a exception is thrown when the Post Term Collection Status is set to Date and this date is missing.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D000000002017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_none_and_date(self):
        """
        Tests that a exception is thrown when the Post Term Collection Status is set to None and the date is set.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405N201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_open_and_date(self):
        """
        Tests that a exception is thrown when the Post Term Collection Status is set to Open and the date is set.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405O201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_retention_end_and_no_agreement_end(self):
        """
        Tests that a exception is thrown when the Retention End Date is set but not the Agreement End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201020000000020140304D20100405D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_retention_end_before_agreement_end(self):
        """
        Tests that a exception is thrown when the Retention End Date is set before the Agreement End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022020010120140304D20100405D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_prior_royalty_start_after_agreement_start(self):
        """
        Tests that a exception is thrown when the Retention End Date is set before the Agreement End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20150405D201605062017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_end_before_retention_end(self):
        """
        Tests that a exception is thrown when the Post Term Collection End Date is set before the Retention End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201401012017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_end_before_agreement_end_with_retention(self):
        """
        Tests that a exception is thrown when the Post Term Collection End Date is set before the Agreement End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201201012017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_post_term_collection_end_before_agreement_end_without_retention(self):
        """
        Tests that am exception is thrown when the Post Term Collection End Date is set before the Agreement End Date.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020300000000D20100405D201201012017060701234MYY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_no_sm_clause_for_op(self):
        """
        Tests that am exception is thrown when the Sales/Manufacture Clause is not set for an Agreement which requires it.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OP201201022013020320140304D20100405D201605062017060701234 YY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_no_sm_clause_for_os(self):
        """
        Tests that am exception is thrown when the Sales/Manufacture Clause is not set for an Agreement which requires it.
        """
        record = 'AGR0000123400000023C1234567890123D1234567890123OS201201022013020320140304D20100405D201605062017060701234 YY0123456789012A'

        self.assertRaises(ParseException, self.grammar.parseString, record)
