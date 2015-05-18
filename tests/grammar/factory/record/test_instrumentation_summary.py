# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar


"""
CWR Instrumentation Summary grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentationSummaryGrammar(unittest.TestCase):
    """
    Tests that the Instrumentation Summary grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('instrumentation_summary')

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'INS0000123400000023012BBADESCRIPTION                                       '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('INS', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(12, result.number_voices)
        self.assertEqual('BBA', result.standard_instrumentation_type)
        self.assertEqual('DESCRIPTION', result.instrumentation_description)


class TestInstrumentationSummaryGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('instrumentation_summary')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)