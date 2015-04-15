# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getCommonGrammar

"""
CWR Information for Components grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInformationForComponentsValid(unittest.TestCase):
    def setUp(self):
        self.grammar = getCommonGrammar('information_for_components')

    def test_valid_full(self):
        component = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'
        non_roman = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'
        now_1 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'
        now_2 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = component + '\n' + non_roman + '\n' + now_1 + '\n' + now_2

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('COM', result[0].record_type)
        self.assertEqual('NCT', result[1].record_type)
        self.assertEqual('NOW', result[2].record_type)
        self.assertEqual('NOW', result[3].record_type)

    def test_valid_minimum(self):
        component = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'

        record = component

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('COM', result[0].record_type)

    def test_valid_work(self):
        component = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'
        non_roman = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'

        record = component + '\n' + non_roman

        result = self.grammar.parseString(record)

        self.assertEqual(2, len(result))

        self.assertEqual('COM', result[0].record_type)
        self.assertEqual('NCT', result[1].record_type)

    def test_valid_writer_1(self):
        component = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'
        now = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = component + '\n' + now

        result = self.grammar.parseString(record)

        self.assertEqual(2, len(result))

        self.assertEqual('COM', result[0].record_type)
        self.assertEqual('NOW', result[1].record_type)

    def test_valid_writer_2(self):
        component = 'COM0000123400000023THE TITLE                                                   T0123456789ABCD0123456789030201LAST NAME 1                                  FIRST NAME 1                  00014107338LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000229-7I-000000230-7'
        now = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = component + '\n' + now + '\n' + now

        result = self.grammar.parseString(record)

        self.assertEqual(3, len(result))

        self.assertEqual('COM', result[0].record_type)
        self.assertEqual('NOW', result[1].record_type)
        self.assertEqual('NOW', result[1].record_type)