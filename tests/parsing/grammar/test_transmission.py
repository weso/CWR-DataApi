# -*- encoding: utf-8 -*-
import unittest
import datetime

from pyparsing import ParseException

from cwr.parsing.grammar import transmission


"""
CWR record parsing tests.

The following cases are tested:
- RecordPrefixDecoder decodes correctly formatted transmission headers
- RecordPrefixDecoder decodes correctly transmission headers without the optional character set

- RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types
- RecordPrefixDecoder throws an exception when the company name is in lower case
- RecordPrefixDecoder throws an exception when the record numbers are too short
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
        self.grammar = transmission.transmission_header

    def test_valid_full(self):
        """
        Tests that TransmissionHeaderDecoder decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('HDR', result.record_type)
        self.assertEqual('AA', result.sender_type)
        self.assertEqual(1234, result.sender_id)
        self.assertEqual('NAME OF THE COMPANY', result.sender_name)
        self.assertEqual('01.10', result.edi_standard)
        self.assertEqual(datetime.datetime.strptime('20120115', '%Y%m%d').date(), result.creation_date)
        self.assertEqual(datetime.datetime.strptime('123000', '%H%M%S').time(), result.creation_time)
        self.assertEqual(datetime.datetime.strptime('20121102', '%Y%m%d').date(), result.transmission_date)
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
        self.assertEqual(datetime.datetime.strptime('20120115', '%Y%m%d').date(), result.creation_date)
        self.assertEqual(datetime.datetime.strptime('123000', '%H%M%S').time(), result.creation_time)
        self.assertEqual(datetime.datetime.strptime('20121102', '%Y%m%d').date(), result.transmission_date)
        self.assertEqual('', result.character_set)


class TestParseTransmissionTrailer(unittest.TestCase):
    """
    Tests that TransmissionTrailerDecoder decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = transmission.transmission_trailer

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
        self.grammar = transmission.transmission_header

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
        self.grammar = transmission.transmission_header

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that TransmissionTrailerDecoder throws an exception when the line is too short.
        """
        record = 'TRL01234012345670123456'

        self.assertRaises(ParseException, self.grammar.parseString, record)