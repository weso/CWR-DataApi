# -*- coding: utf-8 -*-
import unittest
import time
import sys

from cwr.parser.decoder.file import default_grammar_factory

"""
Tests for the DefaultFieldFactory.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestDefaultRuleFactory(unittest.TestCase):
    def setUp(self):
        self._factory = default_grammar_factory()

    def test_10(self):
        grammar = self._factory.get_rule('transactions')

        record = ''
        if sys.version_info[0] == 2:
            for x in xrange(35):
                if len(record) == 0:
                    record = _agreement_full()
                elif len(record) > 0:
                    record = record + '\n' + _agreement_full()
        else:
            for x in range(35):
                if len(record) == 0:
                    record = _agreement_full()
                elif len(record) > 0:
                    record = record + '\n' + _agreement_full()

        start = time.clock()
        grammar.parseString(record)
        end = time.clock()

        time_parse = (end - start)

        self.assertTrue(time_parse < 1)


def _agreement_full():
    agreement = 'AGR0000123400000023C1234567890123D1234567890123OG201201022013020320140304D20100405D201605062017060701234MYY0123456789012A'

    record = agreement + '\n' + _agr_territory() + '\n' + _agr_territory()

    return record


def _agr_territory():
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

    agr_territory = territory_1 + '\n' + territory_2 + '\n' + assignor_1 + '\n' + assignor_2 + '\n' + acquirer_1 + '\n' + acquirer_2

    return agr_territory
