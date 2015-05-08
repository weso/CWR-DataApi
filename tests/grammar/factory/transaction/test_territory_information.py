# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import get_record_grammar

"""
CWR Administrator Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTerritoryInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('territory_information')

    def test_valid_full(self):
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

        record = territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2

        result = self.grammar.parseString(record)

        self.assertEqual(10, len(result))

        self.assertEqual('TER', result[0].record_type)
        self.assertEqual('TER', result[1].record_type)

        self.assertEqual('IPA', result[2].record_type)
        self.assertEqual('NPA', result[3].record_type)

        self.assertEqual('IPA', result[4].record_type)
        self.assertEqual('NPA', result[5].record_type)

        self.assertEqual('IPA', result[6].record_type)
        self.assertEqual('NPA', result[7].record_type)

        self.assertEqual('IPA', result[8].record_type)
        self.assertEqual('NPA', result[9].record_type)
