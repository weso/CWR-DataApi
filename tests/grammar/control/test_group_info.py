# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.transaction import file

"""
CWR Administrator Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = file.group_info

    def test_agreement_min(self):
        header = 'GRHAGR0000102.100130400001  '
        trailer = 'GRT012340123456701234567             '

        record = header + '\n' + _agreement_short() + '\n' + trailer

        result = self.grammar.parseString(record)[0]

        transaction = result.transactions[0]

        self.assertEqual('AGR', transaction[0].record_type)

    def test_agreement_small_pair(self):
        header = 'GRHAGR0000102.100130400001  '
        trailer = 'GRT000010000017900000719   0000000000'

        record = header + '\n' + _agreement_short() + '\n' + _agreement_short() + '\n' + trailer

        result = self.grammar.parseString(record)[0]

        transaction = result.transactions[0]

        self.assertEqual('AGR', transaction[0].record_type)

    def test_agreement_full(self):
        header = 'GRHAGR0123402.100123456789  '

        trailer = 'GRT012340123456701234567             '

        agreement_record_1 = _agreement_record_big()

        agreement_record_2 = _agreement_record_big()

        record = header + '\n' + agreement_record_1 + '\n' + agreement_record_2 + '\n' + trailer

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.group_header.record_type)

        self.assertEqual('GRT', result.group_trailer.record_type)

        transactions = result.transactions

        self.assertEqual(2, len(transactions))

        transaction = transactions[0]
        self.assertEqual(21, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)

        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('TER', transaction[2].record_type)

        self.assertEqual('IPA', transaction[3].record_type)
        self.assertEqual('NPA', transaction[4].record_type)

        self.assertEqual('IPA', transaction[5].record_type)
        self.assertEqual('NPA', transaction[6].record_type)

        self.assertEqual('IPA', transaction[7].record_type)
        self.assertEqual('NPA', transaction[8].record_type)

        self.assertEqual('IPA', transaction[9].record_type)
        self.assertEqual('NPA', transaction[10].record_type)

        self.assertEqual('TER', transaction[11].record_type)
        self.assertEqual('TER', transaction[12].record_type)

        self.assertEqual('IPA', transaction[13].record_type)
        self.assertEqual('NPA', transaction[14].record_type)

        self.assertEqual('IPA', transaction[15].record_type)
        self.assertEqual('NPA', transaction[16].record_type)

        self.assertEqual('IPA', transaction[17].record_type)
        self.assertEqual('NPA', transaction[18].record_type)

        self.assertEqual('IPA', transaction[19].record_type)
        self.assertEqual('NPA', transaction[20].record_type)


class TestGroupInformationInvalid(unittest.TestCase):
    def setUp(self):
        self.grammar = file.group_info


    def test_agreement_and_work(self):
        header = 'GRHACK0123402.100123456789  '

        trailer = 'GRT012340123456701234567             '

        record = header + '\n' + _agreement_record_big() + '\n' + _work_big() + '\n' + trailer

        #self.assertRaises(ParseException, self.grammar.parseString, record)


def _work_big():
    return 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
           'SPU0000019900000702014271370  MUSIC SOCIETY                                 E          005101734040102328568410061 0500061 1000061 10000   0000000000000                            OS ' + '\n' + \
           'SPU00000199000007030166       ANOTHER SOCIETY                               AM         002501650060477617137010061 0000061 0000061 00000   0000000000000                            PS ' + '\n' + \
           'SPU00000199000007040170       YET ANOTHER SOCIETY                           SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
           'SPT000001990000070570             050000500005000I0484Y001' + '\n' + \
           'SWR00000199000007061185684  A NAME                                       YET ANOTHER NAME               C          0026058307861 0500061 0000061 00000    0000260582865             ' + '\n' + \
           'SWT00000199000007071185684  050000500005000I0484Y001' + '\n' + \
           'PWR00000199000007084271370  MUSIC SOCIETY                                01023285684100              1185684  ' + '\n' + \
           'PER0000019900000709A NAME                                                                     000000000000000000000000' + '\n' + \
           'REC000001990000071019980101                                                            000300     A COMPILATION                                               P A I  _AR_                                                 33002                                       U   '


def _agreement_record_big():
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


def _agreement_short():
    agr_1 = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
    ter_1_1 = 'TER0000000000000000I2136'
    ipa_1_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
    ipa_1_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'

    return agr_1 + '\n' + ter_1_1 + '\n' + ipa_1_1 + '\n' + ipa_1_2
