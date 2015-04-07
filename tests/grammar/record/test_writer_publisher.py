# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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
        _config = CWRConfiguration()

        _factory_field = DefaultFieldFactory(_config.load_field_config('common'))

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('writer_publisher')

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
        self.assertEqual('A12345678', result.publisher_ip_n)
        # self.assertEqual('THE PUBLISHER', result.publisher_name)
        self.assertEqual('C1234567890123', result.submitter_agreement_n)
        self.assertEqual('D1234567890123', result.society_assigned_agreement_n)
        self.assertEqual('A12345678', result.writer_ip_n)