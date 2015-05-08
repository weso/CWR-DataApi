# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import get_record_grammar


"""
CWR Publisher Territory of Control (SPT) grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPNGrammar(unittest.TestCase):
    """
    Tests that the NPN grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('publisher_territory')

    def test_valid_common(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT000001790000054770             013330133301333I0484Y001'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(179, result.transaction_sequence_n)
        self.assertEqual(547, result.record_sequence_n)
        self.assertEqual('70', result.ip_n)
        self.assertEqual(13.33, result.pr_collection_share)
        self.assertEqual(13.33, result.mr_collection_share)
        self.assertEqual(13.33, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(484, result.tis_numeric_code)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(1, result.sequence_n)

    def test_valid_common_short(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT0000000100000002160694172      050000500000000I0484N01'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(1, result.transaction_sequence_n)
        self.assertEqual(2, result.record_sequence_n)
        self.assertEqual('160694172', result.ip_n)
        self.assertEqual(50, result.pr_collection_share)
        self.assertEqual(50, result.mr_collection_share)
        self.assertEqual(0, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(484, result.tis_numeric_code)
        self.assertEqual(False, result.shares_change)
        self.assertEqual(1, result.sequence_n)

    def test_valid_full(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT0000123400000023A12345678      010120500002520I0008Y012'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.ip_n)
        self.assertEqual(10.12, result.pr_collection_share)
        self.assertEqual(50, result.mr_collection_share)
        self.assertEqual(25.2, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(8, result.tis_numeric_code)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(12, result.sequence_n)

    def test_valid_min(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT0000000100000001               000000000000000I0008Y012'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(1, result.transaction_sequence_n)
        self.assertEqual(1, result.record_sequence_n)
        self.assertEqual(None, result.ip_n)
        self.assertEqual(0, result.pr_collection_share)
        self.assertEqual(0, result.mr_collection_share)
        self.assertEqual(0, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(8, result.tis_numeric_code)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(12, result.sequence_n)