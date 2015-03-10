# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import writer_publisher


"""
CWR Publisher For Writer grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWriterPublisherGrammar(unittest.TestCase):
    """
    Tests that the Writer grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = writer_publisher.publisher

    def test_valid_full(self):
        """
        Tests that Writer grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'PWR0000123400000023A12345678THE PUBLISHER                                C1234567890123D1234567890123A12345678'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('PWR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.publisher_id)
        # self.assertEqual('THE PUBLISHER', result.publisher_name)
        self.assertEqual('C1234567890123', result.agreement_id)
        self.assertEqual('D1234567890123', result.society_agreement_id)
        self.assertEqual('A12345678', result.writer_id)