# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import DefaultPrefixBuilder, DefaultRecordFactory


"""
CWR Alternate Title grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAlternateTitleGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = DefaultPrefixBuilder(_config.record_types())
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('work_alternate_title')

    def test_extended_character(self):
        record = 'ALT0000028200001380PA\xc6\x8f                                                        AT  '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ALT', result.record_type)
        self.assertEqual(282, result.transaction_sequence_n)
        self.assertEqual(1380, result.record_sequence_n)
        self.assertEqual('PA\xc6\x8f', result.alternate_title)
        self.assertEqual('AT', result.title_type)
        self.assertEqual(None, result.language_code)

    def test_valid_full(self):
        record = 'ALT0000123400000023THE TITLE                                                   ATES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ALT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.alternate_title)
        self.assertEqual('AT', result.title_type)
        self.assertEqual('ES', result.language_code)
