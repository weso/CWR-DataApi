# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Non-Roman Alphabet Agreement Party Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNPAGrammar(unittest.TestCase):
    """
    Tests that the NPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('nra_agreement_party')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('012345678', result.ip_n)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual('ES', result.language_code)

    def test_valid_min(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'NPA0000123400000023000000000PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                                 '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('000000000', result.ip_n)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual(None, result.language_code)

    def test_extended_character(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'NPA0000123400000023000000000PARTY NAME \xc6\x8f                                                                                                                                                   PARTY WRITER NAME \xc6\x8f                                                                                                                                              '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('000000000', result.ip_n)
        self.assertEqual('PARTY NAME \xc6\x8f', result.ip_name)
        self.assertEqual('PARTY WRITER NAME \xc6\x8f', result.ip_writer_name)
        self.assertEqual(None, result.language_code)


class TestNPAGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_agreement_party')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
