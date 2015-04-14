# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import DefaultPrefixBuilder, DefaultRecordFactory


"""
CWR Non-Roman Alphabet Publisher Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPRGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = DefaultPrefixBuilder(_config.record_types(), _factory_field)
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('nra_performance_data')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPR0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      00014107338I-000000229-7ESENCAN'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME', result.performing_artist_name)
        self.assertEqual('FIRST NAME', result.performing_artist_first_name)
        self.assertEqual(14107338, result.performing_artist_ipi_name_n)
        self.assertEqual('I', result.performing_artist_ipi_base_n.header)
        self.assertEqual(229, result.performing_artist_ipi_base_n.id_code)
        self.assertEqual(7, result.performing_artist_ipi_base_n.check_digit)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('EN', result.performance_language)
        self.assertEqual('CAN', result.performance_dialect)