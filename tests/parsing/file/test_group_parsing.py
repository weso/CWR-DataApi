# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.parsing.group import GroupHeaderDecoder

"""
CWR group parsing tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseGroupHeader(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder decodes correctly formatted strings
    """

    def setUp(self):
        self._parser = GroupHeaderDecoder()

    def test_valid_full(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.100123456789  '

        result = self._parser.decode(record)

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(123456789, result.batch_request_id)

    def test_valid_no_batch_request(self):
        """
        Tests that GroupHeaderDecoder decodes a Group Header with no batch id.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.10000000000000  '

        result = self._parser.decode(record)

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(0, result.batch_request_id)


class TestParseGroupHeaderException(unittest.TestCase):
    """
    Tests that GroupHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def setUp(self):
        self._parser = GroupHeaderDecoder()

    def test_invalid_wrong_type(self):
        """
        Tests that GroupHeaderDecoder throws an exception when the group ID is 0.
        """
        # TODO: Check the exception's info
        record = 'GRHACK0000002.100123456789  '

        self.assertRaises(ParseException, self._parser.decode, record)