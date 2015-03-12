# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import ari


"""
CWR Additional Related Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAdditionalRelatedInformationGrammar(unittest.TestCase):
    """
    Tests that the Additional Related Information grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = ari.ari

    def test_valid_full(self):
        record = 'ARI0000123400000023001ABCD0123456789ALLDWNOTE                                                                                                                                                            '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ARI', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(1, result.society_n)
        self.assertEqual('ABCD0123456789', result.work_n)
        self.assertEqual('ALL', result.type_of_right)
        self.assertEqual('DW', result.subject_code)
        self.assertEqual('NOTE', result.note)