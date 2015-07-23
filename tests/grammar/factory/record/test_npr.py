# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Non-Roman Alphabet Publisher Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNPRGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_performance_data')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPR0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      00014107338I-000000229-7ESENCAN'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME', result.performing_artist_name)
        self.assertEqual('FIRST NAME', result.performing_artist_first_name)
        self.assertEqual(14107338, result.performing_artist_ipi_name_n)
        self.assertEqual('I-000000229-7', result.performing_artist_ipi_base_n)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('EN', result.performance_language)
        self.assertEqual('CAN', result.performance_dialect)

    def test_extended_character(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPR0000123400000023NAME \xc6\x8f                                                                                                                                                         FIRST NAME \xc6\x8f                                                                                                                                                   00014107338I-000000229-7ESENCAN'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME \xc6\x8f', result.performing_artist_name)
        self.assertEqual('FIRST NAME \xc6\x8f',
                         result.performing_artist_first_name)
        self.assertEqual(14107338, result.performing_artist_ipi_name_n)
        self.assertEqual('I-000000229-7', result.performing_artist_ipi_base_n)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('EN', result.performance_language)
        self.assertEqual('CAN', result.performance_dialect)


class TestNPRGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_performance_data')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
