# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar


"""
CWR Transaction Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionTrailerGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('transmission_trailer')

    def test_valid_full(self):
        record = 'TRL000020000053200005703'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TRL', result.record_type)
        self.assertEqual(2, result.group_count)
        self.assertEqual(532, result.transaction_count)
        self.assertEqual(5703, result.record_count)


class TestParseTransmissionTrailerException(unittest.TestCase):
    """
    Tests that TransmissionTrailerDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self.grammar = get_record_grammar('transmission_header')

    def test_empty(self):
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)