# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Non-Roman Alphabet Writer Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNWNGrammar(unittest.TestCase):
    """
    Tests that the NWN grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('nra_writer_name')

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NWN0000123400000023A12345678LAST NAME                                                                                                                                                       FIRST NAME                                                                                                                                                      ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.ip_n)
        self.assertEqual('LAST NAME', result.writer_last_name)
        self.assertEqual('FIRST NAME', result.writer_first_name)
        self.assertEqual('ES', result.language_code)

    def test_extended_character(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NWN0000123400000023A12345678LAST NAME \xc6\x8f                                                                                                                                                    FIRST NAME \xc6\x8f                                                                                                                                                   ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.ip_n)
        self.assertEqual('LAST NAME \xc6\x8f', result.writer_last_name)
        self.assertEqual('FIRST NAME \xc6\x8f', result.writer_first_name)
        self.assertEqual('ES', result.language_code)


class TestNWNGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_writer_name')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
