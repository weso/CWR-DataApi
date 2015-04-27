# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.transmission import TransmissionTrailer


"""
TransmissionTrailer to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionTrailerDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = TransmissionTrailer(record_type='TRL',
                                   group_count=155,
                                   transaction_count=245,
                                   record_count=568)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('TRL', encoded['record_type'])
        self.assertEqual(155, encoded['group_count'])
        self.assertEqual(245, encoded['transaction_count'])
        self.assertEqual(568, encoded['record_count'])