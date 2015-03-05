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


class TestFileValid(unittest.TestCase):
    def setUp(self):
        self.grammar = file.cwr_file

    def test(self):
        header_file = 'HDRPB226144593AGENCIA GRUPO MUSICAL                        01.102013080902591120130809               '
        header_group = 'GRHAGR0000102.100130400001  '
        agr = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
        ipa_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
        ipa_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'
        territory = 'TER0000000000000000I2136'
        trailer_group = 'GRT000010000017900000719   0000000000'
        trailer_file = 'TRL000020000053200005703'

        record = header_file + '\n' + header_group + '\n' + agr + '\n' + territory + '\n' + ipa_1 + '\n' + ipa_2 +\
                 '\n' + trailer_group + '\n' + trailer_file

        result = self.grammar.parseString(record)

        self.assertEqual(8, len(result))

    def test_agreement_full(self):
        header_file = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        trailer_file = 'TRL012340123456701234568'

        header = 'GRHACK0123402.100123456789  '

        trailer = 'GRT012340123456701234567             '

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

        agreement_record = agreement + '\n' + agr_territory_1 + '\n' + agr_territory_2

        group = header + '\n' + agreement_record + '\n' + trailer

        record = header_file + '\n' + group + '\n' + trailer_file

        result = self.grammar.parseString(record)

        self.assertEqual(25, len(result))

        self.assertEqual('HDR', result[0].record_type)

        self.assertEqual('GRH', result[1].record_type)

        self.assertEqual('AGR', result[2].record_type)

        self.assertEqual('TER', result[3].record_type)
        self.assertEqual('TER', result[4].record_type)

        self.assertEqual('IPA', result[5].record_type)
        self.assertEqual('NPA', result[6].record_type)

        self.assertEqual('IPA', result[7].record_type)
        self.assertEqual('NPA', result[8].record_type)

        self.assertEqual('IPA', result[9].record_type)
        self.assertEqual('NPA', result[10].record_type)

        self.assertEqual('IPA', result[11].record_type)
        self.assertEqual('NPA', result[12].record_type)

        self.assertEqual('TER', result[13].record_type)
        self.assertEqual('TER', result[14].record_type)

        self.assertEqual('IPA', result[15].record_type)
        self.assertEqual('NPA', result[16].record_type)

        self.assertEqual('IPA', result[17].record_type)
        self.assertEqual('NPA', result[18].record_type)

        self.assertEqual('IPA', result[19].record_type)
        self.assertEqual('NPA', result[20].record_type)

        self.assertEqual('IPA', result[21].record_type)
        self.assertEqual('NPA', result[22].record_type)

        self.assertEqual('GRT', result[23].record_type)

        self.assertEqual('TRL', result[24].record_type)