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


class TestTransactionInformationGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('transactions')

    def test_agreement_two(self):
        record = _agreement_full() + '\n' + _agreement_full()

        group = self.grammar.parseString(record)

        self.assertEqual(2, len(group))

        result = group[0]

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

        result = group[1]

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

    def test_agreement_one(self):
        record = _agreement_full()

        group = self.grammar.parseString(record)

        self.assertEqual(1, len(group))

        result = group[0]

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

    def test_agreement_full(self):
        record = _agreement_full()

        result = self.grammar.parseString(record)[0]

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

    def test_work_min(self):
        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = work

        result = self.grammar.parseString(record)[0]

        self.assertEqual(1, len(result))

        self.assertEqual('NWR', result[0].record_type)

    def test_work_big(self):
        record = _work_big()

        result = self.grammar.parseString(record)[0]

        self.assertEqual(10, len(result))

        self.assertEqual('NWR', result[0].record_type)
        self.assertEqual('SPU', result[1].record_type)
        self.assertEqual('SPU', result[2].record_type)
        self.assertEqual('SPU', result[3].record_type)
        self.assertEqual('SPT', result[4].record_type)
        self.assertEqual('SWR', result[5].record_type)
        self.assertEqual('SWT', result[6].record_type)
        self.assertEqual('PWR', result[7].record_type)
        self.assertEqual('PER', result[8].record_type)
        self.assertEqual('REC', result[9].record_type)

    def test_work_two(self):
        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = work + '\n' + _work_big()

        group = self.grammar.parseString(record)

        self.assertEqual(2, len(group))

        result = group[0]

        self.assertEqual(1, len(result))

        result = group[1]

        self.assertEqual(10, len(result))

        self.assertEqual('NWR', result[0].record_type)
        self.assertEqual('SPU', result[1].record_type)
        self.assertEqual('SPU', result[2].record_type)
        self.assertEqual('SPU', result[3].record_type)
        self.assertEqual('SPT', result[4].record_type)
        self.assertEqual('SWR', result[5].record_type)
        self.assertEqual('SWT', result[6].record_type)
        self.assertEqual('PWR', result[7].record_type)
        self.assertEqual('PER', result[8].record_type)
        self.assertEqual('REC', result[9].record_type)

    def test_acknowledgement_agreement_full(self):
        acknowledgement = 'ACK0000123400000023201201021020300123401234567AGRTHE CREATION TITLE                                          ABCD1234512345123456ABCD123451234512345720130203AS'

        message_1 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '
        message_2 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '

        agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

        record = acknowledgement + '\n' + message_1 + '\n' + message_2 + '\n' + agreement

        result = self.grammar.parseString(record)[0]

        self.assertEqual(4, len(result))

        self.assertEqual('ACK', result[0].record_type)
        self.assertEqual('MSG', result[1].record_type)
        self.assertEqual('MSG', result[2].record_type)
        self.assertEqual('AGR', result[3].record_type)

    def test_acknowledgement_work_full(self):
        acknowledgement = 'ACK0000123400000023201201021020300123401234567AGRTHE CREATION TITLE                                          ABCD1234512345123456ABCD123451234512345720130203AS'

        message_1 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '
        message_2 = 'MSG0000123400000023F00001234AGRE123MESSAGE                                                                                                                                               '

        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        conflict = 'EXC0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = acknowledgement + '\n' + message_1 + '\n' + message_2 + '\n' + work + '\n' + conflict

        result = self.grammar.parseString(record)[0]

        self.assertEqual(5, len(result))

        self.assertEqual('ACK', result[0].record_type)
        self.assertEqual('MSG', result[1].record_type)
        self.assertEqual('MSG', result[2].record_type)
        self.assertEqual('NWR', result[3].record_type)
        self.assertEqual('EXC', result[4].record_type)


class TestTransactionInformationGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('transactions')

    def test_empty(self):
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)


def _agr_territory():
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

    agr_territory = territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2

    return agr_territory


def _agreement_full():
    agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

    record = agreement + '\n' + _agr_territory() + '\n' + _agr_territory()

    return record


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
