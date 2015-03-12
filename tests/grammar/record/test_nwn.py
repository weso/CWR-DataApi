# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import nra


"""
CWR Non-Roman Alphabet Writer Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNWNGrammar(unittest.TestCase):
    """
    Tests that the NWN grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = nra.nwn

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NWN0000123400000023A12345678LAST NAME                                                                                                                                                       FIRST NAME                                                                                                                                                      ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.ip_n)
        self.assertEqual('LAST NAME', result.writer_last_name)
        self.assertEqual('FIRST NAME', result.writer_first_name)
        self.assertEqual('ES', result.language_code)