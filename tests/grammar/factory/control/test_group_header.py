# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Group Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupHeaderGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('group_header')

    def test_valid_full(self):
        record = 'GRHAGR0000102.100130400001  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual(1, result.group_id)
        self.assertEqual('AGR', result.transaction_type)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(130400001, result.batch_request_id)

    def test_valid_full_ack(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.100123456789  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(123456789, result.batch_request_id)

    def test_valid_no_batch_request(self):
        """
        Tests that GroupHeaderDecoder decodes a Group Header with no batch id.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.100000000000  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(0, result.batch_request_id)


class TestGroupInformationGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = self.grammar = get_record_grammar('group_info')

    def test_empty(self):
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)


class TestGrammarGroupHeaderGrammarException(unittest.TestCase):
    """
    Tests that GroupHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self.grammar = get_record_grammar('group_header')

    def test_empty(self):
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)
