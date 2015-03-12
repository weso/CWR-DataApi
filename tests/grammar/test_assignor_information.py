# -*- coding: utf-8 -*-
import unittest

from cwr.grammar import interested_party

"""
CWR Acquirer Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAssignorInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = interested_party.ipa_information

    def test_full(self):
        ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'
        npa = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

        record = ipa + '\n' + npa

        result = self.grammar.parseString(record)

        self.assertEqual('IPA', result[0].record_type)
        self.assertEqual('NPA', result[1].record_type)

    def test_min(self):
        ipa = 'IPA0000123400000023AC01234567890I-000000229-7A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'

        record = ipa

        result = self.grammar.parseString(record)

        self.assertEqual('IPA', result[0].record_type)