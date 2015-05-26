# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException
from cwr.grammar.factory.rule import FieldRuleFactory

from config_cwr.accessor import CWRConfiguration
from cwr.grammar.field.record import record_prefix
from cwr.parser.decoder.file import default_adapters

"""
CWR file Record parsing tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_common_factory = FieldRuleFactory(_config.load_field_config('common'), default_adapters())


class TestParseTransactionRecordPrefixValid(unittest.TestCase):
    """
    Tests that RecordPrefixDecoder decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = record_prefix('HDR', _common_factory)

    def test_valid(self):
        """
        Tests that RecordPrefixDecoder decodes correctly formatted record prefixes.
        """
        prefix = 'HDR0000123400000023'

        result = self.grammar.parseString(prefix)

        self.assertEqual('HDR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)


class TestParseRecordPrefixException(unittest.TestCase):
    """
    Tests that RecordPrefixDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self.grammar = record_prefix('HDR', _common_factory)

    def test_wrong_type(self):
        """
        Tests that RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types.
        """
        prefix = 'AAA0000123400000023'

        self.assertRaises(ParseException, self.grammar.parseString, prefix)

    def test_record_n_too_short(self):
        """
        Tests that RecordPrefixDecoder throws an exception when the record numbers are too short.
        """
        prefix = 'HDR000123400000023'

        self.assertRaises(ParseException, self.grammar.parseString, prefix)

    def test_begins_empty(self):
        """
        Tests that RecordPrefixDecoder throws an exception when the prefix is headed by empty spaces.
        """
        prefix = ' HDR0000123400000023'

        self.assertRaises(ParseException, self.grammar.parseString, prefix)
