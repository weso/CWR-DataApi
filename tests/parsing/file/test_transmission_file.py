# -*- encoding: utf-8 -*-
import unittest

from cwr.parsing.transmission import TransmissionHeaderDecoder

"""
CWR record parsing tests.

The following cases are tested:
- RecordPrefixDecoder decodes correctly formatted record prefixes

- RecordPrefixDecoder throws an exception when the record type is not one of the CWR record types
- RecordPrefixDecoder throws an exception when the record numbers are too short
- RecordPrefixDecoder throws an exception when the record numbers are too long
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionHeader(unittest.TestCase):
    """
    Tests that TransmissionHeaderDecoder decodes correctly formatted strings
    """

    def setUp(self):
        self._parser = TransmissionHeaderDecoder()

    def test_valid(self):
        """
        Tests that TransmissionHeaderDecoder decodes correctly formatted record prefixes.
        """
        record = 'HDRAA000001234NAME OF THE COMPANY                          01.102012011512300020121102U+0123         '

        result = self._parser.decode(record)
        print result