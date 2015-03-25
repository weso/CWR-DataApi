# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.transaction import transaction

"""
CWR Test Work grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkTransactionValid(unittest.TestCase):
    def setUp(self):
        self.grammar = transaction.work_transaction

    def test_common(self):
        record = 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
                 'SPU0000019900000702014271370  MUSIC SOCIETY                                 E          005101734040102328568410061 0500061 1000061 10000   0000000000000                            OS ' + '\n' + \
                 'SPU00000199000007030166       ANOTHER SOCIETY                               AM         002501650060477617137010061 0000061 0000061 00000   0000000000000                            PS ' + '\n' + \
                 'SPU00000199000007040170       YET ANOTHER SOCIETY                           SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000001990000070570             050000500005000I0484Y001' + '\n' + \
                 'SWR00000199000007061185684  A NAME                                       YET ANOTHER NAME               C          0026058307861 0500061 0000061 00000    0000260582865             ' + '\n' + \
                 'SWT00000199000007071185684  050000500005000I0484Y001' + '\n' + \
                 'PWR00000199000007084271370  MUSIC SOCIETY                                01023285684100              1185684  ' + '\n' + \
                 'PER0000019900000709A NAME                                                                     000000000000000000000000' + '\n' + \
                 'REC000001990000071019980101                                                            000300     A COMPILATION                                               P A I  _AR_                                                 33002                                       U   '

        result = self.grammar.parseString(record)

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

    def test_work_full(self):
        record = 'NWR0000017900000000STREET NAME                                                   1430374       T037306869919980730            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
                 'SPU00000179000005380166       MUSIC SOCIETY                                 E          002501650060399357851805061 0025061 0050061 00500   0000000000000                            OS ' + '\n' + \
                 'SPU00000179000005390170       ANOTHER SOCIETY                               SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000001790000054070             002500025000250I0484Y001' + '\n' + \
                 'SPU00000179000005410247       A PUBLISHER                                   E          004344910660399367851805061 0025061 0050061 00500   0000000000000                            OS ' + '\n' + \
                 'SPU00000179000005420266       MUSIC SOCIETY                                 AM         002501650060394480004710061 0000061 0000061 00000   0000000000000                            PS ' + '\n' + \
                 'SPU00000179000005430270       ANOTHER SOCIETY                               SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000001790000054470             002500025000250I0484Y001' + '\n' + \
                 'SPU00000179000005450366       MUSIC SOCIETY                                 E          002501650060380247851610061 0133361 0266761 02667   0000000000000                            OS ' + '\n' + \
                 'SPU00000179000005460370       ANOTHER SOCIETY                               SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000001790000054770             013330133301333I0484Y001' + '\n' + \
                 'SWR00000179000005481178518  SURNAME                                      NAME                           C          0026169554761 0050061 0000061 00000    0000000000000             ' + '\n' + \
                 'SWT00000179000005491178518  005000050000500I0484Y001' + '\n' + \
                 'PWR000001790000055066       MUSIC SOCIETY                                03993578518050              1178518  ' + '\n' + \
                 'PWR000001790000055147       A PUBLISHER                                  03993678518050              1178518  ' + '\n' + \
                 'SWR00000179000005521178516  SURNAME                                      NAME                           C          0026169445261 0133361 0000061 00000    0000000000000             ' + '\n' + \
                 'SWT00000179000005531178516  013340133401334I0484Y001' + '\n' + \
                 'PWR000001790000055466       MUSIC SOCIETY                                03802478516100              1178516  ' + '\n' + \
                 'OWR00000179000005551176743  SURNAME                                      NAME                           C          0000000000061 0100061 0100061 01000    0000000000000             ' + '\n' + \
                 'OWR00000179000005561178515  SURNAME                                      NAME                           C          0000000000061 0266761 0266761 02667    0000000000000             ' + '\n' + \
                 'OWR00000179000005571178514  SURNAME                                      NAME                           CA         0000000000061 0266761 0266761 02667    0000000000000             ' + '\n' + \
                 'PER0000017900000558PERFORMER                                                                  000000000000000000000000'

        result = self.grammar.parseString(record)

        self.assertEqual(22, len(result))

        self.assertEqual('NWR', result[0].record_type)

        self.assertEqual('SPU', result[1].record_type)
        self.assertEqual('SPU', result[2].record_type)

        self.assertEqual('SPT', result[3].record_type)

        self.assertEqual('SPU', result[4].record_type)
        self.assertEqual('SPU', result[5].record_type)
        self.assertEqual('SPU', result[6].record_type)

        self.assertEqual('SPT', result[7].record_type)

        self.assertEqual('SPU', result[8].record_type)
        self.assertEqual('SPU', result[9].record_type)

        self.assertEqual('SPT', result[10].record_type)

        self.assertEqual('SWR', result[11].record_type)

        self.assertEqual('SWT', result[12].record_type)

        self.assertEqual('PWR', result[13].record_type)
        self.assertEqual('PWR', result[14].record_type)

        self.assertEqual('SWR', result[15].record_type)

        self.assertEqual('SWT', result[16].record_type)

        self.assertEqual('PWR', result[17].record_type)

        self.assertEqual('OWR', result[18].record_type)
        self.assertEqual('OWR', result[19].record_type)
        self.assertEqual('OWR', result[20].record_type)

        self.assertEqual('PER', result[21].record_type)

    def test_work_min(self):
        work = 'NWR0000123400000023TITLE OF THE WORK                                           ENABCD0123456789T012345678920130102AB0123456789POP030201YMUSPOTMODMOVORIORITHE CONTACT                   A123456789ARY01220140302Y28#3                     KV 297#1                 Y'

        record = work

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('NWR', result[0].record_type)
