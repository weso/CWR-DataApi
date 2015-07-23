# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Work Origin grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWorkOriginGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('work_origin')

    def test_full(self):
        record = 'ORN0000123400000023LIBPRODUCTION TITLE                                            IDENTIFIER     1234THE LIBRARY                                                 B1234567812345678901212341ABDFE       EPISODE TITLE                                               ABD12345            2012123ABDEFG         '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ORN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('LIB', result.intended_purpose)
        self.assertEqual('PRODUCTION TITLE', result.production_title)
        self.assertEqual('IDENTIFIER', result.cd_identifier)
        self.assertEqual(1234, result.cut_number)
        self.assertEqual('THE LIBRARY', result.library)
        self.assertEqual('B', result.bltvr)
        self.assertEqual('1234567812345678901212341', result.visan)
        self.assertEqual('ABDFE', result.production_n)
        self.assertEqual('EPISODE TITLE', result.episode_title)
        self.assertEqual('ABD12345', result.episode_n)
        self.assertEqual(2012, result.year_production)
        self.assertEqual(123, result.audio_visual_key.society_code)
        self.assertEqual('ABDEFG', result.audio_visual_key.av_number)

    def test_common(self):
        record = 'ORN0000044400003579LIBPRODUCTION TITLE                                                           0000                                                             0000000000000000000000000            EPISODE TITLE                                                                   0000000               '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ORN', result.record_type)
        self.assertEqual(444, result.transaction_sequence_n)
        self.assertEqual(3579, result.record_sequence_n)
        self.assertEqual('LIB', result.intended_purpose)
        self.assertEqual('PRODUCTION TITLE', result.production_title)
        self.assertEqual(None, result.cd_identifier)
        self.assertEqual(0, result.cut_number)
        self.assertEqual(None, result.library)
        self.assertEqual(None, result.bltvr)
        self.assertEqual('0000000000000000000000000', result.visan)
        self.assertEqual(None, result.production_n)
        self.assertEqual('EPISODE TITLE', result.episode_title)
        self.assertEqual(None, result.episode_n)
        self.assertEqual(0, result.year_production)
        self.assertEqual(0, result.audio_visual_key.society_code)
        self.assertEqual('', result.audio_visual_key.av_number)


class TestWorkOriginGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('work_origin')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
