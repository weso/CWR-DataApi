# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar


"""
CWR Territory in Agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementTerritoryGrammar(unittest.TestCase):
    """
    Tests that the Territory in Agreement grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('territory_in_agreement')

    def test_valid(self):
        """
        Tests that Territory in Agreement grammar decodes correctly formatted record prefixes.
        """
        record = 'TER0000123400000023I0020'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(20, result.tis_numeric_code)


class TestAgreementTerritoryGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('territory_in_agreement')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)