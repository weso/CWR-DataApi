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


class TestAgreementTransactionGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('agreement_transaction')

    def test_valid_short(self):
        record = _agreement_short()

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('AGR', result[0].record_type)

        self.assertEqual('TER', result[1].record_type)

        self.assertEqual('IPA', result[2].record_type)
        self.assertEqual('IPA', result[3].record_type)

    def test_valid_full(self):
        record = _agreement_long()

        result = self.grammar.parseString(record)

        self.assertEqual(21, len(result))

        self.assertEqual('AGR', result[0].record_type)

        self.assertEqual('TER', result[1].record_type)
        self.assertEqual('TER', result[2].record_type)

        self.assertEqual('IPA', result[3].record_type)
        self.assertEqual('NPA', result[4].record_type)

        self.assertEqual('IPA', result[5].record_type)
        self.assertEqual('NPA', result[6].record_type)

        self.assertEqual('IPA', result[7].record_type)
        self.assertEqual('NPA', result[8].record_type)

        self.assertEqual('IPA', result[9].record_type)
        self.assertEqual('NPA', result[10].record_type)

        self.assertEqual('TER', result[11].record_type)
        self.assertEqual('TER', result[12].record_type)

        self.assertEqual('IPA', result[13].record_type)
        self.assertEqual('NPA', result[14].record_type)

        self.assertEqual('IPA', result[15].record_type)
        self.assertEqual('NPA', result[16].record_type)

        self.assertEqual('IPA', result[17].record_type)
        self.assertEqual('NPA', result[18].record_type)

        self.assertEqual('IPA', result[19].record_type)
        self.assertEqual('NPA', result[20].record_type)


class TestAgreementTransactionGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('agreement_transaction')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)


def _agreement_short():
    agr_1 = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
    ter_1_1 = 'TER0000000000000000I2136'
    ipa_1_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
    ipa_1_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'

    return agr_1 + '\n' + ter_1_1 + '\n' + ipa_1_1 + '\n' + ipa_1_2


def _agreement_long():
    agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

    territory_1 = 'TER0000123400000023I0020'
    territory_2 = 'TER0000123400000023I0020'

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    assignor_1 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    assignor_2 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    acquirer_1 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    acquirer_2 = ipa + '\n' + npa

    agr_territory_1 = territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2

    territory_1 = 'TER0000123400000023I0020'
    territory_2 = 'TER0000123400000023I0020'

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    assignor_1 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    assignor_2 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    acquirer_1 = ipa + '\n' + npa

    ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
    npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

    acquirer_2 = ipa + '\n' + npa

    agr_territory_2 = territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2

    return agreement + '\n' + agr_territory_1 + '\n' + agr_territory_2