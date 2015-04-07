# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Transmission grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseTransmissionHeader(unittest.TestCase):
    """
    Tests that the Transmission Header grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_header')

    def test_valid_full(self):
        """
        Tests that Transmission Header grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.record_type)
        self.assertEqual('AA', result.sender_type)
        self.assertEqual(1234, result.sender_id)
        self.assertEqual('NAME OF THE COMPANY', result.sender_name)
        self.assertEqual('01.10', result.edi_standard)
        self.assertEqual(2012, result.creation_date_time.year)
        self.assertEqual(1, result.creation_date_time.month)
        self.assertEqual(15, result.creation_date_time.day)
        self.assertEqual(12, result.creation_date_time.hour)
        self.assertEqual(30, result.creation_date_time.minute)
        self.assertEqual(0, result.creation_date_time.second)
        self.assertEqual(2012, result.transmission_date.year)
        self.assertEqual(11, result.transmission_date.month)
        self.assertEqual(2, result.transmission_date.day)
        self.assertEqual('U+0123', result.character_set)

    def test_valid_no_charset(self):
        """
        Tests that TransmissionHeaderDecoder decodes correctly formatted record prefixes.

        This is missing the optional charset field.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102               '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.record_type)
        self.assertEqual('AA', result.sender_type)
        self.assertEqual(1234, result.sender_id)
        self.assertEqual('NAME OF THE COMPANY', result.sender_name)
        self.assertEqual('01.10', result.edi_standard)
        self.assertEqual(2012, result.creation_date_time.year)
        self.assertEqual(1, result.creation_date_time.month)
        self.assertEqual(15, result.creation_date_time.day)
        self.assertEqual(12, result.creation_date_time.hour)
        self.assertEqual(30, result.creation_date_time.minute)
        self.assertEqual(0, result.creation_date_time.second)
        self.assertEqual(2012, result.transmission_date.year)
        self.assertEqual(11, result.transmission_date.month)
        self.assertEqual(2, result.transmission_date.day)
        self.assertEqual(None, result.character_set)


class TestParseTransmissionTrailer(unittest.TestCase):
    """
    Tests that TransmissionTrailerDecoder decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_trailer')

    def test_valid_full(self):
        """
        Tests that TransmissionTrailerDecoder decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'TRL012340123456701234568'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TRL', result.record_type)
        self.assertEqual(1234, result.group_count)
        self.assertEqual(1234567, result.transaction_count)
        self.assertEqual(1234568, result.record_count)


class TestParseTransmissionHeaderException(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_header')

    def test_invalid_wrong_type(self):
        """
        Tests that TransmissionHeaderDecoder throws an exception when the record type is not one of the CWR record types.
        """
        record = 'AAAAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid_lower_case_name(self):
        """
        Tests that TransmissionHeaderDecoder throws an exception when the company name is in lower case.
        """
        record = 'HDRAA000001234name of the company                          01.102012011512300020121102U+0123         '

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that TransmissionHeaderDecoder throws an exception when the record size is too short.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123        '

        self.assertRaises(ParseException, self.grammar.parseString, record)


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
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('transmission_header')

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that TransmissionTrailerDecoder throws an exception when the line is too short.
        """
        record = 'TRL01234012345670123456'

        self.assertRaises(ParseException, self.grammar.parseString, record)