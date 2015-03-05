# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import file

"""
CWR Administrator Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransactionInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = file.transaction_info

    def test_agreement_full(self):
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

        record = agreement + '\n' + agr_territory_1 + '\n' + agr_territory_2

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

    def test_work_min(self):
        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = work

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('NWR', result[0].record_type)

    def test_acknowledgement_agreement_full(self):
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

    def test_acknowledgement_work_full(self):
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
