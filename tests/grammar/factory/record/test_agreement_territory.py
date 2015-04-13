# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Territory in Agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseAgreementTerritory(unittest.TestCase):
    """
    Tests that the Territory in Agreement grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('territory_in_agreement')

    def test_valid(self):
        """
        Tests that Territory in Agreement grammar decodes correctly formatted record prefixes.
        """
        record = 'TER0000123400000023I0020'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(20, result.tis_numeric_code)