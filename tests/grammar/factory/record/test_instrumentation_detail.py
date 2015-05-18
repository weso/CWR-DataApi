# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar


"""
CWR Instrumentation Detail grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentationDetailGrammar(unittest.TestCase):
    """
    Tests that the Instrumentation Detail grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('instrumentation_detail')

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'IND0000123400000023ALT123'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('IND', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('ALT', result.instrument_code)
        self.assertEqual(123, result.number_players)


class TestInstrumentationDetailGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('instrumentation_detail')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)