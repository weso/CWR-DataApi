# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Non-Roman Alphabet Other Writer Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestNOWGrammar(unittest.TestCase):
    """
    Tests that the NPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('nra_other_writer')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NOW', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME', result.writer_name)
        self.assertEqual('FIRST NAME', result.writer_first_name)
        self.assertEqual('ES', result.language_code)
        self.assertEqual(1, result.position)

    def test_extended_character(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NOW0000123400000023NAME \xc6\x8f                                                                                                                                                         FIRST NAME \xc6\x8f                                                                                                                                                   ES1'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NOW', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME \xc6\x8f', result.writer_name)
        self.assertEqual('FIRST NAME \xc6\x8f', result.writer_first_name)
        self.assertEqual('ES', result.language_code)
        self.assertEqual(1, result.position)


class TestNOWGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_other_writer')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
