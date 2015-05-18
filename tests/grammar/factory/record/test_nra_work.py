# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR NRA for Work details grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNRAWorkGrammar(unittest.TestCase):
    """
    Tests that the Instrumentation Detail grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = get_record_grammar('nra_work')

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NCT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual('ES', result.language_code)

    def test_extended_character(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NCT0000123400000023THE TITLE \xc6\x8f                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NCT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE \xc6\x8f', result.title)
        self.assertEqual('ES', result.language_code)


class TestNRAWorkGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('nra_work')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)