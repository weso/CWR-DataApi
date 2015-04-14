# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import DefaultPrefixBuilder, DefaultRecordFactory


"""
CWR Group Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupHeaderGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = DefaultPrefixBuilder(_config.record_types(), _factory_field)
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('group_header')

    def test_valid_full(self):
        record = 'GRHAGR0000102.100130400001  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual(1, result.group_id)
        self.assertEqual('AGR', result.transaction_type)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(130400001, result.batch_request_id)
