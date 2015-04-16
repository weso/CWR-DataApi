# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getRecordGrammar
from cwr.transmission import TransmissionHeader, TransmissionTrailer

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
        self.grammar = getRecordGrammar('transmission')

    def test_empty_lines_end(self):
        record = _common()

        record += '\n' + ' ' + '\n' + ' ' + '\t' + ' ' + '\n'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(1, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(1, len(transactions))

        transaction = transactions[0]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

    def test_two_transactions(self):
        record = _two_transactions()

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(1, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(2, len(transactions))

        transaction = transactions[0]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

        transaction = transactions[1]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

    def test_two_groups(self):
        record = _two_groups()

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(2, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(2, len(transactions))

        transaction = transactions[0]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

        transaction = transactions[1]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

    def test_common(self):
        record = _common()

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(1, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(1, len(transactions))

        transaction = transactions[0]

        self.assertEqual(4, len(transaction))

        self.assertEqual('AGR', transaction[0].record_type)
        self.assertEqual('TER', transaction[1].record_type)
        self.assertEqual('IPA', transaction[2].record_type)
        self.assertEqual('IPA', transaction[3].record_type)

    def test_agreement_work(self):
        record = _long()

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(2, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(1, len(transactions))

        transaction = transactions[0]

        self.assertEqual(21, len(transaction))

        group = result.groups[1]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('NWR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(1, len(transactions))

        transaction = transactions[0]

        self.assertEqual(1, len(transaction))

        self.assertEqual('NWR', transaction[0].record_type)

    def test_agreement_full(self):
        record = _agreement_only()

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.header.record_type)
        self.assertTrue(isinstance(result.header, TransmissionHeader))

        self.assertEqual('TRL', result.trailer.record_type)
        self.assertTrue(isinstance(result.trailer, TransmissionTrailer))

        self.assertEqual(1, len(result.groups))

        group = result.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)

        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(1, len(transactions))

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


def _common():
    header_file = 'HDRPB226144593AGENCIA GRUPO MUSICAL                        01.102013080902591120130809               '
    header_group = 'GRHAGR0000102.100130400001  '
    agr = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
    territory = 'TER0000000000000000I2136'
    ipa_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
    ipa_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'
    trailer_group = 'GRT000010000017900000719   0000000000'
    trailer_file = 'TRL000020000053200005703'

    transaction = agr + '\n' + territory + '\n' + ipa_1 + '\n' + ipa_2

    record = header_file + '\n' + header_group + '\n' + transaction + \
             '\n' + trailer_group + '\n' + trailer_file

    return record


def _two_groups():
    header_file = 'HDRPB226144593AGENCIA GRUPO MUSICAL                        01.102013080902591120130809               '
    header_group1 = 'GRHAGR0000102.100130400001  '
    agr = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
    territory = 'TER0000000000000000I2136'
    ipa_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
    ipa_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'
    trailer_group1 = 'GRT000010000017900000719   0000000000'
    trailer_file = 'TRL000020000053200005703'

    transaction1 = agr + '\n' + territory + '\n' + ipa_1 + '\n' + ipa_2

    transaction2 = 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
                   'SPU0000019900000702014271370  MUSIC SOCIETY                                 E          005101734040102328568410061 0500061 1000061 10000   0000000000000                            OS ' + '\n' + \
                   'SPU00000199000007030166       ANOTHER SOCIETY                               AM         002501650060477617137010061 0000061 0000061 00000   0000000000000                            PS ' + '\n' + \
                   'SPU00000199000007040170       YET ANOTHER SOCIETY                           SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                   'SPT000001990000070570             050000500005000I0484Y001' + '\n' + \
                   'SWR00000199000007061185684  A NAME                                       YET ANOTHER NAME               C          0026058307861 0500061 0000061 00000    0000260582865             ' + '\n' + \
                   'SWT00000199000007071185684  050000500005000I0484Y001' + '\n' + \
                   'PWR00000199000007084271370  MUSIC SOCIETY                                01023285684100              1185684  ' + '\n' + \
                   'PER0000019900000709A NAME                                                                     000000000000000000000000' + '\n' + \
                   'REC000001990000071019980101                                                            000300     A COMPILATION                                               P A I  _AR_                                                 33002                                       U   '

    header_group2 = 'GRHNWR0000102.100130400001  '
    trailer_group2 = 'GRT000010000017900000719   0000000000'

    record = header_file + '\n' + \
             header_group1 + '\n' + \
             transaction1 + '\n' + \
             transaction1 + '\n' + \
             trailer_group1 + '\n' + \
             header_group2 + '\n' + \
             transaction2 + '\n' + \
             transaction2 + '\n' + \
             trailer_group2 + '\n' + \
             trailer_file

    return record


def _two_transactions():
    header_file = 'HDRPB226144593AGENCIA GRUPO MUSICAL                        01.102013080902591120130809               '
    header_group = 'GRHAGR0000102.100130400001  '
    agr = 'AGR000000000000000000023683606100              OS200311182013111820131118N        D20131118        00009SYY              '
    territory = 'TER0000000000000000I2136'
    ipa_1 = 'IPA0000000000000001AS0026166137500000000000001183606  ITALIAN                                      GILBERTI DUANTE               61 0500061 0000061 00000'
    ipa_2 = 'IPA0000000000000002AC00250165006000000000000066       SOCIETY MUSIC                                                              61 0500061 1000061 10000'
    trailer_group = 'GRT000010000017900000719   0000000000'
    trailer_file = 'TRL000020000053200005703'

    transaction = agr + '\n' + territory + '\n' + ipa_1 + '\n' + ipa_2

    record = header_file + '\n' + header_group + '\n' + transaction + '\n' + transaction + \
             '\n' + trailer_group + '\n' + trailer_file

    return record


def _long():
    header_file = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

    trailer_file = 'TRL012340123456701234568'

    record = header_file + '\n' + _agreement_group() + '\n' + _work_group() + '\n' + trailer_file

    return record


def _agreement_only():
    header_file = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

    trailer_file = 'TRL012340123456701234568'

    group = _agreement_group()

    record = header_file + '\n' + group + '\n' + trailer_file

    return record


def _agreement_territory():
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

    return territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2


def _agreement():
    agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

    agr_territory_1 = _agreement_territory()

    agr_territory_2 = _agreement_territory()

    return agreement + '\n' + agr_territory_1 + '\n' + agr_territory_2


def _agreement_group():
    header = 'GRHAGR0123402.100123456789  '

    trailer = 'GRT000010000017900000719   0000000000'

    return header + '\n' + _agreement() + '\n' + trailer


def _work_group():
    header = 'GRHNWR0000202.100130500002  '

    trailer = 'GRT012340123456701234567             '

    return header + '\n' + _work() + '\n' + trailer


def _work():
    work = 'NWR0000017900000000NAME OF THE STREET                                            1430374       T037306869919980730            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y'

    return work