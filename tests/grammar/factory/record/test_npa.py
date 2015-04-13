# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Non-Roman Alphabet Agreement Party Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPAGrammar(unittest.TestCase):
    """
    Tests that the NPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('nra_agreement_party')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPA0000123400000023012345678PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                               ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('012345678', result.ip_n)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual('ES', result.language_code)

    def test_valid_min(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'NPA0000123400000023000000000PARTY NAME                                                                                                                                                      PARTY WRITER NAME                                                                                                                                                 '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('000000000', result.ip_n)
        self.assertEqual('PARTY NAME', result.ip_name)
        self.assertEqual('PARTY WRITER NAME', result.ip_writer_name)
        self.assertEqual(None, result.language_code)