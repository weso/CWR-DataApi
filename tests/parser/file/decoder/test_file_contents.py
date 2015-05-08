# -*- coding: utf-8 -*-

import unittest

from cwr.transmission import TransmissionHeader, TransmissionTrailer
from cwr.parser.decoder.common import GrammarDecoder
from tests.utils.grammar import get_record_grammar


"""
CWR file encoder tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileCWRDecodeValid(unittest.TestCase):
    def setUp(self):
        self._parser = GrammarDecoder(get_record_grammar('transmission'))

    def test_two_groups(self):
        record = _two_groups()

        result = self._parser.decode(record)[0]

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