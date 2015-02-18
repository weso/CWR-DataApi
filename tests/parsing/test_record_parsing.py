# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.parsing.record import RecordPrefixDecoder


"""
CWR record parsing tests.

The following cases are tested:
- RecordPrefixDecoder decodes correctly formatted record prefixes
- RecordPrefixDecoder ignores extra values when the record numbers are too long

- RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types
- RecordPrefixDecoder throws an exception when the record numbers are too short
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseRecordPrefixValid(unittest.TestCase):
    """
    Tests that RecordPrefixDecoder decodes correctly formatted strings, and those where the error can be corrected
    """

    def setUp(self):
        self._parser = RecordPrefixDecoder()

    def test_valid(self):
        """
        Tests that RecordPrefixDecoder decodes correctly formatted record prefixes.
        """
        prefix = 'HDR0000123400000023'

        result = self._parser.parse(prefix)

        self.assertEqual('HDR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)

    def test_numbers_length_too_long(self):
        """
        Tests that RecordPrefixDecoder ignores extra values when the record numbers are too long.
        """
        prefix = 'HDR00000123400000023'

        result = self._parser.parse(prefix)

        self.assertEqual('HDR', result.record_type)
        self.assertEqual(123, result.transaction_sequence_n)
        self.assertEqual(40000002, result.record_sequence_n)


class TestParseRecordPrefixException(unittest.TestCase):
    """
    Tests that RecordPrefixDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self._parser = RecordPrefixDecoder()

    def test_invalid_wrong_type(self):
        """
        Tests that RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types.
        """
        prefix = 'AAA0000123400000023'

        self.assertRaises(ParseException, self._parser.parse, prefix)

    def test_invalid_wrong_length_too_short(self):
        """
        Tests that RecordPrefixDecoder throws an exception when the record numbers are too short.
        """
        prefix = 'HDR000123400000023'

        self.assertRaises(ParseException, self._parser.parse, prefix)