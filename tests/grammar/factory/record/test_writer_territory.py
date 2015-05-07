# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getRecordGrammar


"""
CWR Writer Territory of Control (SWT) grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestSWTGrammar(unittest.TestCase):
    """
    Tests that the SWT grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = getRecordGrammar('writer_territory')

    def test_valid_too_short(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SWT0000000000000002030106939100001000000000I0484N01'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SWT', result.record_type)
        self.assertEqual(0, result.transaction_sequence_n)
        self.assertEqual(2, result.record_sequence_n)
        self.assertEqual('030106939', result.ip_n)
        self.assertEqual(100, result.pr_collection_share)
        self.assertEqual(100, result.mr_collection_share)
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
        record = 'SWT0000123400000023A12345678010120500002520I0008Y012'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SWT', result.record_type)
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