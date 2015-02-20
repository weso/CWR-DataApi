# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.parsing.transmission import TransmissionHeaderDecoder

"""
CWR record parsing tests.

The following cases are tested:
- RecordPrefixDecoder decodes correctly formatted record prefixes

- RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types
- RecordPrefixDecoder throws an exception when the record numbers are too short
- RecordPrefixDecoder throws an exception when the record numbers are too long
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseTransmissionHeader(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder decodes correctly formatted strings
    """

    def setUp(self):
        self._parser = TransmissionHeaderDecoder()

    def test_valid_full(self):
        """
        Tests that TransmissionHeaderDecoder decodes correctly formatted record prefixes.

        This contains all the fields
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        result = self._parser.decode(record)

    def test_valid_no_charset(self):
        """
        Tests that TransmissionHeaderDecoder decodes correctly formatted record prefixes.

        This is missing the optional charset field.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102               '

        result = self._parser.decode(record)


class TestParseTransmissionHeaderException(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self._parser = TransmissionHeaderDecoder()

    def test_invalid_wrong_type(self):
        """
        Tests that TransmissionHeaderDecoder throws an exception when the record type is not one of the CWR record types.
        """
        record = 'AAAAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        self.assertRaises(ParseException, self._parser.decode, record)

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that TransmissionHeaderDecoder throws an exception when the record size is too short.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123        '

        self.assertRaises(ParseException, self._parser.decode, record)