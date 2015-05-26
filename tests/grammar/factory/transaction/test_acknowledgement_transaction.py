# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Administrator Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAcknowledgementTransactionGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('acknowledgement_transaction')

    def test_agreement_full(self):
        acknowledgement = 'ACK0000123400000023201201021020300123401234567AGRTHE CREATION TITLE                                          ABCD1234512345123456ABCD123451234512345720130203AS'

        message_1 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '
        message_2 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '

        agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

        record = acknowledgement + '\n' + message_1 + '\n' + message_2 + '\n' + agreement

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('ACK', result[0].record_type)
        self.assertEqual('MSG', result[1].record_type)
        self.assertEqual('MSG', result[2].record_type)
        self.assertEqual('AGR', result[3].record_type)

    def test_work_full(self):
        acknowledgement = 'ACK0000123400000023201201021020300123401234567AGRTHE CREATION TITLE                                          ABCD1234512345123456ABCD123451234512345720130203AS'

        message_1 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '
        message_2 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '

        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        conflict = 'EXC0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = acknowledgement + '\n' + message_1 + '\n' + message_2 + '\n' + work + '\n' + conflict

        result = self.grammar.parseString(record)

        self.assertEqual(5, len(result))

        self.assertEqual('ACK', result[0].record_type)
        self.assertEqual('MSG', result[1].record_type)
        self.assertEqual('MSG', result[2].record_type)
        self.assertEqual('NWR', result[3].record_type)
        self.assertEqual('EXC', result[4].record_type)


class TestAcknowledgementTransactionGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('acknowledgement_transaction')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
