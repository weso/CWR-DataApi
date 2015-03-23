# -*- coding: utf-8 -*-
import unittest

from cwr.grammar import interested_party

"""
CWR Administrator Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAdministratorInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = interested_party.administrator_information

    def test_valid_full(self):
        publisher = 'SPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'
        npn = 'NPN000012340000002312A12345678THE NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ES'
        territory_1 = 'SPT0000123400000023A12345678      010120500002520I0008Y012'
        territory_2 = 'SPT0000123400000023A12345678      010120500002520I0008Y012'

        record = publisher + '\n' + npn + '\n' + territory_1 + '\n' + territory_2

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('SPU', result[0].record_type)
        self.assertEqual('NPN', result[1].record_type)
        self.assertEqual('SPT', result[2].record_type)
        self.assertEqual('SPT', result[3].record_type)

    def test_valid_min(self):
        publisher = 'SPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        record = publisher

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('SPU', result[0].record_type)