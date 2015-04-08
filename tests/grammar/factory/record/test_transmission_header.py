# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Transaction Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionHeaderGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_header')

    def test_valid_full(self):
        record = 'HDRPB226144593AGENCIA GRUPO MUSICAL                        01.102013080902591120130809               '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.record_type)
        self.assertEqual('PB', result.sender_type)
        self.assertEqual(226144593, result.sender_id)
        self.assertEqual('AGENCIA GRUPO MUSICAL', result.sender_name)
        self.assertEqual('01.10', result.edi_standard)
        self.assertEqual(2013, result.creation_date_time.year)
        self.assertEqual(8, result.creation_date_time.month)
        self.assertEqual(9, result.creation_date_time.day)
        self.assertEqual(2, result.creation_date_time.hour)
        self.assertEqual(59, result.creation_date_time.minute)
        self.assertEqual(11, result.creation_date_time.second)
        self.assertEqual(2013, result.transmission_date.year)
        self.assertEqual(8, result.transmission_date.month)
        self.assertEqual(9, result.transmission_date.day)
