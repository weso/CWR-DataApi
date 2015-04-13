# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, DefaultRecordFactory
from cwr.grammar.factory.transaction import DefaultTransactionFactory

"""
CWR Instrumentation Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentationInformationValid(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)
        _factory_transaction = DefaultTransactionFactory(_config.load_transaction_config('common'), _factory_record)

        self.grammar = _factory_transaction.get_transaction('instrumentation_information')

    def test_valid_full(self):
        summary = 'INS0000123400000023012BBADESCRIPTION                                       '
        detail_1 = 'IND0000123400000023ALT123'
        detail_2 = 'IND0000123400000023ALT123'

        record = summary + '\n' + detail_1 + '\n' + detail_2

        result = self.grammar.parseString(record)

        self.assertEqual(3, len(result))

        self.assertEqual('INS', result[0].record_type)
        self.assertEqual('IND', result[1].record_type)
        self.assertEqual('IND', result[2].record_type)

    def test_min(self):
        summary = 'INS0000123400000023012BBADESCRIPTION                                       '

        record = summary

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('INS', result[0].record_type)