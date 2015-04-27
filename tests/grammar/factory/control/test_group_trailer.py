# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getRecordGrammar


"""
CWR Group Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupTrailerGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = getRecordGrammar('group_trailer')

    def test_valid_full(self):
        record = 'GRT000010000017900000719   0000000000'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRT', result.record_type)
        self.assertEqual(1, result.group_id)
        self.assertEqual(179, result.transaction_count)
        self.assertEqual(719, result.record_count)

    def test_valid_full_b(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'GRT012340123456701234567             '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRT', result.record_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual(1234567, result.transaction_count)
        self.assertEqual(1234567, result.record_count)


class TestGrammarGroupTrailerException(unittest.TestCase):
    """
    Tests that GroupTrailerDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self.grammar = getRecordGrammar('group_trailer')

    def test_invalid_wrong_group_id(self):
        """
        Tests that GroupTrailerDecoder throws an exception when the group ID is 0.
        """
        record = 'GRHACK0000002.100123456789  '

        # self.assertRaises(ParseException, self.grammar.parseString, record)