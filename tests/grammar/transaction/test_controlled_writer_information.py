# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.transaction import interested_party

"""
CWR Controlled Writer Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestControlledWriterInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = interested_party.controlled_writer_information

    def test_full(self):
        writer = 'SWR0000123400000023A12345678LAST NAME                                    FIRST NAME                    NA 92370341200014107338009020500100300001102312YYY I-000000229-7012345678901B'
        nwn = 'NWN0000123400000023A12345678LAST NAME                                                                                                                                                       FIRST NAME                                                                                                                                                      ES'
        territory_1 = 'SWT0000123400000023A12345678010120500002520I0008Y012'
        territory_2 = 'SWT0000123400000023A12345678010120500002520I0008Y012'
        publisher_1 = 'PWR0000123400000023A12345678THE PUBLISHER                                C1234567890123D1234567890123A12345678'
        publisher_2 = 'PWR0000123400000023A12345678THE PUBLISHER                                C1234567890123D1234567890123A12345678'

        record = writer + '\n' + nwn + '\n' + territory_1 + '\n' + territory_2 + '\n' + publisher_1 + '\n' + publisher_2

        result = self.grammar.parseString(record)

        self.assertEqual(6, len(result))

        self.assertEqual('SWR', result[0].record_type)
        self.assertEqual('NWN', result[1].record_type)
        self.assertEqual('SWT', result[2].record_type)
        self.assertEqual('SWT', result[3].record_type)
        self.assertEqual('PWR', result[4].record_type)
        self.assertEqual('PWR', result[5].record_type)

    def test_min(self):
        writer = 'SWR0000123400000023A12345678LAST NAME                                    FIRST NAME                    NA 92370341200014107338009020500100300001102312YYY I-000000229-7012345678901B'
        publisher_1 = 'PWR0000123400000023A12345678THE PUBLISHER                                C1234567890123D1234567890123A12345678'

        record = writer + '\n' + publisher_1

        result = self.grammar.parseString(record)

        self.assertEqual(2, len(result))

        self.assertEqual('SWR', result[0].record_type)
        self.assertEqual('PWR', result[1].record_type)