# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Information for Versions grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInformationForVersionsGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('information_for_versions')

    def test_valid_full(self):
        title = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'
        nra = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'
        now_1 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'
        now_2 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = title + '\n' + nra + '\n' + now_1 + '\n' + now_2

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('VER', result[0].record_type)
        self.assertEqual('NCT', result[1].record_type)
        self.assertEqual('NOW', result[2].record_type)
        self.assertEqual('NOW', result[3].record_type)

    def test_writer_1(self):
        title = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'
        now = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = title + '\n' + now

        result = self.grammar.parseString(record)

        self.assertEqual(2, len(result))

        self.assertEqual('VER', result[0].record_type)
        self.assertEqual('NOW', result[1].record_type)

    def test_writer_2(self):
        title = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'
        now = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = title + '\n' + now + '\n' + now

        result = self.grammar.parseString(record)

        self.assertEqual(3, len(result))

        self.assertEqual('VER', result[0].record_type)
        self.assertEqual('NOW', result[1].record_type)
        self.assertEqual('NOW', result[2].record_type)

    def test_work(self):
        title = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'
        nra = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'

        record = title + '\n' + nra

        result = self.grammar.parseString(record)

        self.assertEqual(2, len(result))

        self.assertEqual('VER', result[0].record_type)
        self.assertEqual('NCT', result[1].record_type)

    def test_valid_min(self):
        title = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        record = title

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('VER', result[0].record_type)


class TestInformationForVersionsGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('information_for_versions')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)