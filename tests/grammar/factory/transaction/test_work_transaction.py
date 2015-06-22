# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Test Work grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWorkTransactionGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('work_transaction')

    def test_d(self):
        record = 'NWR0000000000000000WORK NAME                                                   ES000000123     T011112211111221011            POP000320U      ORI                                                    00000000000                                                    ' + '\n' + \
                 'SPU000123450000000101122334403AN EDITOR                                     E          00123456703              0590500009910000   00000   I-001234567-8                               ' + '\n' + \
                 'SPT0001234500000002112233403      050001000000000I0484N01' + '\n' + \
                 'SWR0001234500000003011223340SURNAMES                                     NAME                           CA         000112233400120100001200000   00000    I-001122334-5             ' + '\n' + \
                 'SWT00012345000000040112233400500000000I0484N01'

        result = self.grammar.parseString(record)

        self.assertEqual(5, len(result))

        self.assertEqual('NWR', result[0].record_type)

        self.assertEqual('SPU', result[1].record_type)
        self.assertEqual('SPT', result[2].record_type)

        self.assertEqual('SWR', result[3].record_type)
        self.assertEqual('SWT', result[4].record_type)

    def test_writer(self):
        record = 'NWR0000000000000000WORK NAME                                                   ES000000123     T011112211111221011            POP000320U      ORI                                                    00000000000                                                    ' + '\n' + \
                 'SWR0000000000000001030106939WRITER SURNAME                               WRITER                         CA         000111011110111000001110000   00000    I-001234567-1             ' + '\n' + \
                 'SWT0000000000000002030106939100001000000000I0484N01'

        result = self.grammar.parseString(record)

        self.assertEqual(3, len(result))

        self.assertEqual('NWR', result[0].record_type)

        self.assertEqual('SWR', result[1].record_type)
        self.assertEqual('SWT', result[2].record_type)

    def test_common(self):
        record = 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
                 'SPU0000019900000702014271370  MUSIC SOCIETY                                 E          005101734040102328568410061 0500061 1000061 10000   0000000000000                            OS ' + '\n' + \
                 'SPU00000199000007030166       ANOTHER SOCIETY                               AM         002501650060477617137010061 0000061 0000061 00000   0000000000000                            PS ' + '\n' + \
                 'SPU00000199000007040170       YET ANOTHER SOCIETY                           SE         002261445930035870006610059 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000001990000070570             050000500005000I0484Y001' + '\n' + \
                 'SWR00000199000007061185684  A NAME                                       YET ANOTHER NAME               C          0026058307861 0500061 0000061 00000    0000000000000             ' + '\n' + \
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

    def test_common_b(self):
        record = 'NWR0000038200000000MUSIC NAME                                                  AB1234567       T011223304500000000            UNC000300YMTX   ORI   ORIORI                                          N00000000000U                                                  Y' + '\n' + \
                 'SPU0000038200002736011223344  PUBLISHER                                     E          001102233000001111111110011 0111111 0222222 03333   0000000000000                            OS ' + '\n' + \
                 'SPU00000382000027370123       PUBLISHER B                                   AM         001102233000001111111010011 0000000 0000000 00000   0000000000000                            PS ' + '\n' + \
                 'SPU00000382000027380123       PUBLISHER C                                   SE         001111111111111111001110011 00000   00000   00000   0000000000000                            PG ' + '\n' + \
                 'SPT000003820000273900             050000500005000I0484Y001' + '\n' + \
                 'SWR00000382000027401122334  WRITER SURNAME                               WRITER NAME                    CA         0026058307861 0166761 0000061 00000    0000000000000             ' + '\n' + \
                 'SWT00000382000027411122334  050000500005000I0484Y001' + '\n' + \
                 'PWR00000382000027421122334  PUBLISHER                                    01011111111100              1111111  ' + '\n' + \
                 'OWR00000382000027431122334  WRITER SURNAME B                             WRITER NAME B                  CA         0000000000011 0111111 0111111 01111    0000000000000             ' + '\n' + \
                 'OWR00000382000027441122334  WRITER SURNAME C                             WRITER NAME C                  CA         0000000000011 0111111 0111111 01111    0000000000000             ' + '\n' + \
                 'PER0000038200002745PERFORMER                                                                  000000000000000000000000' + '\n' + \
                 'PER0000038200002746PERFORMER B                                                                000000000000000000000000' + '\n' + \
                 'REC000003820000274700000000                                                            000300     A TITLE                                                     A PUBLISHER                                                 1110111                                     U   '

        result = self.grammar.parseString(record)

        self.assertEqual(13, len(result))

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


class TestWorkTransactionGrammarException(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('work_transaction')

    def test_empty(self):
        """
        Tests that a exception is thrown when the the works number is zero.
        """
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
