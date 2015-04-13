# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, DefaultRecordFactory


"""
CWR Transaction Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionTrailerGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_trailer')

    def test_valid_full(self):
        record = 'TRL000020000053200005703'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TRL', result.record_type)
        self.assertEqual(2, result.group_count)
        self.assertEqual(532, result.transaction_count)
        self.assertEqual(5703, result.record_count)


class TestParseTransmissionTrailerException(unittest.TestCase):
    """
    Tests that TransmissionTrailerDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_header')

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that TransmissionTrailerDecoder throws an exception when the line is too short.
        """
        record = 'TRL01234012345670123456'

        self.assertRaises(ParseException, self.grammar.parseString, record)
