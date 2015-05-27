# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Entire Work Title grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestEntireWorkTitleGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('entire_work_title')

    def test_valid_full(self):
        record = 'EWT0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('EWT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('LAST NAME 1', result.writer_1_last_name)
        self.assertEqual('FIRST NAME 1', result.writer_1_first_name)
        self.assertEqual('THE SOURCE', result.source)
        self.assertEqual(14107338, result.writer_1_ipi_name_n)
        self.assertEqual('I', result.writer_1_ipi_base_n.header)
        self.assertEqual(229, result.writer_1_ipi_base_n.id_code)
        self.assertEqual(7, result.writer_1_ipi_base_n.check_digit)
        self.assertEqual('LAST NAME 2', result.writer_2_last_name)
        self.assertEqual('FIRST NAME 2', result.writer_2_first_name)
        self.assertEqual(14107339, result.writer_2_ipi_name_n)
        self.assertEqual('I', result.writer_2_ipi_base_n.header)
        self.assertEqual(230, result.writer_2_ipi_base_n.id_code)
        self.assertEqual(7, result.writer_2_ipi_base_n.check_digit)
        self.assertEqual('ABCD0123456789', result.submitter_work_n)


class TestEntireWorkTitleGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('entire_work_title')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
