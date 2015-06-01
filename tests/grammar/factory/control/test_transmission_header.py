# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from tests.utils.grammar import get_record_grammar

"""
CWR Transaction Header grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestTransmissionHeaderGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = get_record_grammar('transmission_header')

    def test_valid_common(self):
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


class TestParseTransmissionHeaderException(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self.grammar = get_record_grammar('transmission_header')

    def test_empty(self):
        record = ''

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_invalid(self):
        record = 'This is an invalid string'

        self.assertRaises(ParseException, self.grammar.parseString, record)
